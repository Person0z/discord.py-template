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
from helpers import errors
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
        
        # in the future dev the give role with lvl
                
    @commands.slash_command(name="rank", description="Check your global info!")
    async def rank(self, inter):
        try:
            with open('./rank.json') as rank_file:
                data = json.load(rank_file)
            xp = data.get(f"{inter.author.id}")
            calc_lvl = xp/100
            if calc_lvl < 1:
                lvl = 0
            lvl = round(calc_lvl)
            stages = [0, 1, 2, 3, 4, 5, 6, "🌟"]
            stg = stages[min(7, sum(lvl >= i for i in [0, 100, 500, 1500, 3000, 5000, 10000]))]
            embedVar = disnake.Embed(colour=config.Success())
            embedVar.add_field(name="You have", value=f"**``{xp}`` xp**", inline=False)
            embedVar.add_field(name="You are at the", value=f"**``{lvl}`` level**", inline=False)
            embedVar.add_field(name="You are at the", value=f"**``{stg}`` stage**", inline=False)
            await inter.response.send_message(embed=embedVar)
        except Exception as e:
            print(f'Error sending rank message: {e}')
            await inter.send(embed=errors.create_error_embed(f"Error sending rank command: {e}"))

    @commands.slash_command(name="top", description="Check the top of xp in all time!")
    async def top(self, inter, top: int):
        try:
            with open('./rank.json') as rank_file:
                data = json.load(rank_file)
        
            sorted_data = sorted(data.items(), key=lambda x: x[1], reverse=True)
            short_top = sorted_data[:top]

            embedVar = disnake.Embed(title=f"Top {top} of the member xp", colour=config.Success())
            for key, value in short_top:
                user = self.bot.get_user(int(key))
                if user:
                    embedVar.add_field(name=f"{user.name}", value=f"```With {value} xp```", inline=False)
                else:
                    embedVar.add_field(name=f"Not Fund", value=f" ", inline=False)
            await inter.response.send_message(embed=embedVar)
        except Exception as e:
            print(f'Error sending top message: {e}')
            await inter.send(embed=errors.create_error_embed(f"Error sending top command: {e}"))

    @commands.slash_command(name="xp", description="Check your total xp!")
    async def xp(self, inter):
        try:
            with open('./rank.json') as rank_file:
                data = json.load(rank_file)
            xp = data.get(f"{inter.author.id}")
            embedVar = disnake.Embed(colour=config.Success())
            embedVar.add_field(name="You have", value=f"**``{xp}`` xp**", inline=False)
            await inter.response.send_message(embed=embedVar)
        except Exception as e:
            print(f'Error sending xp message: {e}')
            await inter.send(embed=errors.create_error_embed(f"Error sending xp command: {e}"))

    @commands.slash_command(name="givexp", description="Give xp to a member!")
    @commands.default_member_permissions(administrator=True)
    async def givexp(self, inter, member: disnake.Member, amount: int):
        try:
            with open('./rank.json') as rank_file:
                data = json.load(rank_file)

            if data.get(f"{member.id}"):
                xp = data.get(f"{member.id}")
                data[f"{member.id}"] = xp + amount
                
                with open('./rank.json', 'w') as rank_file:
                    json.dump(data, rank_file)
                
            else:
                data[f"{member.id}"] = amount
                with open('./rank.json', 'w') as rank_file:
                    json.dump(data, rank_file)
            embedVar = disnake.Embed(colour=config.Success())
            embedVar.add_field(name="You have give", value=f"**``{amount}`` xp to  {member}**", inline=False)
            await inter.response.send_message(embed=embedVar)
        except Exception as e:
            print(f'Error sending givexp message: {e}')
            await inter.send(embed=errors.create_error_embed(f"Error sending givexp command: {e}"))

    @commands.slash_command(name="level", description="Check your level")
    async def level(self, inter):
        try:
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
        except Exception as e:
            print(f'Error sending level message: {e}')
            await inter.send(embed=errors.create_error_embed(f"Error sending level command: {e}"))

    @commands.slash_command(name="stage", description="Check your stage")
    async def stage(self, inter):
        try:
            with open('./rank.json') as rank_file:
                data = json.load(rank_file)
            xp = data.get(f"{inter.author.id}")
            calc_lvl = xp/100
            if calc_lvl < 1:
                lvl = 0
            lvl = round(calc_lvl)

            stages = [0, 1, 2, 3, 4, 5, 6, "🌟"]
            stg = stages[min(7, sum(lvl >= i for i in [0, 100, 500, 1500, 3000, 5000, 10000]))]
            embedVar = disnake.Embed(colour=config.Success())
            embedVar.add_field(name="You are at the", value=f"**``{stg}`` stage**", inline=False)
            await inter.response.send_message(embed=embedVar)
        except Exception as e:
            print(f'Error sending stage message: {e}')
            await inter.send(embed=errors.create_error_embed(f"Error sending stage command: {e}"))

def setup(bot):
    bot.add_cog(level(bot))