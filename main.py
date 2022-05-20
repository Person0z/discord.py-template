# Imports Don't Remove any!!
import disnake
from disnake.ext import commands
import os
from dotenv import load_dotenv
import platform

# Loading things from .env
load_dotenv()
token = os.getenv('token')
guild = os.getenv('guild')

# Prefix & Intents
bot = commands.Bot(command_prefix=".", intents=disnake.Intents.all(), case_insensitive=True)

# On Ready
@bot.event
async def on_ready():
    print('')
    print(f'======================================')
    print(f"The bot is ready!")
    print(f"Logged in as {bot.user.name}")
    print(f"Python version: {platform.python_version()}")
    print('Discord Bot Template Made By Person0z')
    print(f'======================================')    
    print('')
    
# Load Cogs
@bot.command()
async def load(inter, extension):
    bot.load_extension(f'cogs.{extension}')
    
# Unload
@bot.command()
async def unload(inter, extension):
    bot.unload_extension(f'cogs.{extension}')

# Load Cogs On Start
for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        bot.load_extension(f'cogs.{filename[:-3]}')   

# Login to Discord with the bot's token.
bot.run(token)
