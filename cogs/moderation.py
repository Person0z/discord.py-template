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
import json
from helpers import errors

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
        try:

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
        except Exception as e:
            print(f'Error sending slow command: {e}')
            await inter.send(embed=errors.create_error_embed(f"Error sending slowmode command: {e}"))

    # Lock Command
    @commands.slash_command(name='lock',
                            description='Lock a channel',)
    async def lock(self, inter: disnake.ApplicationCommandInteraction, channel: disnake.TextChannel = None):
        try:
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
        except Exception as e:
            print(f'Error sending lock command: {e}')
            await inter.send(embed=errors.create_error_embed(f"Error sending lock command: {e}"))

    # Unlock Command
    @commands.slash_command(name='unlock',
                            description='Unlock a channel',)
    async def unlock(self, inter: disnake.ApplicationCommandInteraction, channel: disnake.TextChannel = None):
        try:
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
        except Exception as e:
            print(f'Error sending unlock command: {e}')
            await inter.send(embed=errors.create_error_embed(f"Error sending unlock command: {e}"))

    # Purge Command
    @commands.slash_command(name='purge',
                            description='Purge a channel',)
    async def purge(self, inter: disnake.ApplicationCommandInteraction, amount: int, channel: disnake.TextChannel = None):
        try:
            if not inter.author.guild_permissions.manage_messages:
                embed = disnake.Embed(title=f"You do not have permission to purge ``{channel}!``", color=config.Error())
                embed.set_footer(text=f'Attempted by {inter.author}', icon_url=inter.author.avatar.url)
                return await inter.response.send_message(ephemeral=True, embed=embed)   
            if not inter.guild.me.guild_permissions.manage_messages:
                embed = disnake.Embed(title=f"I do not have permission to purge ``{channel}!``", color=config.Error())
                embed.set_footer(text=f'Attempted by {inter.author}', icon_url=inter.author.avatar.url)
                return await inter.response.send_message(delete_after=15, embed=embed)
            if not channel:
                channel = inter.channel
            await channel.purge(limit=amount)
            embed = disnake.Embed(title=f"Successfully purged ``{amount}`` messages in ``{channel}!``", color=config.Success())
            embed.set_footer(text=f'Purged by {inter.author}', icon_url=inter.author.avatar.url)
            await inter.response.send_message(embed=embed)
        except Exception as e:
            print(f'Error sending purge command: {e}')
            await inter.send(embed=errors.create_error_embed(f"Error sending purge command: {e}"))

    # kick command
    @commands.slash_command(name='kick',
                            description='Kick a member',)
    async def kick(self, inter: disnake.ApplicationCommandInteraction, member: disnake.Member, *, reason: str = None):
        try:
            if not inter.author.guild_permissions.kick_members:
                embed = disnake.Embed(title=f"You do not have permission to kick ``{member}``!", color=config.Error())
                embed.set_footer(text=f'Attempted by {inter.author}', icon_url=inter.author.avatar.url)
                return await inter.response.send_message(ephemeral=True, embed=embed)   
            if not inter.guild.me.guild_permissions.kick_members:
                embed = disnake.Embed(title=f"I do not have permission to kick ``{member}``!", color=config.Error())
                embed.set_footer(text=f'Attempted by {inter.author}', icon_url=inter.author.avatar.url)
                return await inter.response.send_message(delete_after=15, embed=embed)
            if member.top_role >= inter.author.top_role:
                embed = disnake.Embed(title=f"You cannot kick ``{member}`` because they have a higher role than you!", color=config.Error())
                embed.set_footer(text=f'Attempted by {inter.author}', icon_url=inter.author.avatar.url)
                return await inter.response.send_message(ephemeral=True, embed=embed)
            if member.top_role >= inter.guild.me.top_role:
                embed = disnake.Embed(title=f"I cannot kick ``{member}`` because they have a higher role than me!", color=config.Error())
                embed.set_footer(text=f'Attempted by {inter.author}', icon_url=inter.author.avatar.url)
                return await inter.response.send_message(ephemeral=True, embed=embed)
            if reason is None:
                reason = "No reason provided"
            await member.kick(reason=reason)
            embed = disnake.Embed(title=f"Successfully Kicked ``{member}``!", color=config.Success())
            embed.set_footer(text=f'Kicked by {inter.author}', icon_url=inter.author.avatar.url)
            await inter.response.send_message(embed=embed)
        except Exception as e:
            print(f'Error sending kick command: {e}')
            await inter.send(embed=errors.create_error_embed(f"Error sending kick command: {e}"))

    # ban command
    @commands.slash_command(name='ban',
                            description='Ban a member',)
    async def ban(self, inter: disnake.ApplicationCommandInteraction, member: disnake.Member, *, reason: str = "No reason provided"):
        try:
            if not inter.author.guild_permissions.ban_members:
                embed = disnake.Embed(title=f"You do not have permission to ban ``{member}!``", color=config.Error())
                embed.set_footer(text=f'Attempted by {inter.author}', icon_url=inter.author.avatar.url)
                return await inter.response.send_message(ephemeral=True, embed=embed)   
            if not inter.guild.me.guild_permissions.ban_members:
                embed = disnake.Embed(title=f"I do not have permission to ban ``{member}!``", color=config.Error())
                embed.set_footer(text=f'Attempted by {inter.author}', icon_url=inter.author.avatar.url)
                return await inter.response.send_message(delete_after=15, embed=embed)
            if member.top_role >= inter.author.top_role:
                embed = disnake.Embed(title=f"You cannot ban ``{member}`` because they have a higher role than you!", color=config.Error())
                embed.set_footer(text=f'Attempted by {inter.author}', icon_url=inter.author.avatar.url)
                return await inter.response.send_message(delete_after=15, embed=embed)
            try:
                embed = disnake.Embed(title=f"You Have Been Banned from **{member.guild.name}**!", color=config.Success())
                embed.add_field(name="Reason:", value=f"``{reason}``", inline=False)
                embed.set_footer(text=f'Banned by {inter.author}', icon_url=inter.author.avatar.url)
                await member.send(embed=embed)
            except:
                pass
            await member.ban(reason=reason)
            embed = disnake.Embed(title=f"Successfully Banned ``{member}`` for ``{reason}``", color=config.Success())
            embed.set_footer(text=f'Banned by {inter.author}', icon_url=inter.author.avatar.url)
            await inter.response.send_message(embed=embed)
        except Exception as e:
            print(f'Error sending ban command: {e}')
            await inter.send(embed=errors.create_error_embed(f"Error sending ban command: {e}"))

    # unban command 
    @commands.slash_command(name='unban',
                            description='Unban a member',)
    async def unban(self, inter: disnake.ApplicationCommandInteraction, member: disnake.User):
        try:
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
        except Exception as e:
            print(f'Error sending unban command: {e}')
            await inter.send(embed=errors.create_error_embed(f"Error sending unban command: {e}"))

    # Nuke command that nukes channels
    @commands.slash_command(name='nuke',
                            description='Nuke a channel',)
    async def nuke(self, inter: disnake.ApplicationCommandInteraction, channel: disnake.TextChannel = None):
        try:
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
        except Exception as e:
            print(f'Error sending nuke command: {e}')
            await inter.send(embed=errors.create_error_embed(f"Error sending nuke command: {e}"))

    # deletes any .exe, .bat, .sh files that are uploaded however allows certain roles to bypass this
    @commands.Cog.listener()
    async def on_message(self, message):
        try:
            if message.author.bot:
                return
            if message.attachments:
                for attachment in message.attachments:
                    if attachment.filename.endswith('.') or attachment.filename.endswith('.bat') or attachment.filename.endswith('.sh'):
                        await message.delete()
                        embed = disnake.Embed(title=f"``{attachment.filename}`` is not allowed!", color=config.Error())
                        embed.set_footer(text=f'Attempted by {message.author}', icon_url=message.author.avatar.url)
                        await message.channel.send(embed=embed)
        except Exception as e:
            print(f'Error sending on_message (delete illgal files) command: {e}')

    # warn command that logs warnings & reason for the warn to a json and then kicks the user if they reach 3 warns, then bans them if they reach 5 warns
    @commands.slash_command(name='warn',
                            description='Warn a member',)
    async def warn(self, inter: disnake.ApplicationCommandInteraction, member: disnake.Member, *, reason: str = None):
        try:
            if not inter.author.guild_permissions.kick_members:
                embed = disnake.Embed(title=f"You do not have permission to warn ``{member}!``", color=config.Error())
                embed.set_footer(text=f'Attempted by {inter.author}', icon_url=inter.author.avatar.url)
                return await inter.response.send_message(ephemeral=True, embed=embed)   
            if not inter.guild.me.guild_permissions.kick_members:
                embed = disnake.Embed(title=f"I do not have permission to warn ``{member}!``", color=config.Error())
                embed.set_footer(text=f'Attempted by {inter.author}', icon_url=inter.author.avatar.url)
                return await inter.response.send_message(delete_after=15, embed=embed)
            if member.top_role >= inter.author.top_role:
                embed = disnake.Embed(title=f"You cannot warn ``{member}`` because they have a higher role than you!", color=config.Error())
                embed.set_footer(text=f'Attempted by {inter.author}', icon_url=inter.author.avatar.url)
                return await inter.response.send_message(delete_after=15, embed=embed)
            if reason is None:
                reason = "No reason provided"
            with open('data/warns.json', 'r') as f:
                warns = json.load(f)
            if str(member.id) not in warns:
                warns[str(member.id)] = []
            warns[str(member.id)].append(reason)
            with open('data/warns.json', 'w') as f:
                json.dump(warns, f, indent=4)
            embed = disnake.Embed(title=f"Successfully Warned ``{member}`` for ``{reason}``", color=config.Success())
            embed.set_footer(text=f'Warned by {inter.author}', icon_url=inter.author.avatar.url)
            await inter.response.send_message(embed=embed)
            if len(warns[str(member.id)]) == 3:
                embed = disnake.Embed(title=f"You Have Been Warned 3 Times in **{member.guild.name}**!", color=config.Success())
                embed.add_field(name="Reason:", value=f"``{reason}``", inline=False)
                embed.set_footer(text=f'Warned by {inter.author}', icon_url=inter.author.avatar.url)
                await member.send(embed=embed)
                await member.kick(reason=reason)
                embed = disnake.Embed(title=f"Successfully Kicked ``{member}`` for ``{reason}``", color=config.Success())
                embed.set_footer(text=f'Kicked by {inter.author}', icon_url=inter.author.avatar.url)
                await inter.response.send_message(embed=embed)
            if len(warns[str(member.id)]) == 5:
                embed = disnake.Embed(title=f"You Have Been Warned 5 Times in **{member.guild.name}**!", color=config.Success())
                embed.add_field(name="Reason:", value=f"``{reason}``", inline=False)
                embed.set_footer(text=f'Warned by {inter.author}', icon_url=inter.author.avatar.url)
                await member.send(embed=embed)
                await member.ban(reason=reason)
                embed = disnake.Embed(title=f"Successfully Banned ``{member}`` for ``{reason}``", color=config.Success())
                embed.set_footer(text=f'Banned by {inter.author}', icon_url=inter.author.avatar.url)
                await inter.response.send_message(embed=embed)
        except Exception as e:
            print(f'Error sending warn command: {e}')
            await inter.send(embed=errors.create_error_embed(f"Error sending warn command: {e}"))

    # warns command that shows the amount of warns a user has
    @commands.slash_command(name='warns',
                            description='Shows the amount of warns of a member',)
    async def warns(self, inter: disnake.ApplicationCommandInteraction, member: disnake.Member):
        try:
            if not inter.author.guild_permissions.kick_members:
                embed = disnake.Embed(title=f"You do not have permission to check the warns of ``{member}!``", color=config.Error())
                embed.set_footer(text=f'Attempted by {inter.author}', icon_url=inter.author.avatar.url)
                return await inter.response.send_message(ephemeral=True, embed=embed)   
            if not inter.guild.me.guild_permissions.kick_members:
                embed = disnake.Embed(title=f"I do not have permission to check the warns of ``{member}!``", color=config.Error())
                embed.set_footer(text=f'Attempted by {inter.author}', icon_url=inter.author.avatar.url)
                return await inter.response.send_message(delete_after=15, embed=embed)
            with open('data/warns.json', 'r') as f:
                warns = json.load(f)
            if str(member.id) not in warns:
                embed = disnake.Embed(title=f"``{member}`` has no warns!", color=config.Success())
                embed.set_footer(text=f'Warns checked by {inter.author}', icon_url=inter.author.avatar.url)
                return await inter.response.send_message(embed=embed)
            embed = disnake.Embed(title=f"``{member}`` has ``{len(warns[str(member.id)])}`` warns!", color=config.Success())
            embed.set_footer(text=f'Warns checked by {inter.author}', icon_url=inter.author.avatar.url)
            await inter.response.send_message(embed=embed)
        except Exception as e:
            print(f'Error sending warns command: {e}')
            await inter.send(embed=errors.create_error_embed(f"Error sending warns command: {e}"))

    # clearwarns command that clears the amount of warns that you choose of a user 
    @commands.slash_command(name='clearwarns',
                            description='Clear the warns of a member',)
    async def clearwarns(self, inter: disnake.ApplicationCommandInteraction, member: disnake.Member, amount: int):
        try:
            if not inter.author.guild_permissions.kick_members:
                embed = disnake.Embed(title=f"You do not have permission to clear the warns of ``{member}!``", color=config.Error())
                embed.set_footer(text=f'Attempted by {inter.author}', icon_url=inter.author.avatar.url)
                return await inter.response.send_message(ephemeral=True, embed=embed)   
            if not inter.guild.me.guild_permissions.kick_members:
                embed = disnake.Embed(title=f"I do not have permission to clear the warns of ``{member}!``", color=config.Error())
                embed.set_footer(text=f'Attempted by {inter.author}', icon_url=inter.author.avatar.url)
                return await inter.response.send_message(delete_after=15, embed=embed)
            if member.top_role >= inter.author.top_role:
                embed = disnake.Embed(title=f"You cannot clear the warns of ``{member}`` because they have a higher role than you!", color=config.Error())
                embed.set_footer(text=f'Attempted by {inter.author}', icon_url=inter.author.avatar.url)
                return await inter.response.send_message(delete_after=15, embed=embed)
            if amount > 5:
                embed = disnake.Embed(title=f"You cannot clear more than 5 warns at a time!", color=config.Error())
                embed.set_footer(text=f'Attempted by {inter.author}', icon_url=inter.author.avatar.url)
                return await inter.response.send_message(delete_after=15, embed=embed)
            with open('data/warns.json', 'r') as f:
                warns = json.load(f)
            if str(member.id) not in warns:
                embed = disnake.Embed(title=f"``{member}`` has no warns!", color=config.Success())
                embed.set_footer(text=f'Checked by {inter.author}', icon_url=inter.author.avatar.url)
                return await inter.response.send_message(embed=embed)
            if len(warns[str(member.id)]) < amount:
                embed = disnake.Embed(title=f"``{member}`` does not have ``{amount}`` warns!", color=config.Success())
                embed.set_footer(text=f'Checked by {inter.author}', icon_url=inter.author.avatar.url)
                return await inter.response.send_message(embed=embed)
            for i in range(amount):
                warns[str(member.id)].pop()
            with open('data/warns.json', 'w') as f:
                json.dump(warns, f, indent=4)
            embed = disnake.Embed(title=f"Successfully cleared ``{amount}`` warns of ``{member}``!", color=config.Success())
            embed.set_footer(text=f'Checked by {inter.author}', icon_url=inter.author.avatar.url)
            await inter.response.send_message(embed=embed)
        except Exception as e:
            print(f'Error sending clearwarns command: {e}')
            await inter.send(embed=errors.create_error_embed(f"Error sending clearwarns command: {e}"))

    # clearallwarns command that clears all the warns of a user
    @commands.slash_command(name='clearallwarns',
                            description='Clear all the warns of a member',)
    async def clearallwarns(self, inter: disnake.ApplicationCommandInteraction, member: disnake.Member):
        try:
            if not inter.author.guild_permissions.kick_members:
                embed = disnake.Embed(title=f"You do not have permission to clear the warns of ``{member}!``", color=config.Error())
                embed.set_footer(text=f'Attempted by {inter.author}', icon_url=inter.author.avatar.url)
                return await inter.response.send_message(ephemeral=True, embed=embed)   
            if not inter.guild.me.guild_permissions.kick_members:
                embed = disnake.Embed(title=f"I do not have permission to clear the warns of ``{member}!``", color=config.Error())
                embed.set_footer(text=f'Attempted by {inter.author}', icon_url=inter.author.avatar.url)
                return await inter.response.send_message(delete_after=15, embed=embed)
            if member.top_role >= inter.author.top_role:
                embed = disnake.Embed(title=f"You cannot clear the warns of ``{member}`` because they have a higher role than you!", color=config.Error())
                embed.set_footer(text=f'Attempted by {inter.author}', icon_url=inter.author.avatar.url)
                return await inter.response.send_message(delete_after=15, embed=embed)
            with open('data/warns.json', 'r') as f:
                warns = json.load(f)
            if str(member.id) not in warns:
                embed = disnake.Embed(title=f"``{member}`` has no warns!", color=config.Success())
                embed.set_footer(text=f'Checked by {inter.author}', icon_url=inter.author.avatar.url)
                return await inter.response.send_message(embed=embed)
            warns.pop(str(member.id))
            with open('data/warns.json', 'w') as f:
                json.dump(warns, f, indent=4)
            embed = disnake.Embed(title=f"Successfully cleared all warns of ``{member}``!", color=config.Success())
            embed.set_footer(text=f'Checked by {inter.author}', icon_url=inter.author.avatar.url)
            await inter.response.send_message(embed=embed)
        except Exception as e:
            print(f'Error sending clearallwarns command: {e}')
            await inter.send(embed=errors.create_error_embed(f"Error sending clearallwarns command: {e}"))

def setup(bot):
    bot.add_cog(moderation(bot))