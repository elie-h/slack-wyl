# import os
# import pprint

# from ai import generate_response_V2, generate_thread_summary
# from models import SlackAppMentionModel
# from slack_bolt.adapter.socket_mode.async_handler import AsyncSocketModeHandler
# from slack_bolt.async_app import AsyncApp
# from utils import WAIT_MESSAGE, get_slack_thread, sanitise_slack_thread, update_chat

# from api.ai import generate_response, generate_thread_summary
# from api.models import SlackAppMentionModel
# from api.utils import WAIT_MESSAGE, get_slack_thread, sanitise_slack_thread, update_chat

# pp = pprint.PrettyPrinter(indent=1)


# SLACK_BOT_TOKEN = os.getenv("SLACK_BOT_TOKEN")
# SLACK_APP_TOKEN = os.environ.get("SLACK_APP_TOKEN")
# app = AsyncApp(token=SLACK_BOT_TOKEN)


# @app.event("app_mention")
# async def process_app_mention(body, say, context):
#     message = SlackAppMentionModel(**body)
#     channel_id = message.event.channel
#     thread_ts = body["event"].get("thread_ts", body["event"]["ts"])
#     bot_user_id = context["bot_user_id"]

#     conversation_history = await get_slack_thread(app, channel_id, thread_ts)
#     messages = sanitise_slack_thread(conversation_history, bot_user_id)
#     pp.pprint(messages)  # This is the conversation to be fed to the model

#     slack_resp = await app.client.chat_postMessage(
#         channel=channel_id, thread_ts=thread_ts, text=WAIT_MESSAGE
#     )
#     reply_message_ts = slack_resp.get("message", {}).get(
#         "ts", None
#     )  # This is the message to be updated with the model response


#     if not reply_message_ts:
#         print("Error: could not get reply message ts")
#         return

#     ai_response = await generate_response(messages)
#     await update_chat(app, channel_id, reply_message_ts, ai_response)


# @app.shortcut("summarise_thread")
# async def process_summarise_request(ack, shortcut, say, context):
#     await ack()
#     channel_id = shortcut["channel"]["id"]
#     thread_ts = shortcut["message"]["ts"]
#     bot_user_id = context["bot_user_id"]

#     slack_resp = await app.client.chat_postMessage(
#         channel=channel_id,
#         thread_ts=thread_ts,
#         text="Generating summary... :robot_face:",
#     )

#     conversation_history = get_slack_thread(app, channel_id, thread_ts)
#     messages = sanitise_slack_thread(conversation_history, bot_user_id)
#     ai_summary = await generate_thread_summary(messages)
#     reply_message_ts = slack_resp.get("message", {}).get("ts", None)

#     if not reply_message_ts:
#         print("Error: could not get reply message ts")
#         return
#     await update_chat(app, channel_id, reply_message_ts, ai_summary)


# @app.event("message")
# async def process_message(body, say, context):
#     print("ignore message event")
#     return


# async def main():
#     handler = AsyncSocketModeHandler(app, os.environ["SLACK_APP_TOKEN"])
#     await handler.start_async()


# if __name__ == "__main__":
#     import asyncio

#     asyncio.run(main())
