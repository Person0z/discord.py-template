import disnake
from disnake.ext import commands, tasks
import os
import json
import config
from config import wlcom

class welcome(commands.Cog):
    def __init__(self, bot):
    	self.bot = bot    

    @commands.Cog.listener()
    async def on_ready(self):
        print(f'Loaded Cog Welcome')

    # a welcome message when someone joins the server with there porfile picture and name in the embed and a welcome message in the chat in a custom channel
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

    @commands.slash_command(name="addwelcome", description="Add the welcome chan")
    async def addwelcome(inter):
        if not inter.author.guild_permissions.manage_channels:
            embed = disnake.Embed(title=f"You do not have permission to set welcome chan", color=config.Error())
            embed.set_footer(text=f'Attempted by {inter.author}', icon_url=inter.author.avatar.url)
            return await inter.response.send_message(ephemeral=True, embed=embed)
        
        json_data = json.dumps(wlcom)
        json_dict = json.loads(json_data)
        json_dict[f'{inter.guild.id}'] = f'{inter.channel.id}'

        embed = disnake.Embed(title=f"Successfully add channel {inter.channel} to welcome channel", color=config.Success())
        embed.set_footer(text=f'Set by {inter.author}', icon_url=inter.author.avatar.url)
        await inter.response.send_message(embed=embed)

def setup(bot):
    bot.add_cog(welcome(bot))