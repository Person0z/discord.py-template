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
import json
import random

class level(commands.Cog):
    
    def __init__(self, bot):
    	self.bot = bot
        
    @commands.Cog.listener()
    async def on_ready(self):
        print(f'Loaded Cog Level')
        
    @commands.Cog.listener()
    async def on_message(message):
        data = {000:50}
        data_dict = json.loads(data)

        if message.author.id in data_dict:
            xp = data_dict.get(message.author.id)
            xp = xp + random.randint(1, 25)
            data_dict[message.author.id] = xp
        else:
            data_dict[message.author.id] = random.randint(1, 25)


def setup(bot):
    bot.add_cog(level(bot))