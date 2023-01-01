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
import subprocess
import platform
import time
import asyncio
import random
import sys

# Loading things from config
import config    # The config will be updated to a better version soon, 
        
# Setting up the bot
bot = commands.Bot(
    command_prefix=config.prefix,
    intents=disnake.Intents.all(),
    case_insensitive=True,
    owner_ids=config.owner_ids
)

@bot.command()
async def update(ctx):
    if ctx.author.id in config.owner_ids:
        if platform.system() == "Windows":
            try:
                embed = disnake.Embed(title="Updating... (Windows)", description="Updating the bot from the Github Repo...", color=config.Success())
                embed.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar.url)
                await ctx.send(embed=embed)
                subprocess.call('cls')
                subprocess.call("git pull", shell=True)
                subprocess.call([sys.executable, "main.py"])
                sys.exit()
            except:
                await ctx.send("Git failed to update the bot! Please try again later.")

        elif platform.system() == "Linux":
            try:
                embed = disnake.Embed(title="Updating... (Linux)", description="Updating the bot from the Github Repo...", color=config.Success())
                embed.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar.url)
                await ctx.send(embed=embed)
                subprocess.call('clear')
                subprocess.call(["git", "pull"])
                subprocess.call([sys.executable, "main.py"])
                sys.exit()
            except:
                await ctx.send("Git failed to update the bot! Please try again later.")
        else:
            embed = disnake.Embed(title="Error", description="Your OS is not supported!", color=config.Error())
            await ctx.send(embed=embed)
    else:
        embed = disnake.Embed(title="Error", description="You are not allowed to use this command!", color=config.Error())
        await ctx.send(embed=embed)

# On Ready
@bot.event
async def on_ready():
    print('###############################################')
    print('#           Template made by Person0z         #')
    print('#          https://github.com/Person0z        #')
    print('#           Copyright© Person0z, 2022         #') 
    print("#                                             #")
    print('#           Join Discord For Support!         #')
    print('#         https://discord.gg/5dEadru9mU       #')
    print("#                                             #")
    print('#           Do Not Remove This Header         #')
    print('###############################################')
    print('')
    print('')
    print('===============================================')
    print("The bot is ready!")
    print(f'Logged in as {bot.user.name}#{bot.user.discriminator} | {bot.user.id}')
    print(f"I am on {len(bot.guilds)} server")
    print(f'Running on {platform.system()} {platform.release()} ({os.name})')
    print(f"Disnake version : {disnake.__version__}")
    print(f"Python version: {platform.python_version()}")
    print('===============================================')
    print('')
    print('')
    print('================== Loaded Cogs ================')
    status_task.start()
    await asyncio.sleep(0.01)
    print('===============================================')

# Status Task
@tasks.loop(minutes=0.15)
async def status_task():
    await bot.change_presence(activity=disnake.Game(random.choice(config.activity)))

# Load Cogs On Start
for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        bot.load_extension(f'cogs.{filename[:-3]}')

# Run The Bot 
bot.run(config.token, reconnect=True)


