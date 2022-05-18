import disnake
from disnake.ext import commands
import os
import aiohttp

class Apis(commands.Cog):
    
    def __init__(self, bot):
    	self.bot = bot
        
    @commands.Cog.listener()
    async def on_ready(self):
        print(f'Loaded Cog API')
    
    
    # Dogs Pics
    @commands.slash_command(name="Dog",
                       description="Image of a Dog!")
    async def dog(inter):
       async with aiohttp.ClientSession() as session:
         request = await session.get('https://some-random-api.ml/img/dog')
         dogjson = await request.json()
       embed = disnake.Embed(title="Doggo!", color=disnake.Color.purple())
       embed.set_image(url=dogjson['link'])
       await inter.response.send_message(embed=embed)

    # Cat Pics
    @commands.slash_command(name="Cat",
                       description="Image of a Cat!")
    async def cat(inter):
       async with aiohttp.ClientSession() as session:
         request = await session.get('https://some-random-api.ml/img/cat')
         catjson = await request.json()
       embed = disnake.Embed(title="Kitty!", color=disnake.Color.blue())
       embed.set_image(url=catjson['link'])
       await inter.response.send_message(embed=embed)

def setup(bot):
    bot.add_cog(Apis(bot))