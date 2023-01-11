import disnake
from disnake.ext import commands
import config
import os
import youtube_dl

class level(commands.Cog):
    def __init__(self, bot):
    	self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print('Loaded Cog Levels')


def setup(bot):
    bot.add_cog(level(bot))