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
        with open('./rank.json') as rank_file:
            data = json.load(rank_file)

        if message.author.id in data:
            xp = data.get(message.author.id)
            xp = xp + random.randint(1, 25)
            data[f"{message.author.id}"] = xp
            with open('./rank.json', 'w') as rank_file:
                data = json.load(rank_file)
        else:
            data[f"{message.author.id}"] = random.randint(1, 25)
            with open('./rank.json', 'w') as rank_file:
                data = json.load(rank_file)
    
    @commands.slash_command(name="rank", description="Check your rank !")
    async def rank(inter):
        with open('./rank.json') as rank_file:
            data = json.load(rank_file)
        get_data = json.loads(data)
        xp = get_data.get()
        await inter.send(f"your xp is {xp}")



def setup(bot):
    bot.add_cog(level(bot))