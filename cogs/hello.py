###############################################
#           Template made by Person0z         #
#          https://github.com/Person0z        #
#           Copyright© Person0z, 2022         #
#                                             #
#          This was created by Zerbaib        #
#          https://github.com/Zerbaib         #
#           Do Not Remove This Header         #
###############################################

import disnake
from disnake.ext import commands, tasks

class hello(commands.Cog):
    
    def __init__(self, bot):
    	self.bot = bot
        
    @commands.Cog.listener()
    async def on_ready(self):
        print(f'Loaded Cog Hello')

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.content.startswith("hey"):
            await message.add_reaction("👋")

        if message.content.startswith("yo"):
            await message.add_reaction("👋")

        if message.content.startswith("hello"):
            await message.add_reaction("👋")

        if message.content.startswith("wlc"):
            await message.add_reaction("👋")

        if message.content.startswith("welcome"):
            await message.add_reaction("👋")

        if message.content.startswith("bonjour"):
            await message.add_reaction("👋")

        if message.content.startswith("salut"):
            await message.add_reaction("👋")

        if message.content.startswith("bjr"):
            await message.add_reaction("👋")

        if message.content.startswith("slt"):
            await message.add_reaction("👋")
        
        if message.content.startswith("bienvenue"):
            await message.add_reaction("👋")

def setup(bot):
    bot.add_cog(hello(bot))