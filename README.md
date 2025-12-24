# Discord Bot

A simple Discord bot that responds to the `!ping` command with `Pong!`.

## Features

- Responds to `!ping` command with `Pong!`
- Secure token management using environment variables
- Simple and easy to set up

## Prerequisites

- Python 3.8 or higher
- A Discord bot token (see setup instructions below)

## Setup Instructions

### 1. Clone the Repository

```bash
git clone <repository-url>
cd bot
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Create a Discord Bot

1. Go to the [Discord Developer Portal](https://discord.com/developers/applications)
2. Click "New Application" and give it a name
3. Go to the "Bot" section and click "Add Bot"
4. Under the "Privileged Gateway Intents" section, enable "Message Content Intent"
5. Under the "Token" section, click "Copy" to copy your bot token
6. Go to the "OAuth2" > "URL Generator" section
7. Select the following scopes:
   - `bot`
8. Select the following bot permissions:
   - `Send Messages`
   - `Read Message History`
9. Copy the generated URL and open it in your browser to invite the bot to your server

### 4. Configure the Bot Token

1. Copy the `.env.example` file to `.env`:

```bash
cp .env.example .env
```

2. Open the `.env` file and replace `your_bot_token_here` with your actual Discord bot token:

```
DISCORD_TOKEN=your_actual_bot_token_here
```

**Important:** Never commit your `.env` file with the actual token to version control. The `.gitignore` file is already configured to exclude it.

### 5. Run the Bot

```bash
python bot.py
```

You should see a message like:
```
BotName#1234 has connected to Discord!
```

## Usage

Once the bot is running and added to your Discord server, you can use the following command:

- `!ping` - The bot will respond with `Pong!`

## Security Notes

- The bot token is stored in the `.env` file which is excluded from version control
- Never share your bot token publicly
- If your token is compromised, regenerate it immediately in the Discord Developer Portal

## Troubleshooting

**Error: DISCORD_TOKEN not found in environment variables**
- Make sure you have created the `.env` file and added your token
- Verify the token key is exactly `DISCORD_TOKEN`

**Bot doesn't respond to commands**
- Make sure the bot has been invited to your server
- Verify the bot has permission to read and send messages in the channel
- Check that you're using the correct command prefix (`!`)

## License

This project is open source and available under the MIT License.