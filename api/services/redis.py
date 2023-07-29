import redis.asyncio as redis
from aredis_om import HashModel
from datetime import datetime


async def init_redis_pool(redis_url: str) -> redis.Redis:
    if not redis_url:
        raise ValueError("REDIS_URL not set")
    redis_c = await redis.from_url(
        redis_url,
        encoding="utf-8",
        db=0,
        decode_responses=True,
    )
    res = await redis_c.ping()
    if not res:
        raise ConnectionError("Could not ping redis")
    return redis_c


class SlackTeam(HashModel):
    # Slack OAuth details
    access_token: str
    token_type: str
    scope: str
    bot_user_id: str
    app_id: str
    team_name: str
    team_id: str
    enterprise_name: str
    enterprise_id: str
    authed_user_id: str
    authed_user_scope: str
    authed_user_access_token: str
    authed_user_token_type: str
    # Usage stats
    n_messages_processed: int
    last_message_processed_at: datetime
    created_at: datetime = datetime.now()
    updated_at: datetime = datetime.now()


# @api.get("/slack/oauth")
# async def oauth(code: str):
#     # Once the user has authorised the app,
#     # Slack will redirect them to this endpoint with the details
#     # needed to interact with the user's workspace
#     # https://api.slack.com/authentication/oauth-v2

#     # We'll need to store the details in the redis so we can use them later
#     # Note: Always check if the team_id exists first otherwise the below will
#     # overwrite the existing details

#     st = SlackTeam(
#         access_token="test",
#         token_type="test",
#         scope="test",
#         bot_user_id="test",
#         app_id="test",
#         team_name="test",
#         team_id="team_id",
#         enterprise_name="test",
#         enterprise_id="test",
#         authed_user_id="test",
#         authed_user_scope="test",
#         authed_user_access_token="test",
#         authed_user_token_type="test",
#         n_messages_processed=0,
#     )
#     st.pk = st.team_id
#     await st.save()
#     return await SlackTeam.get(st.pk)  # Circular, but just testing get/set
