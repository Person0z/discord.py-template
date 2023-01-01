###############################################
#           Template made by Person0z         #
#          https://github.com/Person0z        #
#           Copyright© Person0z, 2022         #
#           Do Not Remove This Header         #
###############################################

# imports and stuff
import disnake
from disnake.ext import commands
import os
import random
import config

class logging(commands.Cog):
    def __init__(self, bot):
    	self.bot = bot
        
    @commands.Cog.listener()
    async def on_ready(self):
        print(f'Loaded Cog Logging')


    # logs deleted messages from all channels in the server
    @commands.Cog.listener()
    async def on_message_delete(self, message):
        if message.author.bot:
            return
        if message.guild.id == config.guild:
            for channel in config.logs:
                embed = disnake.Embed(title=f"Message Deleted", description=f"**Message:** {message.content}\n**Channel:** {message.channel.mention}\n**Author:** {message.author.mention}", color=config.Random)
                await self.bot.get_channel(channel).send(embed=embed)

    
def setup(bot):
    bot.add_cog(logging(bot))