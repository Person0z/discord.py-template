import disnake
from disnake.ext import commands
import configlvl
from discordLevelingSystem import DiscordLevelingSystem, LevelUpAnnouncement, RoleAward

class level(commands.Cogs):
    def __init__(self, bot):
    	self.bot = bot
    
    @commands.slash_command()
    async def rank(ctx):
        data = await configlvl.lvl.get_data_for(ctx.author)
        await ctx.send(f'You are level {data.level} and your rank is {data.rank}')

    @commands.slash_command()
    async def leaderboard(ctx):
        data = await configlvl.lvl.each_member_data(ctx.guild, sort_by='rank')
        # show the leaderboard whichever way you'd like

def setup(bot):
    bot.add_cog(level(bot))