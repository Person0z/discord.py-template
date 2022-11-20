###############################################
#           Template made by Person0z         #
#        Levels Command Made by ๖̶̶̶ζ͜͡Zerbaib     #
#           https://github.com/Zerbaib        #
#          https://github.com/Person0z        #
#           Copyright© Person0z, 2022         #
#           Do Not Remove This Header         #
###############################################

import disnake
from disnake.ext import commands
import os
import config

class level(commands.Cog):
    
    def __init__(self, bot):
    	self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f'Loaded Cog Levels')

def setup(bot):
    bot.add_cog(level(bot))