###############################################
#           Template made by Person0z         #
#          https://github.com/Person0z        #
#           Copyright© Person0z, 2022         #
#           Do Not Remove This Header         #
###############################################

# importing the required modules
import disnake
from disnake.ext import commands
import os
import time
import config

class moderation(commands.Cog):
    
    def __init__(self, bot):
        self.bot = bot
        
    @commands.Cog.listener()
    async def on_ready(self):
        print(f'Loaded Cog Moderation') 

    # Slowmode Command
    @commands.slash_command(name='slowmode',
                            description='Set the slowmode of a channel',)
    async def slowmode(self, inter: disnake.ApplicationCommandInteraction, seconds: int, channel: disnake.TextChannel = None):

        if not inter.author.guild_permissions.manage_channels:
            embed = disnake.Embed(title=f"You do not have permission to set slowmode!", color=config.Error())
            embed.set_footer(text=f'Attempted by {inter.author}', icon_url=inter.author.avatar.url)
            return await inter.response.send_message(ephemeral=True, embed=embed) 

        if not inter.guild.me.guild_permissions.manage_channels:
            embed = disnake.Embed(title=f"I do not have permission to set slowmode!", color=config.Error())
            embed.set_footer(text=f'Attempted by {inter.author}', icon_url=inter.author.avatar.url)
            return await inter.response.send_message(delete_after=15, embed=embed) 
        if not channel:
            channel = inter.channel
        await channel.edit(slowmode_delay=seconds)
        embed = disnake.Embed(title=f"Successfully set slowmode to {seconds} seconds!", color=config.Success())
        embed.set_footer(text=f'Set by {inter.author}', icon_url=inter.author.avatar.url)
        await inter.response.send_message(embed=embed)        

    # Lock Command
    @commands.slash_command(name='lock',
                            description='Lock a channel',)
    async def lock(self, inter: disnake.ApplicationCommandInteraction, channel: disnake.TextChannel = None):
        if not inter.author.guild_permissions.manage_channels:
            embed = disnake.Embed(title=f"You do not have permission to lock ``{channel}!``", color=config.Error())
            embed.set_footer(text=f'Attempted by {inter.author}', icon_url=inter.author.avatar.url)
            return await inter.response.send_message(ephemeral=True, embed=embed)            
        if not inter.guild.me.guild_permissions.manage_channels:
            embed = disnake.Embed(title=f"I do not have permission to lock ``{channel}!``", color=config.Error())
            embed.set_footer(text=f'Attempted by {inter.author}', icon_url=inter.author.avatar.url)
            return await inter.response.send_message(delete_after=15, embed=embed)
        if not channel:
            channel = inter.channel
        await channel.set_permissions(inter.guild.default_role, send_messages=False)
        embed = disnake.Embed(title=f"Successfully locked ``{channel}!``", color=config.Success())
        embed.set_footer(text=f'Locked by {inter.author}', icon_url=inter.author.avatar.url)
        await inter.response.send_message(embed=embed)

    # Unlock Command
    @commands.slash_command(name='unlock',
                            description='Unlock a channel',)
    async def unlock(self, inter: disnake.ApplicationCommandInteraction, channel: disnake.TextChannel = None):
        if not inter.author.guild_permissions.manage_channels:
            embed = disnake.Embed(title=f"You do not have permission to unlock ``{channel}!``", color=config.Error())
            embed.set_footer(text=f'Attempted by {inter.author}', icon_url=inter.author.avatar.url)
            return await inter.response.send_message(ephemeral=True, embed=embed)   
        if not inter.guild.me.guild_permissions.manage_channels:
            embed = disnake.Embed(title=f"I do not have permission to unlock ``{channel}!``", color=config.Error())
            embed.set_footer(text=f'Attempted by {inter.author}', icon_url=inter.author.avatar.url)
            return await inter.response.send_message(delete_after=15, embed=embed)
        if not channel:
            channel = inter.channel
        await channel.set_permissions(inter.guild.default_role, send_messages=True)
        embed = disnake.Embed(title=f"Successfully Unlocked ``{channel}!``", color=config.Success())
        embed.set_footer(text=f'Locked by {inter.author}', icon_url=inter.author.avatar.url)
        await inter.response.send_message(embed=embed)

    # Purge Command
    @commands.slash_command(name='purge',
                            description='Purge messages from a channel',)
    async def purge(self, inter: disnake.ApplicationCommandInteraction, amount: int, channel: disnake.TextChannel = None):
        if not inter.author.guild_permissions.manage_messages:
            embed = disnake.Embed(title=f"You do not have permission To purge messages!", color=config.Error())
            embed.set_footer(text=f'Attempted by {inter.author}', icon_url=inter.author.avatar.url)
            return await inter.response.send_message(ephemeral=True, embed=embed)   
        if not inter.guild.me.guild_permissions.manage_messages:
            embed = disnake.Embed(title=f"I do not have permission to purge messages!", color=config.Error())
            embed.set_footer(text=f'Attempted by {inter.author}', icon_url=inter.author.avatar.url)
            return await inter.response.send_message(delete_after=15, embed=embed)
        if not channel:
            channel = inter.channel
        await channel.purge(limit=amount)
        embed = disnake.Embed(title=f"Successfully Purged ``{amount}`` Messages!", color=config.Success())
        embed.set_footer(text=f'Purged by {inter.author}', icon_url=inter.author.avatar.url)
        await inter.response.send_message(embed=embed)

    # kick command 
    @commands.slash_command(name='kick',
                            description='Kick a member',)
    async def kick(self, inter: disnake.ApplicationCommandInteraction, member: disnake.Member, *, reason: str = "No reason provided"):
        if not inter.author.guild_permissions.kick_members:
            embed = disnake.Embed(title=f"You do not have permission to kick ``{member}!``", color=config.Error())
            embed.set_footer(text=f'Attempted by {inter.author}', icon_url=inter.author.avatar.url)
            return await inter.response.send_message(ephemeral=True, embed=embed)   
        if not inter.guild.me.guild_permissions.kick_members:
            embed = disnake.Embed(title=f"I do not have permission to kick ``{member}!``", color=config.Error())
            embed.set_footer(text=f'Attempted by {inter.author}', icon_url=inter.author.avatar.url)
            return await inter.response.send_message(delete_after=15, embed=embed)
        embed = disnake.Embed(title=f"You Have Been Kicked from **{member.guild.name}**!", color=config.Success())
        embed.add_field(name="Reason:", value=f"``{reason}``", inline=False)
        embed.set_footer(text=f'Kicked by {inter.author}', icon_url=inter.author.avatar.url)
        await member.send(embed=embed)
        await member.kick(reason=reason)
        embed = disnake.Embed(title=f"Successfully Kicked ``{member}`` for ``{reason}``", color=config.Success())
        embed.set_footer(text=f'Kicked by {inter.author}', icon_url=inter.author.avatar.url)
        await inter.response.send_message(embed=embed)

    # ban command 
    @commands.slash_command(name='ban',
                            description='Ban a member',)
    async def ban(self, inter: disnake.ApplicationCommandInteraction, member: disnake.Member, *, reason: str = "No reason provided"):
        if not inter.author.guild_permissions.ban_members:
            embed = disnake.Embed(title=f"You do not have permission to ban ``{member}!``", color=config.Error())
            embed.set_footer(text=f'Attempted by {inter.author}', icon_url=inter.author.avatar.url)
            return await inter.response.send_message(ephemeral=True, embed=embed)   
        if not inter.guild.me.guild_permissions.ban_members:
            embed = disnake.Embed(title=f"I do not have permission to ban ``{member}!``", color=config.Error())
            embed.set_footer(text=f'Attempted by {inter.author}', icon_url=inter.author.avatar.url)
            return await inter.response.send_message(delete_after=15, embed=embed)
        embed = disnake.Embed(title=f"You Have Been Banned from **{member.guild.name}**!", color=config.Success())
        embed.add_field(name="Reason:", value=f"``{reason}``", inline=False)
        embed.set_footer(text=f'Banned by {inter.author}', icon_url=inter.author.avatar.url)
        await member.send(embed=embed)
        await member.ban(reason=reason)
        embed = disnake.Embed(title=f"Successfully Banned ``{member}`` for ``{reason}``", color=config.Success())
        embed.set_footer(text=f'Banned by {inter.author}', icon_url=inter.author.avatar.url)
        await inter.response.send_message(embed=embed)

    # unban command 
    @commands.slash_command(name='unban',
                            description='Unban a member',)
    async def unban(self, inter: disnake.ApplicationCommandInteraction, member: disnake.User):
        if not inter.author.guild_permissions.ban_members:
            embed = disnake.Embed(title=f"You do not have permission to unban ``{member}!``", color=config.Error())
            embed.set_footer(text=f'Attempted by {inter.author}', icon_url=inter.author.avatar.url)
            return await inter.response.send_message(ephemeral=True, embed=embed)   
        if not inter.guild.me.guild_permissions.ban_members:
            embed = disnake.Embed(title=f"I do not have permission to unban ``{member}!``", color=config.Error())
            embed.set_footer(text=f'Attempted by {inter.author}', icon_url=inter.author.avatar.url)
            return await inter.response.send_message(delete_after=15, embed=embed)
        await inter.guild.unban(member)
        embed = disnake.Embed(title=f"Successfully Unbanned ``{member}``", color=config.Success())
        embed.set_footer(text=f'Unbanned by {inter.author}', icon_url=inter.author.avatar.url)
        await inter.response.send_message(embed=embed)

    # Nuke command that nukes channels 
    @commands.slash_command(name='nuke',
                            description='Nuke a channel',)
    async def nuke(self, inter: disnake.ApplicationCommandInteraction, channel: disnake.TextChannel = None):
        if not inter.author.guild_permissions.manage_channels:
            embed = disnake.Embed(title=f"You do not have permission to nuke ``{channel}!``", color=config.Error())
            embed.set_footer(text=f'Attempted by {inter.author}', icon_url=inter.author.avatar.url)
            return await inter.response.send_message(ephemeral=True, embed=embed)   
        if not inter.guild.me.guild_permissions.manage_channels:
            embed = disnake.Embed(title=f"I do not have permission to nuke ``{channel}!``", color=config.Error())
            embed.set_footer(text=f'Attempted by {inter.author}', icon_url=inter.author.avatar.url)
            return await inter.response.send_message(delete_after=15, embed=embed)
        if channel is None:
            channel = inter.channel
        position = channel.position
        new_channel = await channel.clone(reason=None)
        await channel.delete()
        await new_channel.edit(position=position)
        embed = disnake.Embed(title=f"Successfully Nuked ``{channel}``", color=config.Success())
        embed.set_footer(text=f'Nuked by {inter.author}', icon_url=inter.author.avatar.url)
        await inter.response.send_message(embed=embed)

def setup(bot):
    bot.add_cog(moderation(bot))
