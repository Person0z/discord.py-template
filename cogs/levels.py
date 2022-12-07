import disnake
from disnake.ext import commands
from discordLevelingSystem import DiscordLevelingSystem, LevelUpAnnouncement, RoleAward
import config
import configlvl

class level(commands.Cog):
    def __init__(self, bot):
    	self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f'Loaded Cog Levels')

    @commands.slash_command()
    async def rank(ctx):
        data = await configlvl.lvl.get_data_for(ctx.author)
        await ctx.send(f"You are level {data.level} you have {data.xp} xp\n and your rank is {data.rank}")

    @commands.slash_command()
    async def leaderboard(ctx):
        # data = await configlvl.lvl.each_member_data(ctx.guild, sort_by='rank') # fetch data doesnt work
        await ctx.send("aaa")


def setup(bot):
    bot.add_cog(level(bot))