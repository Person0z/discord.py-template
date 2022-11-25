import disnake
from disnake.ext import commands
import discordLevelingSysteme
import config
import configlvl

class level(commands.Cogs):
    def __init__(self, bot):
    	self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f'Loaded Cog Levels')

def setup(bot):
    bot.add_cog(level())