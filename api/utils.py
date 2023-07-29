from pydantic import BaseModel
from enum import Enum
import re

WAIT_MESSAGE = "Thinking ..."


class RoleEnum(str, Enum):
    USER = "user"
    AI = "ai"


class Message(BaseModel):
    role: RoleEnum
    content: str


def sanitise_slack_thread(conversation_history, bot_user_id: str) -> list[Message]:
    messages: list[Message] = []
    for message in conversation_history["messages"]:
        if "bot_id" in message:
            role = RoleEnum.AI
            message_text = message["text"].replace(f"<@{bot_user_id}>", "").strip()
        else:
            role = RoleEnum.USER
            message_text = message["text"]

        if message_text:
            message_text = re.sub(r"<@[^>]+>", "", message_text)  # Remove remaining Slack IDs
            messages.append(Message(role=role, content=message_text))
        else:
            print(f"Warning: message {message} was skipped.")
            continue
    return messages


# Slack utils
async def update_chat(client, channel_id, reply_message_ts, response_text):
    await client.chat_update(channel=channel_id, ts=reply_message_ts, text=response_text)


async def get_slack_thread(client, channel_id, thread_ts):
    history = await client.conversations_replies(channel=channel_id, ts=thread_ts, inclusive=False)
    return history


if __name__ == "__main__":
    conversation_history = {
        "ok": True,
        "messages": [
            {
                "client_msg_id": "6fa8bf9c-4dbf-48a6-b176-2f75016f5184",
                "type": "message",
                "text": "<@U053DTHLUT1> what’s the best",
                "user": "U053DQMHTK9",
                "ts": "1682634632.471029",
                "blocks": [
                    {
                        "type": "rich_text",
                        "block_id": "m0GU",
                        "elements": [
                            {
                                "type": "rich_text_section",
                                "elements": [
                                    {"type": "user", "user_id": "U053DTHLUT1"},
                                    {"type": "text", "text": " what’s the best"},
                                ],
                            }
                        ],
                    }
                ],
                "team": "T054J209GCQ",
                "thread_ts": "1682634632.471029",
                "reply_count": 2,
                "reply_users_count": 2,
                "latest_reply": "1682634738.596889",
                "reply_users": ["U053DTHLUT1", "U053DQMHTK9"],
                "is_locked": False,
                "subscribed": False,
            },
            {
                "bot_id": "B053WU3T57E",
                "type": "message",
                "text": "The best what? Can you please provide more context or about what you are looking for?",
                "user": "U053DTHLUT1",
                "ts": "1682634633.888689",
                "app_id": "A053UCMPAV8",
                "team": "T054J209GCQ",
                "bot_profile": {
                    "id": "B053WU3T57E",
                    "deleted": False,
                    "name": "wyl",
                    "updated": 1682370174,
                    "app_id": "A053UCMPAV8",
                    "icons": {
                        "image_36": "https://avatars.slack-edge.com/2023-04-24/5163013760868_de0d2cb6059eeaa8de30_36.png",
                        "image_48": "https://avatars.slack-edge.com/2023-04-24/5163013760868_de0d2cb6059eeaa8de30_48.png",
                        "image_72": "https://avatars.slack-edge.com/2023-04-24/5163013760868_de0d2cb6059eeaa8de30_72.png",
                    },
                    "team_id": "T054J209GCQ",
                },
                "edited": {"user": "B053WU3T57E", "ts": "1682634636.000000"},
                "thread_ts": "1682634632.471029",
                "parent_user_id": "U053DQMHTK9",
            },
            {
                "client_msg_id": "8eeab372-bd5e-4c31-8a8c-fa4e746bd472",
                "type": "message",
                "text": "<@U053DTHLUT1> the best in thr world",
                "user": "U053DQMHTK9",
                "ts": "1682634738.596889",
                "blocks": [
                    {
                        "type": "rich_text",
                        "block_id": "Evk",
                        "elements": [
                            {
                                "type": "rich_text_section",
                                "elements": [
                                    {"type": "user", "user_id": "U053DTHLUT1"},
                                    {"type": "text", "text": " the best in thr world"},
                                ],
                            }
                        ],
                    }
                ],
                "team": "T054J209GCQ",
                "thread_ts": "1682634632.471029",
                "parent_user_id": "U053DQMHTK9",
            },
        ],
        "has_more": False,
    }
    messages = sanitise_slack_thread(conversation_history, "U053DTHLUT1")
    print(messages)
