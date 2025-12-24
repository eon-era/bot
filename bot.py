import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get the bot token from environment variables
TOKEN = os.getenv('DISCORD_TOKEN')

# Create bot instance with command prefix and required intents
intents = discord.Intents.default()
intents.message_content = True  # Required for reading message content
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    """Event handler that runs when the bot is ready"""
    print(f'{bot.user} has connected to Discord!')

@bot.command(name='ping')
async def ping(ctx):
    """Responds to !ping command with Pong!"""
    await ctx.send('Pong!')

# Run the bot
if __name__ == '__main__':
    if not TOKEN:
        print('Error: DISCORD_TOKEN not found in environment variables.')
        print('Please add your Discord bot token to the .env file.')
        exit(1)
    bot.run(TOKEN)
