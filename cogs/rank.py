###############################################
#           Template made by Person0z         #
#          https://github.com/Person0z        #
#           Copyright© Person0z, 2022         #
#           Do Not Remove This Header         #
###############################################

import json
import os
import disnake
from disnake.ext import commands
from disnake.ext.commands.cooldowns import CooldownMapping, BucketType
from helpers import errors
import config

class Rank(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.data = {}
        self.cooldowns = {}
        self.level_roles = config.level_roles

        if os.path.exists("data/levels.json"):
            with open("data/levels.json", "r") as f:
                self.data = json.load(f)

        self._cd_mapping = CooldownMapping.from_cooldown(1, 10.0, BucketType.user)

    def save_data(self):
        with open("data/levels.json", "w") as f:
            json.dump(self.data, f, indent=4)

    @commands.Cog.listener()
    async def on_ready(self):
        print('Loaded Cog rank')
        
    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.bot:
            return

        bucket = self.cooldowns.get(message.author.id)
        if bucket is None:
            bucket = self._cd_mapping.get_bucket(message)
            self.cooldowns[message.author.id] = bucket

        retry_after = bucket.update_rate_limit()
        if retry_after:
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

        xp_required = 5 * (lvl ** 2) + 10 * lvl + 10

        if xp >= xp_required:
            self.data[guild_id][user_id]["level"] = lvl + 1

            # Add role to user if they have reached a certain level
            if lvl + 1 in self.level_roles:
                role_id = self.level_roles[lvl + 1]
                role = message.guild.get_role(role_id)
                if role:
                    await message.author.add_roles(role)

        if xp >= xp_required:
            self.data[guild_id][user_id]["level"] = lvl + 1
            embed = disnake.Embed(title=f"{message.author.name} Just Leveled Up!",
                                  description=f"Congrats {message.author.mention}! You have leveled up to level {lvl + 1}!",
                                  color=config.Success())
            await message.channel.send(embed=embed, delete_after=10)
            self.save_data()
    
    @commands.slash_command()
    async def rank(self, inter: disnake.ApplicationCommandInteraction):
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

    @commands.slash_command()
    async def leaderboard(self, inter: disnake.ApplicationCommandInteraction):
        guild_id = str(inter.guild.id)
        if guild_id not in self.data:
            embed = disnake.Embed(title="Leaderboard", description="There are no users on the leaderboard yet!", color=config.Error())
            await inter.send(embed=embed)
            return
        sorted_users = sorted(self.data[guild_id].items(), key=lambda x: (x[1]["level"], x[1]["xp"]), reverse=True)
        embed = disnake.Embed(title="Leaderboard", color=config.Success())
        for i, (user_id, user_data) in enumerate(sorted_users):
            try:
                user = await self.bot.fetch_user(int(user_id))
                embed.add_field(name=f"{i+1}. {user.name}", value=f"Level: {user_data['level']} | XP: {user_data['xp']}")
            except disnake.NotFound:
                pass
            if i == 9:
                break
        await inter.send(embed=embed)

    @commands.slash_command()
    @commands.has_permissions(administrator=True)
    async def addlevel(self, inter: disnake.ApplicationCommandInteraction, user: disnake.Member, levels: int):
        guild_id = str(inter.guild.id)
        user_id = str(user.id)

        if guild_id not in self.data:
            self.data[guild_id] = {}
        if user_id not in self.data[guild_id]:
            self.data[guild_id][user_id] = {"level": 0, "xp": 0}

        self.data[guild_id][user_id]["level"] += levels
        self.save_data()

        embed = disnake.Embed(title=f"{user.name} Given Levels", description=f"{user.mention} has been given {levels} levels!", color=config.Success())
        await inter.send(embed=embed)

    @commands.slash_command()
    @commands.has_permissions(administrator=True)
    async def removelevels(self, inter: disnake.ApplicationCommandInteraction, user: disnake.Member, levels: int):
        guild_id = str(inter.guild.id)
        user_id = str(user.id)

        if guild_id not in self.data:
            embed = disnake.Embed(title="Error", description="Guild not found in database.", color=config.Error())
            await inter.send(embed=embed)
            return

        if user_id not in self.data[guild_id]:
            embed = disnake.Embed(title="Error", description="User not found in database.", color=config.Error())
            await inter.send(embed=embed)
            return

        current_lvl = self.data[guild_id][user_id]["level"]

        if current_lvl - levels < 0:
            embed = disnake.Embed(title="Error", description="Cannot remove more levels than user has.", color=config.Error())
            await inter.send(embed=embed)
            return

        self.data[guild_id][user_id]["level"] -= levels
        self.save_data()

        embed = disnake.Embed(title=f"{user.name} Lost Levels", description=f"{user.mention} has lost {levels} levels!", color=config.Success())
        await inter.send(embed=embed)

    @commands.slash_command(name="remove-xp", description="Remove XP from a member.")
    @commands.has_permissions(administrator=True)
    async def remove_xp(self, inter: disnake.ApplicationCommandInteraction, member: disnake.Member, amount: int):
        guild_id = str(inter.guild.id)
        user_id = str(member.id)

        if guild_id not in self.data or user_id not in self.data[guild_id]:
            embed = disnake.Embed(
                title=f"{member.display_name}'s Rank",
                description=f"{member.mention} hasn't started leveling yet.",
                color=config.Error(),
            )
            await inter.response.send_message(embed=embed, ephemeral=True)
            return

        current_xp = self.data[guild_id][user_id]["xp"]
        new_xp = max(0, current_xp - amount)
        xp_difference = current_xp - new_xp

        self.data[guild_id][user_id]["xp"] = new_xp
        self.save_data()

        embed = disnake.Embed(
            title=f"{member.display_name}'s XP Removed",
            description=f"Removed {xp_difference} XP from {member.mention}.",
            color=config.Success(),
        )
        await inter.response.send_message(embed=embed, ephemeral=True)

    @commands.slash_command()
    @commands.has_permissions(administrator=True)
    async def addxp(self, inter: disnake.ApplicationCommandInteraction, member: disnake.Member, amount: int):
        guild_id = str(inter.guild.id)
        user_id = str(member.id)
        if guild_id not in self.data:
            embed = disnake.Embed(title="Error", description="This guild does not have a leveling system set up yet.", color=config.Error())
            await inter.response.send_message(embed=embed, ephemeral=True)
            return
        if user_id not in self.data[guild_id]:
            embed = disnake.Embed(title="Error", description="This user does not have a level.", color=config.Error())
            await inter.response.send_message(embed=embed, ephemeral=True)
            return
        self.data[guild_id][user_id]["xp"] += amount
        self.save_data()
        embed = disnake.Embed(title="Success", description=f"Successfully added {amount} XP to {member.mention}.", color=config.Success())
        await inter.response.send_message(embed=embed, ephemeral=True)

def setup(bot):
    bot.add_cog(Rank(bot))
