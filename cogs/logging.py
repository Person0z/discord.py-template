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
from datetime import datetime
import random
import config
from helpers import errors

class logging(commands.Cog):
    def __init__(self, bot):
    	self.bot = bot
        
    @commands.Cog.listener()
    async def on_ready(self):
        print(f'Loaded Cog Logging')
            
    # Message deleted, logs messages and pulls
    @commands.Cog.listener()
    async def on_message_delete(self, message):
        try:
            channel = self.bot.get_channel(1054579107666591804)
            embed = disnake.Embed(
                title="Message Deleted",
                description=f"Message sent by **{message.author.mention}** in **{message.channel.mention}** was deleted.",
                color=disnake.Color.red()
            )
            embed.add_field(name="Message:", value=f'```{message.content}```')
            embed.set_footer(text=f"Message ID: {message.id}")
            await channel.send(embed=embed)
        except Exception as e:
            print(f'Error sending logging message: {e}')
            
    
def setup(bot):
    bot.add_cog(logging(bot))