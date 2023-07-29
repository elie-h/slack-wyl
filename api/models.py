from pydantic import BaseModel
from typing import List, Optional

# {
#     "token": "vLHb3ZEZokMS3ed86MtwxLDt",
#     "team_id": "T054J209GCQ",
#     "api_app_id": "A054HS6G4JW",
#     "event": {
#         "client_msg_id": "97b61cfa-8d53-45a6-bb7b-b4197c120347",
#         "type": "app_mention",
#         "text": "<@U054EU0J69K> test",
#         "user": "U05423RBX50",
#         "ts": "1682274846.488879",
#         "blocks": [
#             {
#                 "type": "rich_text",
#                 "block_id": "lCO",
#                 "elements": [
#                     {
#                         "type": "rich_text_section",
#                         "elements": [
#                             {"type": "user", "user_id": "U054EU0J69K"},
#                             {"type": "text", "text": " test"},
#                         ],
#                     }
#                 ],
#             }
#         ],
#         "team": "T054J209GCQ",
#         "channel": "C053U7FNKL3",
#         "event_ts": "1682274846.488879",
#     },
#     "type": "event_callback",
#     "event_id": "Ev054BK8QUMU",
#     "event_time": 1682274846,
#     "authorizations": [
#         {
#             "enterprise_id": None,
#             "team_id": "T054J209GCQ",
#             "user_id": "U054EU0J69K",
#             "is_bot": True,
#             "is_enterprise_install": False,
#         }
#     ],
#     "is_ext_shared_channel": False,
#     "event_context": "4-eyJldCI6ImFwcF9tZW50aW9uIiwidGlkIjoiVDA1NEoyMDlHQ1EiLCJhaWQiOiJBMDU0SFM2RzRKVyIsImNpZCI6IkMwNTNVN0ZOS0wzIn0", # noqa
# }


class SlackAuthorizationModel(BaseModel):
    enterprise_id: Optional[str]
    team_id: str
    user_id: str
    is_bot: bool
    is_enterprise_install: bool


class SlackAppMentionEventModel(BaseModel):
    client_msg_id: str
    type: str
    text: str
    user: str
    ts: str
    thread_ts: Optional[str]
    blocks: List[dict]
    team: str
    channel: str
    event_ts: str


class SlackAppMentionModel(BaseModel):
    token: str
    team_id: str
    api_app_id: str
    event: SlackAppMentionEventModel
    type: str
    event_id: str
    event_time: int
    authorizations: List[SlackAuthorizationModel]
    is_ext_shared_channel: bool
    event_context: str


class SlackChallengeModel(BaseModel):
    token: str
    challenge: str
    type: str
