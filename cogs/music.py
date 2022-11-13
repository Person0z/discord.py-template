import disnake
from disnake.ext import commands
import os
import time
import config

class Music(commands.Cog):
    
    def __init__(self, bot):
    	self.bot = bot
        
    @commands.Cog.listener()
    async def on_ready(self):
        print(f'Loaded Cog Music') 

    # Coming Soon


def setup(bot):
    bot.add_cog(Music(bot))