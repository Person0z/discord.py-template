import disnake
from disnake.ext import commands

class music(commands.Cog):
    def __init__(self, bot):
    	self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f'Loaded Cog Music')

def setup(bot):
    bot.add_cog(music(bot))