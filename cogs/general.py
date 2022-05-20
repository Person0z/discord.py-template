import disnake
from disnake.ext import commands
import os
from dotenv import load_dotenv

# Loading guild for faster registration of slash commands
load_dotenv()
guild = os.getenv('guild')

class general(commands.Cog):
    
    def __init__(self, bot):
    	self.bot = bot
        
    @commands.Cog.listener()
    async def on_ready(self):
        print(f'Loaded Cog General')
        
    # Ping Command
    @commands.slash_command(name='ping',
                           description='Find the web latency of the bot',
                           guild_ids=guild)
    async def ping(self, inter: disnake.ApplicationCommandInteraction):
        await inter.response.send_message(f"Pong! {round(self.bot.latency * 1000)}ms")
        
        
      
def setup(bot):
    bot.add_cog(general(bot))
