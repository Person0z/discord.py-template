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

    @commands.Cog.listener()
    async def on_member_join(self, member):
        role = disnake.utils.get(member.guild.roles, name="Member")
        channel = self.bot.get_channel(config.welcome_channel)
        embed = disnake.Embed(title=f"Welcome {member.name}!", description=f"Welcome to {member.guild.name}! We hope you enjoy your stay here!", color=config.Success())
        embed.add_field (name="\nUser Info", value=f"\n**User:** ```{member.name}#{member.discriminator} ({member.id})```\n**Account Created:** ```{member.created_at.strftime('%a, %#d %B %Y, %I:%M %p UTC')}```\n**Joined Server:** ```{member.joined_at.strftime('%a, %#d %B %Y, %I:%M %p UTC')}```\n", inline=False)
        embed.set_thumbnail(url=member.avatar.url)
        embed.set_footer(text=f"{member.guild.name} | {member.guild.member_count} Members", icon_url=member.guild.icon.url)
        await channel.send(embed=embed)
        await member.add_roles(role)
        await channel.send(f"{member.mention}", delete_after=0.5)

    # a goodbye message when someone leaves the server with there porfile picture and name in the embed and a goodbye message in the chat in a custom channel
    @commands.Cog.listener()
    async def on_member_remove(self, member):
        channel = self.bot.get_channel(config.welcome_channel)
        embed = disnake.Embed(title=f"Goodbye {member.name}!", description=f"Goodbye {member.name}! We hope you enjoyed your stay here!", color=config.Error())
        embed.add_field (name="\nUser Info", value=f"\n**User:** ```{member.name}#{member.discriminator} ({member.id})```\n**Account Created:** ```{member.created_at.strftime('%a, %#d %B %Y, %I:%M %p UTC')}```\n**Joined Server:** ```{member.joined_at.strftime('%a, %#d %B %Y, %I:%M %p UTC')}```\n", inline=False)
        embed.set_thumbnail(url=member.avatar.url)
        embed.set_footer(text=f"{member.guild.name} | {member.guild.member_count} Members", icon_url=member.guild.icon.url)
        await channel.send(embed=embed)            

    # logs deleted messages from all channels in the server
    @commands.Cog.listener()
    async def on_message_delete(self, message):
        try:
            if message.author.bot:
                return
            if message.guild.id == config.guild:
                for channel in config.logs:
                    embed = disnake.Embed(title=f"Message Deleted", description=f"**Message:** {message.content}\n**Channel:** {message.channel.mention}\n**Author:** {message.author.mention}", color=config.Random)
                    await self.bot.get_channel(channel).send(embed=embed)
        except Exception as e:
            print(f'Error in on_message_delete: {e}')
    
def setup(bot):
    bot.add_cog(logging(bot))