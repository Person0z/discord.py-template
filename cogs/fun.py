import disnake
from disnake.ext import commands
import os

class fun(commands.Cog):
    
    def __init__(self, bot):
    	self.bot = bot
        
    @commands.Cog.listener()
    async def on_ready(self):
        print(f'Loaded Cog Fun')

    @commands.slash_command(name="dice", description="Roll a dice!")
    async def dice(inter):
        dice = ["dice/1.png", "dice/2.png", "dice/3.png", "dice/4.png", "dice/5.png", "dice/6.png"]    
        embed = disnake.Embed(title=f"You Rolled A Dice!", color=disnake.Color.random())
        embed.set_image(file=disnake.File(random.choice(dice)))
        embed.set_footer(text=f'Requested by {inter.author}', icon_url=inter.author.avatar.url)
        msg = await inter.send(embed=embed)

def setup(bot):
    bot.add_cog(fun(bot))
