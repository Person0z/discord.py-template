###############################################
#           Template made by Person0z         #
#          https://github.com/Person0z        #
#           Copyright© Person0z, 2022         #
#           Do Not Remove This Header         #
###############################################

# Importing the required modules
import disnake
from disnake.ext import commands, tasks
import os
import psutil 
import requests
import json
import aiohttp
import config
from helpers import errors

class general(commands.Cog):
    
    def __init__(self, bot):
    	self.bot = bot
        
    @commands.Cog.listener()
    async def on_ready(self):
        print(f'Loaded Cog General')

    # Ping Command
    @commands.slash_command(name='ping', description='Get the bot\'s latency',)
    async def ping(self, inter: disnake.ApplicationCommandInteraction):
        try:
            embed = disnake.Embed(title=f"Pong!", description=f"The ping is around `{round(self.bot.latency * 1000)}ms`", color=config.Success())
            embed.set_footer(text=f'Command executed by {inter.author}', icon_url=inter.author.avatar.url)
            await inter.response.send_message(ephemeral=True, embed=embed)
        except Exception as e:
            print(f'Error Sending Ping Command: {e}')
            await inter.send(embed=errors.create_error_embed(f"Error sending ping command: {e}"))

    # Check Slash Command (Checks if the bot is online)
    @commands.slash_command(name="check", description="Check if the bot is online!")
    async def check(inter):
        try:
            embed = disnake.Embed(title=f"Bot Status", description=f"Bot is online!", color=config.Success())
            embed.set_footer(text=f'Requested by {inter.author}', icon_url=inter.author.avatar.url)
            await inter.send(ephemeral=True, embed=embed)
        except Exception as e:
            print(f'Error Sending Check Command: {e}')
            await inter.send(embed=errors.create_error_embed(f"Error sending check command: {e}"))

    # user info command
    @commands.slash_command(name='userinfo', description='Get info about a user')
    async def userinfo(self, inter: disnake.ApplicationCommandInteraction, member: disnake.Member = None):
        try:
            if member is None:
                member = inter.author
            embed = disnake.Embed(title=f"{member.name}'s Info", color=config.Success())
            embed.add_field (name="\nUser Info", value=f"\n**User:** ```{member.name}#{member.discriminator} ({member.id})```\n**Account Created:** ```{member.created_at.strftime('%a, %#d %B %Y, %I:%M %p UTC')}```\n**Joined Server:** ```{member.joined_at.strftime('%a, %#d %B %Y, %I:%M %p UTC')}```", inline=False)
            embed.add_field (name="User Top Role", value=f"{member.top_role.mention}", inline=False)
            embed.add_field (name="User Roles", value=f"{', '.join([role.mention for role in member.roles])}", inline=False)
            embed.add_field (name="User Permissions", value=f"```{', '.join([perm for perm, value in member.guild_permissions if value])}```", inline=False)
            embed.add_field (name="User Status", value=f"```{member.status}```", inline=False)
            embed.add_field (name="User Boosting", value=f"```{member.premium_since}```", inline=False)
            embed.add_field (name="User Avatar", value=f"[Click Here]({member.avatar.url})", inline=False)
            embed.add_field (name="User Profile", value=f"[Click Here](https://discord.com/users/{member.id})", inline=False)
            embed.add_field (name="User Mention", value=f"{member.mention}", inline=False)
            embed.set_thumbnail(url=member.avatar.url)
            embed.set_footer(text=f'Requested by {inter.author}', icon_url=inter.author.avatar.url)
            await inter.response.send_message(embed=embed)
        except Exception as e:
            print(f'Error sending userinfo message: {e}')
            await inter.send(embed=errors.create_error_embed(f"Error sending userinfo command: {e}"))
    
    # server info command
    @commands.slash_command(name='serverinfo', description='Get info about the server',)
    async def serverinfo(self, inter: disnake.ApplicationCommandInteraction):
        try:
            embed = disnake.Embed(title=f"{inter.guild.name}'s Info", color=config.Success())
            embed.add_field (name="\nServer Info", value=f"\n**Server:** ```{inter.guild.name} ({inter.guild.id})```\n**Server Owner:** ```{inter.guild.owner.name}#{inter.guild.owner.discriminator} ({inter.guild.owner.id})```\n**Server Created:** ```{inter.guild.created_at.strftime('%a, %#d %B %Y, %I:%M %p UTC')}```\n**Server Region:** ```{inter.guild.region}```\n**Nitro Info (Boosts):** ```People Boosting: {inter.guild.premium_subscription_count}\nServer Boost Level: {inter.guild.premium_tier}```\n**Server Members:** ```{inter.guild.member_count}```\n**Server Channels:** ```{len(inter.guild.channels)}```\n**Server Emojis:** ```{len(inter.guild.emojis)}```", inline=False)
            embed.add_field (name="Server Roles", value=f"{', '.join([role.mention for role in inter.guild.roles])}", inline=False)
            embed.add_field (name="Server Icon", value=f"[Click Here]({inter.guild.icon.url})", inline=False)
            embed.set_thumbnail(url=inter.guild.icon.url)
            embed.set_footer(text=f'Requested by {inter.author}', icon_url=inter.author.avatar.url)
            await inter.response.send_message(embed=embed)
        except Exception as e:
            print(f'Error sending serverinfo message: {e}')
            await inter.send(embed=errors.create_error_embed(f"Error sending serverinfo command: {e}"))
        
    # Bot CPU and RAM usage with storage usage
    @commands.slash_command(name='botinfo', description='Get info about the bot',)
    async def botinfo(self, inter: disnake.ApplicationCommandInteraction):
        try:
            cpu = psutil.cpu_percent()
            ram_used = psutil.virtual_memory().used / (1024.0 ** 3)
            ram_total = psutil.virtual_memory().total / (1024.0 ** 3)
            storage_used = psutil.disk_usage('/').used / (1024.0 ** 3)
            storage_total = psutil.disk_usage('/').total / (1024.0 ** 3)
            embed = disnake.Embed(title=f"{self.bot.user.name}'s Info", color=config.Success())
            embed.add_field (name="\nBot Info", value=f"\n**Bot:** ```{self.bot.user.name}#{self.bot.user.discriminator} ({self.bot.user.id})```", inline=False)
            embed.add_field (name="Bot Created:", value=f"```{self.bot.user.created_at.strftime('%a, %#d %B %Y, %I:%M %p UTC')}```", inline=False)
            embed.add_field (name="Bot CPU Usage:", value=f"```{cpu}% / 100%```", inline=True)
            embed.add_field (name="Bot RAM Usage:", value=f"```{ram_used:.2f} GB / {ram_total:.2f} GB```", inline=True)
            embed.add_field (name="Bot Storage Usage:", value=f"```{storage_used:.2f} GB / {storage_total:.2f} GB```", inline=True)
            embed.add_field (name="Bot Ping:", value=f"```{round(self.bot.latency * 1000)}ms```", inline=True)
            embed.add_field (name="Bot Version:", value=f"```{config.version}```", inline=True)
            embed.add_field (name="Bot Library:", value="```Disnake```", inline=True)
            embed.add_field (name="Bot Developer:", value="```Person0z#0812\n./Zerbaib.sh#6400```", inline=False)

            embed.add_field (name="Bot Avatar", value=f"[Click Here]({self.bot.user.avatar.url})", inline=False)
            embed.add_field (name="Bot Profile", value=f"[Click Here](https://discord.com/users/{self.bot.user.id})", inline=False)
            embed.set_thumbnail(url=self.bot.user.avatar.url)
            embed.set_footer(text=f'Requested by {inter.author}', icon_url=inter.author.avatar.url)
            await inter.response.send_message(embed=embed)
        except Exception as e:
            print(f'Error sending botinfo message: {e}')
            await inter.send(embed=errors.create_error_embed(f"Error sending botinfo command: {e}"))


    # invite the bot to your server
    @commands.slash_command(name='invite', description='Invite the bot to your server',)
    async def invite(self, inter: disnake.ApplicationCommandInteraction):
        try:
            embed = disnake.Embed(title="Invite Me", color=config.Success())
            embed.add_field (name="Invite Link", value=f"[Click Here](https://discord.com/api/oauth2/authorize?client_id={self.bot.user.id}&permissions=8&scope=bot%20applications.commands)", inline=False)
            embed.set_footer(text=f'Requested by {inter.author}', icon_url=inter.author.avatar.url)
            await inter.response.send_message(embed=embed)
        except Exception as e:
            print(f'Error sending invite message: {e}')
            await inter.send(embed=errors.create_error_embed(f"Error sending invite command: {e}"))

    @commands.slash_command(name='poll', description='Create a poll and we can react for vote')
    async def poll(self, inter, *, question):
        try:
            embed = disnake.Embed(
                title="A new poll apear !",
                description=f"{question}",
                color=config.Random()
            )
            embed.set_footer(
                text=f"Poll created by: {inter.author} • React to vote !"
            )
            await inter.send(embed=embed)
            await inter.add_reaction("👍")
            await inter.add_reaction("👎")
            await inter.add_reaction("🤷")
        except Exception as e:
            print(f'Error sending poll command: {e}')
            await inter.send(embed=errors.create_error_embed(f"Error sending poll command: {e}"))
                
def setup(bot):
    bot.add_cog(general(bot))