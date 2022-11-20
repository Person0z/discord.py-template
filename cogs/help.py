###############################################
#           Template made by Person0z         #
#         Help Command Made by ๖̶̶̶ζ͜͡Zerbaib      #
#           https://github.com/Zerbaib        #
#          https://github.com/Person0z        #
#           Copyright© Person0z, 2022         #
#           Do Not Remove This Header         #
###############################################

import disnake
from disnake.ext import commands
import os
import config

class help(commands.Cog):

    def __init__(self, bot):
    	self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f'Loaded Cog Help')

    # Help Command
    @commands.slash_command(name='help',
                            description='Get Useful (or not) Commands!',)
    async def help(self, inter: disnake.ApplicationCommandInteraction):
        embedVar = disnake.Embed(
            title="Help Commands!",
            description="Check important commands, that you can use!",
            colour=config.Success())
        embedVar.add_field(name="Bot Prefix", value="```/ + !```", inline=False)
        embedVar.add_field(name="Moderation Commands",
                            value=
                                "```/slowmode - Activate slow mode for a channel```" +
                                "```/lock - Lock the channel from any chitter```" +
                                "```/unlock - Unlock the channel for people to chitter```" +
                                "```/purge - Purge (delete) bulk messages```" +
                                "```/kick - Kick someone from the server```" +
                                "```/ban - Ban someone from the server```" +
                                "```/unban -Unban someone from the server```" +
                                "```/nuke - Nuke a channel to brand new```",
                                inline=False)
        embedVar.add_field(name="Fun commands",
                            value=
                            "```/dice - Role a dice, get a number from 1-6```" +
                            "```/8ball - Ask a question, get an \"Honest\" response```" +
                            "```/coinflip - Flip a coin, see what side it lands on!```" +
                            "```/generate - Generate an image from a text!```" +
                            "```/bitcoin - Check the current price of BitCoin```",
                            inline=True)
        embedVar.add_field(name="Ticket Commands",
                            value=
                            "```/ticket - Create a Ticket```" +
                            "```/close - Close a Ticket```" +
                            "```/add - Add a user to a ticket```" +
                            "```/remove - Remove a user from the ticket```" +
                            "```/list - List Pople and roles in a ticket```",
                            inline=True)
        embedVar.set_thumbnail(
            url="https://us-east-1.tixte.net/uploads/your-parents.wants.solutions/help.png"
        )
        await inter.response.send_message(embed=embedVar, delete_after=10)

def setup(bot):
    bot.add_cog(help(bot))
