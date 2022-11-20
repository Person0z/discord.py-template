###############################################
#           Template made by Person0z         #
#          https://github.com/Person0z        #
#           Copyright© Person0z, 2022         #
#           Do Not Remove This Header         #
###############################################

# Imports Don't Remove any!!
import disnake
from disnake.ext import commands, tasks
import os
import platform
import time
import asyncio
import random
import sys

# Loading things from config
import config # The config will be updated to a better version soon, 
                # but for now it will work fine.
        
# Setting up the bot
bot = commands.Bot(
    command_prefix=config.prefix,
    intents=disnake.Intents.all(),
    case_insensitive=True,
    owner_ids=config.owner_ids,
    activity=disnake.Activity(
        type=disnake.ActivityType.watching,
        name=config.activity
    )
)

# Automatically Update Bot from Github Repo. Requires Git
@bot.command()
async def update(ctx):
    if ctx.author.id in config.owner_ids:
        embed = disnake.Embed(title="Requires GIT. Please install if you do not have it.", description="Bot will still attempt to update. Even if you don't have GIT", color=config.Error())
        embed.set_footer(text=f'Requested by {ctx.author}', icon_url=ctx.author.avatar.url)
        await ctx.send(embed=embed)
        embed = disnake.Embed(title="Updating...", description="Updating the bot from Github...", color=disnake.Color.random())
        embed.set_footer(text=f'Requested by {ctx.author}', icon_url=ctx.author.avatar.url)
        await ctx.send(embed=embed)
        os.system("git pull")
        embed = disnake.Embed(title="Restarting...", description=f'Restarting the bot... If the bot crashes then please check if config needs to be updated or if you need to install a pip module. Report any bugs on the GitHub Located [Here](https://github.com/Person0z/discord.py-template/)', color=disnake.Color.random())
        embed.set_footer(text=f'Requested by {ctx.author}', icon_url=ctx.author.avatar.url)
        await ctx.send(embed=embed)
        print("If you see python not found. Don't Worry. It will still restart. I have done it for both Linux & Windows OS")
        time.sleep(3.0)
        os.system("python3 main.py")
        os.system("python main.py")
    else:
        embed = disnake.Embed(title="Error!", description="You do not have permission to use this command!", color=disnake.Color.random())
        embed.set_footer(text=f'Requested by {ctx.author}', icon_url=ctx.author.avatar.url)
        await ctx.send(embed=embed)

# On Ready
@bot.event
async def on_ready():
    print('###############################################')
    print('#           Template made by Person0z         #')
    print('#          https://github.com/Person0z        #')
    print('#           Copyright© Person0z, 2022         #')
    print('#           Do Not Remove This Header         #')
    print('###############################################')
    print('')
    print('')
    print('===============================================')
    print("The bot is ready!")
    print(f'Logged in as {bot.user.name}#{bot.user.discriminator} | {bot.user.id}')
    print(f'Running on {platform.system()} {platform.release()} ({os.name})')
    print(f"Disnake version : {disnake.__version__}")
    print(f"Python version: {platform.python_version()}")
    print('===============================================')
    print('')
    print('')
    print('================== Loaded Cogs ================')
    await bot.wait_until_ready()
    status_task.start()
    await asyncio.sleep(0.01)
    print('===============================================')

@tasks.loop(minutes=0.1)
async def status_task():
    statuses = ["/help", "V.1.5", "V2 en dev ^^", "je soutiens: oz-projects.fr/", "je soutiens: eclazion.net", "tous pour Discord.py", "Dev by: Zerbaib", "prefix: /"]
    await bot.change_presence(activity=disnake.Game(random.choice(statuses)))

# Load Cogs On Start
for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        bot.load_extension(f'cogs.{filename[:-3]}')   

# Login to Discord with the bot's token.
bot.run(config.token)
