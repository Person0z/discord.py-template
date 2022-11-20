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
                            description='Affiche des info utile du bot',)
    async def help(self, inter: disnake.ApplicationCommandInteraction):
        embedVar = disnake.Embed(
            title="Voicie la page d'aide !",
            description="Il y a toutes les commandes importante !",
            colour=config.Success())
        embedVar.add_field(name="Bot Prefix", value="/", inline=False)
        embedVar.add_field(name="Moderation Commands",
                            value=
                                "```/slowmode - active le mod ralentie sur un channel```" +
                                "```/lock - permet de blocker un channel```" +
                                "```/unlock - permet de deblocker un channel```" +
                                "```/purge - permet de clear des message```" +
                                "```/kick - permet de ejecter une personne du serveur```" +
                                "```/ban - permet de ban une personne du serveur```" +
                                "```/unban - permet de de ban une personne du serveur```" +
                                "```/nuke - permet de reset un channel```",
                                inline=False)
        embedVar.add_field(name="Fun commands",
                            value=
                            "```/dice - permet de faire un lancer de des```" +
                            "```/8ball - pause une question j'y reponds```" +
                            "```/coinflip - fait un pile ou face```" +
                            "```/generate - permet de generer une image grace a des mots et l'ia```" +
                            "```/bitcoin - permet de voirs le prix du bitcoin```",
                            inline=True)
        embedVar.add_field(name="Ticket Commands",
                            value=
                            "```/ticket - cree un ticket```" +
                            "```/close - ferme le ticket```" +
                            "```/add - permet d'ajouter une personne au ticket```" +
                            "```/remove - permet de retirer une personne du ticket```" +
                            "```/list - permet de voirs il y a qui dans le ticket```",
                            inline=True)
        embedVar.set_thumbnail(
            url="https://imgs.search.brave.com/Ia3a2619OnBtBqeN2hcIi5XAgv80ZbhfTrwqPKugqJ8/rs:fit:498:498:1/g:ce/aHR0cHM6Ly9tZWRp/YTEudGVub3IuY29t/L2ltYWdlcy82MTBh/YzIzNDg5OTQ1NjQ1/N2M1NjEyZjRjMjgz/N2Y0ZC90ZW5vci5n/aWY_aXRlbWlkPTEx/MDU3ODg5.gif"
        )
        await inter.response.send_message(embed=embedVar)
    
def setup(bot):
    bot.add_cog(help(bot))