import disnake
from disnake.ext import commands
import os
import platform
import aiohttp

# Your Discord Servers ID
GUILD = 945077306374901773

bot = commands.Bot()

# On Ready
@bot.event
async def on_ready():
    print(f'==============================')
    print(f"The bot is ready!")
    print(f"Logged in as {bot.user.name}")
    print(f"Python version: {platform.python_version()}")
    print(f'==============================')

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
bot.run("BOT TOKEN")