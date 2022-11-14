# Imports Don't Remove any!!
import disnake
from disnake.ext import commands
import os
import platform

# Loading things from config
import config

# Prefix & Intents
bot = commands.Bot(command_prefix=config.prefix, intents=disnake.Intents.all(), case_insensitive=True)

# Automatically Update Bot from Github Repo. Requires Git
@bot.command()
async def update(ctx):
    if ctx.author.id in config.owner_ids:
        await ctx.send("Updating...")
        os.system("git pull")
        await ctx.send("Updated!")
        print("Please Restart The Bot!")
        await ctx.send("Restarting...")
        os.system("python main.py")
        os.system("python3 main.py")
        await ctx.send("Restarted!")
        print("Restarted!")
    else:
        await ctx.send("You are not allowed to use this command!")

# On Ready
@bot.event
async def on_ready():
    await bot.change_presence(activity=disnake.Activity(type=disnake.ActivityType.watching, name=config.status))
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
