# Imports Don't Remove any!!
import disnake
from disnake.ext import commands
import os
import platform
import time

# Loading things from config
import config

# Prefix & Intents
bot = commands.Bot(command_prefix=config.prefix, intents=disnake.Intents.all(), case_insensitive=True)

# Automatically Update Bot from Github Repo. Requires Git
@bot.command()
async def update(ctx):
    if ctx.author.id in config.owner_ids:
        embed = diskane.Embed(title="Requires GIT. Please install if you do not have it.", description="Bot will still attempt to update. Even if you don't have GIT", color=config.Error())
        embed.set_footer(text=f'Requested by {ctx.author}', icon_url=ctx.author.avatar.url)
        await ctx.send(ephemeral=True, embed=embed)
        embed = disnake.Embed(title="Updating...", description="Updating the bot from Github...", color=disnake.Color.random())
        embed.set_footer(text=f'Requested by {ctx.author}', icon_url=ctx.author.avatar.url)
        await ctx.send(ephemeral=True, embed=embed)
        os.system("git pull")
        embed = disnake.Embed(title="Updated!", description="Updated the bot from Github!", color=disnake.Color.random())
        embed.set_footer(text=f'Requested by {ctx.author}', icon_url=ctx.author.avatar.url)
        await ctx.send(ephemeral=True, embed=embed)
        embed = disnake.Embed(title="Restarting...", description="Restarting the bot...", color=disnake.Color.random())
        embed.set_footer(text=f'Requested by {ctx.author}', icon_url=ctx.author.avatar.url)
        await ctx.send(ephemeral=True, embed=embed)
        time.sleep(2.0)
        os.system("python3 main.py")
        print("If you see python not found. Don't Worry. It will still restart. I have done it for both Linux & Windows OS")
        os.system("python main.py")
    else:
        embed = disnake.Embed(title="Error!", description="You do not have permission to use this command!", color=disnake.Color.random())
        embed.set_footer(text=f'Requested by {ctx.author}', icon_url=ctx.author.avatar.url)
        await ctx.send(embed=embed)

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
