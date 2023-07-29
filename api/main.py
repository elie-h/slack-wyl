import datetime
from typing import Optional

from ai import generate_response_V2
from config import SLACK_CLIENT_ID, SLACK_CLIENT_SECRET, SLACK_SIGNING_SECRET
from fastapi import FastAPI, Request, Response, status
from fastapi.concurrency import run_in_threadpool
from fastapi.responses import RedirectResponse
from models import SlackAppMentionModel
from slack_bolt.adapter.fastapi.async_handler import AsyncSlackRequestHandler
from slack_bolt.async_app import AsyncApp
from slack_bolt.oauth.async_oauth_settings import AsyncOAuthSettings
from slack_sdk.oauth.installation_store import Installation
from utils import WAIT_MESSAGE, get_slack_thread, sanitise_slack_thread, update_chat

from prisma import Prisma
from prisma.errors import UniqueViolationError

prisma = Prisma()

api = FastAPI(
    title="Wyl",
    version="0.1.0",
    docs_url="/docs",
)


class AsyncInstallationStore:
    async def async_save(self, installation: Installation):
        if installation.team_id is None:
            raise Exception("enterprise_id and team_id must be set")
        try:
            await prisma.slackinstallation.create(
                data={
                    "app_id": installation.app_id,
                    "enterprise_id": installation.enterprise_id,
                    "team_id": installation.team_id,
                    "user_id": installation.user_id,
                    "bot_token": installation.bot_token,
                    "bot_id": installation.bot_id,
                    "bot_user_id": installation.bot_user_id,
                    "is_enterprise_install": installation.is_enterprise_install,
                    "installed_at": datetime.datetime.utcfromtimestamp(installation.installed_at),
                }
            )
        except UniqueViolationError:
            print(f"installation already exists for {installation.enterprise_id=} {installation.team_id=}")

    async def async_find_installation(
        self,
        *,
        enterprise_id: Optional[str],
        team_id: Optional[str],
        user_id: Optional[str] = None,
        is_enterprise_install: Optional[bool] = False,
    ) -> Optional[Installation]:
        if team_id is None:
            raise Exception("team_id must be set")
        si = await prisma.slackinstallation.find_first(
            where={
                "enterprise_id": enterprise_id,
                "team_id": team_id,
            }
        )
        if si:
            return Installation(
                app_id=si.app_id,
                enterprise_id=si.enterprise_id,
                team_id=si.team_id,
                user_id=si.user_id if si.user_id else "",
                bot_token=si.bot_token,
                bot_id=si.bot_id,
                bot_user_id=si.bot_user_id,
                is_enterprise_install=si.is_enterprise_install,
                installed_at=si.installed_at.timestamp(),
            )
        print(f"No installation found for {enterprise_id=} {team_id=}")
        return None  # TODO: Alert someone


bolt_app = AsyncApp(
    signing_secret=SLACK_SIGNING_SECRET,
    oauth_settings=AsyncOAuthSettings(
        client_id=SLACK_CLIENT_ID,
        client_secret=SLACK_CLIENT_SECRET,
        scopes=[
            "app_mentions:read",
            "coversations:reply",
            "channels:history",
            "channels:read",
            "chat:write",
            "commands",
            "groups:read",
            "groups:history",
            "im:history",
            "im:write",
            "mpim:history",
        ],
        state_validation_enabled=False,  # TODO:
        user_scopes=[],
        redirect_uri_path="/slack/oauth_redirect",
        installation_store=AsyncInstallationStore(),  # type: ignore
    ),
)

bolt_handler = AsyncSlackRequestHandler(bolt_app)


@api.on_event("startup")
async def startup_event():
    await prisma.connect()
    api.state.prisma = prisma


@api.on_event("shutdown")
async def shutdown_event():
    await api.state.prisma.disconnect()


@api.get("/health")
async def health():
    return {"status": "ok"}


@api.get("/", include_in_schema=False)
async def root():
    return RedirectResponse("/docs")


async def process_app_mention_event(client, app_mention_event: SlackAppMentionModel):
    channel_id = app_mention_event.event.channel
    thread_ts = app_mention_event.event.thread_ts if app_mention_event.event.thread_ts else app_mention_event.event.ts
    bot_user_id = app_mention_event.event.user

    conversation_history = await get_slack_thread(client, channel_id, thread_ts)
    messages = sanitise_slack_thread(conversation_history, bot_user_id)

    slack_resp = await client.chat_postMessage(channel=channel_id, thread_ts=thread_ts, text=WAIT_MESSAGE)
    reply_message_ts = slack_resp.get("message", {}).get(
        "ts", None
    )  # This is the message to be updated with the model response

    if not reply_message_ts:
        print("Error: could not get reply message ts")
        return

    ai_response = await run_in_threadpool(generate_response_V2, messages)
    await update_chat(client, channel_id, reply_message_ts, ai_response)


@bolt_app.event("app_mention")
async def process_app_mention(body, say, client, context):
    await context.ack()
    event_model = SlackAppMentionModel(**body)
    await process_app_mention_event(client, event_model)


@bolt_app.event("message")
async def process_direct_message(body, say, client, context, ack):
    await context.ack()
    event_model = SlackAppMentionModel(**body)
    await process_app_mention_event(client, event_model)


@api.post("/slack/events", status_code=status.HTTP_200_OK)
async def process_slack_event(
    request: Request,
):
    retry_count = request.headers.get("X-Slack-Retry-Num")
    if retry_count is not None:
        retry_count = int(retry_count)
        retry_reason = request.headers.get("X-Slack-Retry-Reason")
        print(f"Slack attempted to retry a message -  {retry_count=} {retry_reason=}")  # TODO: Alert on this
        # We're assuming it's a duplicate so we just ack it to avoid responding twice
        # See https://api.slack.com/apis/connections/events-api#retries
        return Response(status_code=status.HTTP_200_OK)
    return await bolt_handler.handle(request)


@api.get("/slack/oauth_redirect", status_code=status.HTTP_200_OK)
async def process_slack_redirect(
    request: Request,
):
    return await bolt_handler.handle(request)
