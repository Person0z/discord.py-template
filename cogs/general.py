import disnake
from disnake.ext import commands
import os

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


    # Invite Command
    @commands.slash_command(name='invite',
                            description='Get the invite link for the bot',)
    async def invite(self, inter: disnake.ApplicationCommandInteraction):
        embed = disnake.Embed(title="EvoGen Invite URL", color=disnake.Color.random())
        embed.add_field(name="Invite Me By Clicking the Link Below", value=f"Invite me by clicking [here](https://discord.com/api/oauth2/authorize?client_id=1041164439199694868&permissions=8&scope=bot)", inline=True)
        await inter.author.send(embed=embed)
        await inter.response.send_message("I sent you a private message!")

def setup(bot):
    bot.add_cog(general(bot))
