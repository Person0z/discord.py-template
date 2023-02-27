import json
import os
import disnake
from disnake.ext import commands
from helpers import errors
import config

class Rank(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.data = {}

        if os.path.exists("data/levels.json"):
            with open("data/levels.json", "r") as f:
                self.data = json.load(f)

    def save_data(self):
        with open("data/levels.json", "w") as f:
            json.dump(self.data, f, indent=4)

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.bot:
            return

        guild_id = str(message.guild.id)
        user_id = str(message.author.id)

        if guild_id not in self.data:
            self.data[guild_id] = {}
            self.save_data()
            
        if user_id not in self.data[guild_id]:
            self.data[guild_id][user_id] = {"level": 0, "xp": 0}
            self.save_data()

        self.data[guild_id][user_id]["xp"] += 1
        self.save_data()

        xp = self.data[guild_id][user_id]["xp"]
        lvl = self.data[guild_id][user_id]["level"]

        xp_required = 5 * (lvl**2) + 10 * lvl + 10
        
        if xp >= xp_required:
            self.data[guild_id][user_id]["level"] = lvl + 1
            embed = disnake.Embed(title=f"{message.author.name} Just Leveled Up!", description=f"Congrats {message.author.mention}! You have leveled up to level {lvl + 1}!", color=config.Success())
            await message.channel.send(embed=embed, delete_after=10)
            self.save_data()
    
    @commands.slash_command()
    async def rank(self, inter: disnake.ApplicationCommandInteraction,):
        guild_id = str(inter.guild.id)
        user_id = str(inter.author.id)
        if guild_id not in self.data:
            embed = disnake.Embed(title=f"{inter.author.name}'s Rank", description="You haven't started leveling yet. Send your first message(s) to get your levels up!", color=config.Error())
            await inter.send(embed=embed)
        elif user_id not in self.data[guild_id]:
            embed = disnake.Embed(title=f"{inter.author.name}'s Rank", description="You haven't started leveling yet. Send your first message(s) to get your levels up!", color=config.Error())
            await inter.send(embed=embed)
        else:
            current_xp = self.data[guild_id][user_id]["xp"]
            current_lvl = self.data[guild_id][user_id]["level"]
            xp_required = 5 * (current_lvl**2) + 10 * current_lvl + 10
            remaining_xp = xp_required - current_xp
            embed = disnake.Embed(title=f"{inter.author.name}'s Rank", description=f"Level: {current_lvl} | XP: {current_xp}/{xp_required} You need {remaining_xp} XP to level up!", color=config.Success())
            await inter.send(embed=embed)
                    

def setup(bot):
    bot.add_cog(Rank(bot))
