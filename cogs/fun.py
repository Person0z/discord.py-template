###############################################
#           Template made by Person0z         #
#          https://github.com/Person0z        #
#           Copyright© Person0z, 2022         #
#           Do Not Remove This Header         #
###############################################

# imports and stuff
import disnake
from disnake.ext import commands
import os
import random
import aiohttp

class fun(commands.Cog):
    
    def __init__(self, bot):
    	self.bot = bot
        
    @commands.Cog.listener()
    async def on_ready(self):
        print(f'Loaded Cog Fun')

    # Dice Roll Slash Command
    @commands.slash_command(name="dice", description="Roll a dice!")
    async def dice(inter):
        dice = ["dice/1.png", "dice/2.png", "dice/3.png", "dice/4.png", "dice/5.png", "dice/6.png"]    
        embed = disnake.Embed(title=f"You Rolled A Dice!", color=disnake.Color.random())
        embed.set_image(file=disnake.File(random.choice(dice)))
        embed.set_footer(text=f'Requested by {inter.author}', icon_url=inter.author.avatar.url)
        msg = await inter.send(embed=embed)

    # 8 ball command
    @commands.slash_command(name="8ball", description="Ask the 8ball a question!")
    async def eightball(inter, *, question):
        responses = ["It is certain.", "It is decidedly so.", "Without a doubt.", "Yes - definitely.", "You may rely on it.", "As I see it, yes.", "Most likely.", "Outlook good.", "Yes.", "Signs point to yes.", "Reply hazy, try again.", "Ask again later.", "Better not tell you now.", "Cannot predict now.", "Concentrate and ask again.", "Don't count on it.", "My reply is no.", "My sources say no.", "Outlook not so good.", "Very doubtful."]
        embed = disnake.Embed(title=f"8ball", description=f"Question: {question}\nAnswer: {random.choice(responses)}", color=disnake.Color.random())
        embed.set_footer(text=f'Requested by {inter.author}', icon_url=inter.author.avatar.url)
        await inter.send(embed=embed)
        
    # Coinflip Slash Command
    @commands.slash_command(name="coinflip", description="Flip a coin!")
    async def coinflip(inter):
        coin = ["heads", "tails"]
        embed = disnake.Embed(title=f"You Flipped A Coin!", description=f"You Flipped {random.choice(coin)}", color=disnake.Color.random())
        embed.set_footer(text=f'Requested by {inter.author}', icon_url=inter.author.avatar.url)
        await inter.send(embed=embed)

    @commands.slash_command(
        name="randomfact",
        description="Get a random fact."
    )
    async def randomfact(self, inter):
        async with aiohttp.ClientSession() as session:
            async with session.get("https://uselessfacts.jsph.pl/random.json?language=en") as request:
                if request.status == 200:
                    data = await request.json()
                    embed = disnake.Embed(title=f"Random Fact!", description=data["text"], color=0xD75BF4)
                    embed.set_footer(text=f'Requested by {inter.author}', icon_url=inter.author.avatar.url)
                else:
                    embed = disnake.Embed(
                        title="Error!",
                        description="There is something wrong with the API, please try again later",
                        color=0xE02B2B
                    )
                await inter.send(embed=embed)
                
def setup(bot):
    bot.add_cog(fun(bot))
