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
import config

class level(commands.Cog):
    
    def __init__(self, bot):
    	self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f'Loaded Cog Level')
        
    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.bot:
            return
        with open('./rank.json') as rank_file:
            data = json.load(rank_file)

        if data.get(f"{message.author.id}"):
            xp = data.get(f"{message.author.id}")
            randome = random.randint(1, 25)
            data[f"{message.author.id}"] = xp + randome
            
            with open('./rank.json', 'w') as rank_file:
                json.dump(data, rank_file)
        else:
            data[f"{message.author.id}"] = random.randint(1, 25)
            with open('./rank.json', 'w') as rank_file:
                json.dump(data, rank_file)
                
    @commands.slash_command(name="rank", description="Check your global info!")
    async def rank(self, inter):
        with open('./rank.json') as rank_file:
            data = json.load(rank_file)
        xp = data.get(f"{inter.author.id}")
        calc_lvl = xp/100
        if calc_lvl < 1:
            lvl = 0
        lvl = round(calc_lvl)
        if lvl == 0:
            stg = 0
        if 0 < lvl:
            stg = 1
        if 100 < lvl:
            stg = 2
        if 500 < lvl:
            stg = 3
        if 1500 < lvl:
            stg = 4
        if 3000 < lvl:
            stg = 5
        if 5000 < lvl:
            stg = 6
        if 10000 < lvl:
            stg = "🌟"
        embedVar = disnake.Embed(colour=config.Success())
        embedVar.add_field(name="You have", value=f"**``{xp}`` xp**", inline=False)
        embedVar.add_field(name="You are at the", value=f"**``{lvl}`` level**", inline=False)
        embedVar.add_field(name="You are at the", value=f"**``{stg}`` stage**", inline=False)
        await inter.response.send_message(embed=embedVar)

    @commands.slash_command(name="xp", description="Check your total xp!")
    async def xp(self, inter):
        with open('./rank.json') as rank_file:
            data = json.load(rank_file)
        xp = data.get(f"{inter.author.id}")
        embedVar = disnake.Embed(colour=config.Success())
        embedVar.add_field(name="You have", value=f"**``{xp}`` xp**", inline=False)
        await inter.response.send_message(embed=embedVar)

    @commands.slash_command(name="level", description="Check your level")
    async def level(self, inter):
        with open('./rank.json') as rank_file:
            data = json.load(rank_file)
        xp = data.get(f"{inter.author.id}")
        calc_lvl = xp/100
        if calc_lvl < 1:
            lvl = 0
        lvl = round(calc_lvl)
        embedVar = disnake.Embed(colour=config.Success())
        embedVar.add_field(name="You are at the", value=f"**``{lvl}`` level**", inline=False)
        await inter.response.send_message(embed=embedVar)

    @commands.slash_command(name="stage", description="Check your stage")
    async def stage(self, inter):
        with open('./rank.json') as rank_file:
            data = json.load(rank_file)
        xp = data.get(f"{inter.author.id}")
        calc_lvl = xp/100
        if calc_lvl < 1:
            lvl = 0
        lvl = round(calc_lvl)

        if lvl == 0:
            stg = 0
        if 0 < lvl:
            stg = 1
        if 100 < lvl:
            stg = 2
        if 500 < lvl:
            stg = 3
        if 1500 < lvl:
            stg = 4
        if 3000 < lvl:
            stg = 5
        if 5000 < lvl:
            stg = 6
        if 10000 < lvl:
            stg = "🌟"
        embedVar = disnake.Embed(colour=config.Success())
        embedVar.add_field(name="You are at the", value=f"**``{stg}`` stage**", inline=False)
        await inter.response.send_message(embed=embedVar)

def setup(bot):
    bot.add_cog(level(bot))