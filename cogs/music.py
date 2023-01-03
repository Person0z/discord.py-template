import disnake
from disnake.ext import commands

class music(commands.Cog):
    def __init__(self, bot):
    	self.bot = bot

def setup(bot):
    bot.add_cog(music(bot))