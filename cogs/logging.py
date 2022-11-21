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

    # logs dleted messages to a channel and logs any messsages
    @commands.Cog.listener()
    async def on_message_delete(self, message):
        if message.channel.id in config.logs:
            embed = disnake.Embed(title=f"Message Deleted", description=f"Message sent by {message.author.mention} in {message.channel.mention} was deleted", color=config.Error())
            embed.add_field(name="Message", value=message.content, inline=False)
            embed.set_footer(text=f"Message ID: {message.id}")
            channel = self.bot.get_channel(config.logs[0])
            await channel.send(embed=embed)

    # logs edited messages to a channel and logs any messsages
    @commands.Cog.listener()
    async def on_message_edit(self, before, after):
        if before.channel.id in config.logs:
            embed = disnake.Embed(title=f"Message Edited", description=f"Message sent by {before.author.mention} in {before.channel.mention} was edited", color=config.Error())
            embed.add_field(name="Before", value=before.content, inline=False)
            embed.add_field(name="After", value=after.content, inline=False)
            embed.set_footer(text=f"Message ID: {before.id}")
            channel = self.bot.get_channel(config.logs[0])
            await channel.send(embed=embed)

def setup(bot):
    bot.add_cog(logging(bot))