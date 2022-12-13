import disnake
from disnake.ext import commands
import config

class partner(commands.Cogs):
    def __init__(self, bot):
    	self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f'Loaded Cog Partner')

def setup(bot):
    bot.add_cog(partner(bot))