from starlette.config import Config

config = Config(".env")

DEBUG = config("DEBUG", cast=bool, default=False)
QDRANT_URL = config("QDRANT_URL", cast=str)
QDRANT_API_KEY = config("QDRANT_API_KEY", cast=str)
OPENAI_API_KEY = config("OPENAI_API_KEY", cast=str)
# SLACK_BOT_TOKEN = config("SLACK_BOT_TOKEN", cast=str)
# SLACK_APP_TOKEN = config("SLACK_APP_TOKEN", cast=str)
SLACK_CLIENT_ID = config("SLACK_CLIENT_ID", cast=str)
SLACK_CLIENT_SECRET = config("SLACK_CLIENT_SECRET", cast=str)
SLACK_SIGNING_SECRET = config("SLACK_SIGNING_SECRET", cast=str)
REDIS_URL = config("REDIS_URL", cast=str)
PORT = config("PORT", cast=int, default=8080)
LANGCHAIN_VERBOSE = config("LANGCHAIN_VERBOSE", cast=bool, default=False)
