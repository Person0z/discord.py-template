import disnake
from disnake.ext import commands
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
                           description='Find the web latency of the bot',)
    async def ping(self, inter: disnake.ApplicationCommandInteraction):
        await inter.response.send_message(f"Pong! {round(self.bot.latency * 1000)}ms")

    # Help Command
    @commands.slash_command(name='help',
                            description='Get Useful Info About The Bot',)
    async def help(self, inter: disnake.ApplicationCommandInteraction):
        embed = disnake.Embed(title="EvoGen's Personal Help Menu", color=disnake.Color.random())
        embed.set_author(name="Bot Info", icon_url=self.bot.user.avatar.url)
        embed.add_field(name="Birth Giver", value="Person0z#0812", inline=False)
        embed.add_field(name="Bot Version", value="v1.0", inline=False)
        embed.add_field(name="Prefix", value="</help:1041221660835057695> (Slash Commands)", inline=False)
        embed.add_field(name="Ping", value=f"Pong! {round(self.bot.latency * 1000)}ms", inline=False)
        embed.add_field(name="Commands", value="``fox``, ``generate``, ``help``, ``invite``, ``panda``, ``ping``", inline=False)
        embed.set_footer(text=f'Requested by {inter.author}', icon_url=inter.author.avatar.url)
        await inter.response.send_message(embed=embed)

    # Check Slash Command (Checks if the bot is online)
    @commands.slash_command(name="check", description="Check if the bot is online!")
    async def check(inter):
        embed = disnake.Embed(title=f"Bot Status", description=f"Bot is online!", color=disnake.Color.random())
        embed.set_footer(text=f'Requested by {inter.author}', icon_url=inter.author.avatar.url)
        await inter.send(embed=embed)

    # Invite Command
    @commands.slash_command(name='invite',
                            description='Get the invite link for the bot',)
    async def invite(self, inter: disnake.ApplicationCommandInteraction):
        embed = disnake.Embed(title="EvoGen Invite URL", color=disnake.Color.random())
        embed.add_field(name="Invite me by clicking the link below", value=f"Invite me by clicking [here](https://discord.com/api/oauth2/authorize?client_id=1041164439199694868&permissions=8&scope=bot)", inline=True)
        await inter.author.send(embed=embed)
        await inter.response.send_message("I sent you a private message!")

    # a welcome message when someone joins the server with there porfile picture and name in the embed and a welcome message in the chat in a custom channel
    @commands.Cog.listener()
    async def on_member_join(self, member):
        channel = self.bot.get_channel(config.welcome_channel)
        embed = disnake.Embed(title=f"Welcome {member.name}!", description=f"Welcome to {member.guild.name}! We hope you enjoy your stay here!", color=disnake.Color.random())
        embed.set_thumbnail(url=member.avatar.url)
        embed.set_footer(text=f"{member.guild.name} | {member.guild.member_count} Members", icon_url=member.guild.icon.url)
        await channel.send(embed=embed)
        await channel.send(f"Welcome {member.mention} to the server!", delete_after=0.5)

    # a goodbye message when someone leaves the server with there porfile picture and name in the embed and a goodbye message in the chat in a custom channel
    @commands.Cog.listener()
    async def on_member_remove(self, member):
        channel = self.bot.get_channel(config.welcome_channel)
        embed = disnake.Embed(title=f"Goodbye {member.name}!", description=f"Goodbye {member.name}! We hope you enjoyed your stay here!", color=disnake.Color.random())
        embed.set_thumbnail(url=member.avatar.url)
        embed.set_footer(text=f"{member.guild.name} | {member.guild.member_count} Members", icon_url=member.guild.icon.url)
        await channel.send(embed=embed)


def setup(bot):
    bot.add_cog(general(bot))
