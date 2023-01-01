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
import config

class general(commands.Cog):
    
    def __init__(self, bot):
    	self.bot = bot
        
    @commands.Cog.listener()
    async def on_ready(self):
        print(f'Loaded Cog General')
        
    # Ping Command
    @commands.slash_command(name='ping',
                            description='Get the bot\'s latency',)
    async def ping(self, inter: disnake.ApplicationCommandInteraction):
        embed = disnake.Embed(title=f"Pong!", description=f"The ping is around `{round(self.bot.latency * 1000)}ms`", color=config.Success())
        embed.set_footer(text=f'Command executed by {inter.author}', icon_url=inter.author.avatar.url)
        await inter.response.send_message(ephemeral=True, embed=embed)

    # Check Slash Command (Checks if the bot is online)
    @commands.slash_command(name="check", description="Check if the bot is online!")
    async def check(inter):
        embed = disnake.Embed(title=f"Bot Status", description=f"Bot is online!", color=config.Success())
        embed.set_footer(text=f'Requested by {inter.author}', icon_url=inter.author.avatar.url)
        await inter.send(ephemeral=True, embed=embed)

    # Invite Command
    @commands.slash_command(name='invite',
                            description='Get the invite link for the bot',)
    async def invite(self, inter: disnake.ApplicationCommandInteraction):
        embed = disnake.Embed(title=f"{self.bot.user}'s Invite URL", color=config.Success())
        embed.add_field(name="Invite me by clicking the link below", value=f"Invite me by clicking [here](https://discord.com/api/oauth2/authorize?client_id=1041164439199694868&permissions=8&scope=bot)", inline=True)
        await inter.author.send(embed=embed)
        embed = disnake.Embed(title=f"{self.bot.user}'s Invite URL", description=f"Check your DMs {inter.author.mention}!", color=config.Success())
        embed.set_footer(text=f'Requested by {inter.author}', icon_url=inter.author.avatar.url)

        await inter.response.send_message(ephemeral=True, embed=embed)

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
            
    # user info command
    @commands.slash_command(name='userinfo',
                            description='Get info about a user',)
    async def userinfo(self, inter: disnake.ApplicationCommandInteraction, member: disnake.Member = None):
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

    # server info command
    @commands.slash_command(name='serverinfo',
                            description='Get info about the server',)
    async def serverinfo(self, inter: disnake.ApplicationCommandInteraction):
        embed = disnake.Embed(title=f"{inter.guild.name}'s Info", color=config.Success())
        embed.add_field (name="\nServer Info", value=f"\n**Server:** ```{inter.guild.name} ({inter.guild.id})```\n**Server Owner:** ```{inter.guild.owner.name}#{inter.guild.owner.discriminator} ({inter.guild.owner.id})```\n**Server Created:** ```{inter.guild.created_at.strftime('%a, %#d %B %Y, %I:%M %p UTC')}```\n**Server Region:** ```{inter.guild.region}```\n**Nitro Info (Boosts):** ```People Boosting: {inter.guild.premium_subscription_count}\nServer Boost Level: {inter.guild.premium_tier}```\n**Server Members:** ```{inter.guild.member_count}```\n**Server Channels:** ```{len(inter.guild.channels)}```\n**Server Emojis:** ```{len(inter.guild.emojis)}```", inline=False)
        embed.add_field (name="Server Roles", value=f"{', '.join([role.mention for role in inter.guild.roles])}", inline=False)
        embed.add_field (name="Server Icon", value=f"[Click Here]({inter.guild.icon.url})", inline=False)
        embed.set_thumbnail(url=inter.guild.icon.url)
        embed.set_footer(text=f'Requested by {inter.author}', icon_url=inter.author.avatar.url)
        await inter.response.send_message(embed=embed)


def setup(bot):
    bot.add_cog(general(bot))
