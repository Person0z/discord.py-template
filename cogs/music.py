import disnake
from disnake.ext import commands
import config

class music(commands.Cog):
    def __init__(self, bot):
    	self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f'Loaded Cog Music')

    @commands.slash_command(name="play", description="play music on youtube")
    async def play(self, inter: disnake.ApplicationCommandInteraction, name: int):
        embed = disnake.Embed(title=f"Successfully add music {name} to queue", color=config.Success())
        embed.set_footer(text=f'Set by {inter.author}', icon_url=inter.author.avatar.url)
        await inter.response.send_message(embed=embed)

def setup(bot):
    bot.add_cog(music(bot))