import os
import sys
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
        sys.exit(1)
    
    try:
        bot.run(TOKEN)
    except discord.LoginFailure:
        print('Error: Invalid Discord token.')
        print('Please check your DISCORD_TOKEN in the .env file.')
        sys.exit(1)
    except Exception as e:
        print(f'Error: Failed to run bot: {e}')
        sys.exit(1)
