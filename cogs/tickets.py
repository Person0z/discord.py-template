import disnake
from disnake.ext import commands
import os

class tickets(commands.Cog):
    
    def __init__(self, bot):
    	self.bot = bot
        
    @commands.Cog.listener()
    async def on_ready(self):
        print(f'Loaded Cog Tickets')
        
    # Coming Soon

def setup(bot):
    bot.add_cog(tickets(bot))
