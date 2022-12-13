import disnake
from disnake.ext import commands
import config

class partner(commands.Cogs):
    def __init__(self, bot):
    	self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f'Loaded Cog Partner')
        
    @commands.slash_command(name="partner", description="Acces to partner command")
    async def partner(inter):
        await inter.send("aaa")

def setup(bot):
    bot.add_cog(partner(bot))