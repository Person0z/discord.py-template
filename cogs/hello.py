###############################################
#           Template made by Person0z         #
#          https://github.com/Person0z        #
#           Copyright© Person0z, 2022         #
#                                             #
#          This was created by Zerbaib        #
#          https://github.com/Zerbaib         #
#           Do Not Remove This Header         #
###############################################

import disnake
from disnake.ext import commands, tasks

class hello(commands.Cog):
    
    def __init__(self, bot):
    	self.bot = bot
        
    @commands.Cog.listener()
    async def on_ready(self):
        print(f'Loaded Cog General')



def setup(bot):
    bot.add_cog(hello(bot))