# Imports Don't Remove any!!
import disnake
from disnake.ext import commands
import os
import platform

# Loading things from config
import config

# Prefix & Intents
bot = commands.Bot(command_prefix=config.prefix, intents=disnake.Intents.all(), case_insensitive=True)

# On Ready
@bot.event
async def on_ready():
    await bot.change_presence(activity=disnake.Activity(type=disnake.ActivityType.watching, name="Person0z's Server!"))
    print('')
    print('======================================')
    print("The bot is ready!")
    print(f"Logged in as {bot.user.name}")
    print(f"Disnake version: {disnake.__version__}")
    print(f"Python version: {platform.python_version()}")
    print('Discord Bot Template Made By Person0z')
    print('======================================')    
    print('')
    

# Load Cogs
#@bot.slash_command()
#async def load(ctx, extension):
#    bot.load_extension(f'cogs.{extension}')
    
# Unload
#@bot.slash_command()
#async def unload(ctx, extension):
#    bot.unload_extension(f'cogs.{extension}')

# Load Cogs On Start
for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        bot.load_extension(f'cogs.{filename[:-3]}')   

# Login to Discord with the bot's token.
bot.run(config.token)
