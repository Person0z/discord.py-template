import disnake
from disnake.ext import commands
import configlvl
import config
from discordLevelingSystem import DiscordLevelingSystem, LevelUpAnnouncement, RoleAward

class level(commands.Cog):
    def __init__(self, bot):
    	self.bot = bot
    
    @commands.Cog.listener()
    async def on_ready(self):
        print(f'Loaded Cog Level')

    @commands.slash_command(name='rank', description='A rank command to see your level')
    async def rank(ctx):
        data = await configlvl.lvl.get_data_for(ctx.author)
        await ctx.send(f'You are level {data.level} and your rank is {data.rank}')

    @commands.slash_command(name='leaderboard', description='A command to see the top of rank')
    async def leaderboard(ctx):
        data = await configlvl.lvl.each_member_data(ctx.guild, sort_by='rank')
        # show the leaderboard whichever way you'd like

def setup(bot):
    bot.add_cog(level(bot))