# Slack GPT Bot: Wyl 🤖

Hi from Wyl, a Python-based Slack GPT Bot that leverages the power of OpenAI's GPT models to answer user queries in real-time. Primed with a knowledge base of quality tech advice and backed by a vector database, Wyl serves as a helpful resource for developers, especially junior engineers, seeking advice on best practices and technical questions.

Wyl features powerful capabilities such as information retrieval from its modifiable knowledgebase, and summarisation tasks. All these features make Wyl more than just a bot, but a smart assistant that improves productivity and collaboration.

## Key Features 💡

- Group Chats: Wyl seamlessly integrates into your Slack workspace and interacts within group chats.
- Information Retrieval: Backed by OpenAI's GPT models, Wyl can provide detailed responses to a broad range of technical queries.
- Modifiable Knowledgebase: Update Wyl's knowledgebase with the latest and most accurate tech advice.
- Summarisation Tasks: Wyl can summarize lengthy technical documents, making them easier to understand and consume.

The intention of this project is to create a smart assistant for developers, capable of providing sound advice and assistance when it comes to best practices or asking technical questions.

Let's get started with Wyl! ⬇️

## Installation

1. Clone this repository:

```bash
git clone git@github.com:eh-93/wylai.git
cd wylai
```

2. Install the required packages:

```bash
cd api
pip install -r requirements.txt
```

3. Create a .env file in the root directory of the project and add your Slack and OpenAI API keys:

```bash
export OPENAI_API_KEY=""
export SERPAPI_API_KEY=""
export SLACK_BOT_TOKEN=""
export SLACK_APP_TOKEN=""

```

See below how to get those.

## Configuring Permissions in Slack

Before you can run the Slack GPT Bot, you need to configure the appropriate permissions for your Slack bot. Follow these steps to set up the necessary permissions:

1. Create [Slack App](https://api.slack.com/authentication/basics)
2. Go to your [Slack API Dashboard](https://api.slack.com/apps) and click on the app you created for this bot.
3. In the left sidebar, click on "OAuth & Permissions".
4. In the "Scopes" section, you will find two types of scopes: "Bot Token Scopes" and "User Token Scopes". Add the following scopes under "Bot Token Scopes":
   - `app_mentions:read`: Allows the bot to read mention events.
   - `chat:write`: Allows the bot to send messages.
5. Scroll up to the "OAuth Tokens for Your Workspace" and click "Install App To Workspace" button. This will generate the `SLACK_BOT_TOKEN`.
6. In the left sidebar, click on "Socket Mode" and enable it. You'll be prompted to "Generate an app-level token to enable Socket Mode". Generate a token named `SLACK_APP_TOKEN` and add the `connections:write` scope.
7. In the "Features affected" section of "Socket Mode" page, click "Event Subscriptions" and toggle "Enable Events" to "On". Add `app_mention` event with the `app_mentions:read` scope in the "Subscribe to bot events" section below the toggle.

## Usage

1. Start the bot:

```
python api/main.py
```

2. Invite the bot to your desired Slack channel.
3. Mention the bot in a message and ask a question (including any URLs). The bot will respond with an answer.
