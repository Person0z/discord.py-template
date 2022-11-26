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

    #@bot.event
    #async def on_dls_level_up(member: discord.Member, message: discord.Message, data: MemberData):





def setup(bot):
    bot.add_cog(level(bot))