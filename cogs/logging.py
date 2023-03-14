###############################################
#           Template made by Person0z         #
#          https://github.com/Person0z        #
#           Copyright© Person0z, 2022         #
#           Do Not Remove This Header         #
###############################################

# imports and stuff
from distutils.fancy_getopt import FancyGetopt
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
        print('Loaded Cog Logging')

    @commands.Cog.listener()
    async def on_member_join(self, member):
        try:
            channel = self.bot.get_channel(config.join_channel)
            if role := disnake.utils.get(
                member.guild.roles, name=config.join_role
            ):
                try:
                    await member.add_roles(role)
                except Exception as e:
                    print(f'Error adding role to member: {e}')
            embed = disnake.Embed(title=f"Welcome {member.name}!", description=f"{member.guild.name}! We hope you enjoy your stay here!", color=config.Success())
            embed.add_field (name="\nUser Info", value=f"\n**User:** \n```{member.name}#{member.discriminator} ({member.id})```\n**Account Created:** \n```{member.created_at.strftime('%a, %#d %B %Y, %I:%M %p UTC')}```\n**Joined Server:** \n```{member.joined_at.strftime('%a, %#d %B %Y, %I:%M %p UTC')}```\n", inline=False)
            if member.avatar:
                embed.set_thumbnail(url=member.avatar.url)
            embed.set_footer(text=f"{member.guild.name} | {member.guild.member_count} Members", icon_url=member.guild.icon.url)
            await channel.send(embed=embed)
            await channel.send(f"{member.mention}", delete_after=0.2)
        except Exception as e:
            print(f'Error sending welcome message: {e}')

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        try:
            channel = self.bot.get_channel(config.leave_channel)
            embed = disnake.Embed(title=f"Goodbye {member.name}!", description=f"Goodbye {member.name}! We hope you enjoyed your stay here!", color=config.Error())
            embed.add_field (name="\nUser Info", value=f"\n**User:** ```{member.name}#{member.discriminator} ({member.id})```\n**Account Created:** ```{member.created_at.strftime('%a, %#d %B %Y, %I:%M %p UTC')}```\n**Joined Server:** ```{member.joined_at.strftime('%a, %#d %B %Y, %I:%M %p UTC')}```\n", inline=False)
            if member.avatar:
                embed.set_thumbnail(url=member.avatar.url)
            embed.set_footer(text=f"{member.guild.name} | {member.guild.member_count} Members", icon_url=member.guild.icon.url)
            await channel.send(embed=embed)
        except Exception as e:
            print(f'Error sending goodbye message: {e}')

    # logs deleted messages from all channels in the server
    @commands.Cog.listener()
    async def on_message_delete(self, message):
        try:
            channel = self.bot.get_channel(config.logs)
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

    @commands.Cog.listener()
    async def on_message_edit(self, before, after):
        try:
            channel = self.bot.get_channel(config.logs)
            if before.guild and before.content != after.content:
                embed = disnake.Embed(
                    title="Edited message",
                    description=f"One message was edited in {before.channel.mention}",
                    color=disnake.Color.orange()
                )
                embed.add_field(name="Author", value=before.author.mention)
                embed.add_field(name="Old", value=f"```{before.content}```", inline=False)
                embed.add_field(name="New", value=f"```{after.content}```", inline=False)
                await channel.send(embed=embed)
        except Exception as e:
            print(f'Error sending logging message: {e}')

    @commands.Cog.listener()
    async def on_member_remove(self, member, user):
        channel = self.bot.get_channel(config.logs)
        async for entry in member.guild.audit_logs(limit=1, action=disnake.AuditLogAction.ban):
            if entry.target == member:
                reason = entry.reason
            embed = disnake.Embed(title=f"User was ban",
                              description=f"{user} was ban for ```{reason}```",
                              color=0xFF0000)
            embed.set_author(name=user.name, icon_url=user.avatar_url)
            embed.set_footer(text=f"User ID: {user.id}")
            await channel.send(embed=embed)
        
        async for entry in member.guild.audit_logs(limit=1, action=disnake.AuditLogAction.kick):
            if entry.target == member:
                reason = entry.reason
            embed = disnake.Embed(title=f"User was kick",
                              description=f"{user} was kick for ```{reason}```",
                              color=0xFF0000)
            embed.set_author(name=user.name, icon_url=user.avatar_url)
            embed.set_footer(text=f"User ID: {user.id}")
            await channel.send(embed=embed)

def setup(bot):
    bot.add_cog(logging(bot))