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
    print(f"Discord.py API version: {disnake.__version__}")
    print(f"Python version: {platform.python_version()}")
    print(f'==============================')
    
# Ping Command
@bot.slash_command(name="ping",
                   description="Returns websocket latency.",
                   guild_ids=[GUILD])
async def ping(inter):
    await inter.response.send_message('The Bots Ping is ' f"{round(bot.latency * 1000)}ms")
    
# Dog Pic
@bot.slash_command(name="Dog",
                   description="Image of a Dog!",
                   guild_ids=[GUILD])
async def dog(inter):
   async with aiohttp.ClientSession() as session:
     request = await session.get('https://some-random-api.ml/img/dog')
     dogjson = await request.json()
   embed = disnake.Embed(title="Doggo!", color=disnake.Color.purple())
   embed.set_image(url=dogjson['link'])
   await inter.response.send_message(embed=embed)
# Cat Pics
@bot.slash_command(name="Cat",
                   description="Image of a Cat!",
                   guild_ids=[GUILD])
async def cat(inter):
   async with aiohttp.ClientSession() as session:
     request = await session.get('https://some-random-api.ml/img/cat')
     catjson = await request.json()
   embed = disnake.Embed(title="Kitty!", color=disnake.Color.blue())
   embed.set_image(url=catjson['link'])
   await inter.response.send_message(embed=embed)    

# Login to Discord with the bot's token.
bot.run("YOUR TOKEN")
