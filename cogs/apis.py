###############################################
#           Template made by Person0z         #
#          https://github.com/Person0z        #
#           Copyright© Person0z, 2022         #
#           Do Not Remove This Header         #
###############################################

# Importing Libraries
import disnake
from disnake.ext import commands
import os
import aiohttp
import base64
import time
from PIL import Image
from io import BytesIO
import random
import json

class Apis(commands.Cog):
    
    def __init__(self, bot):
        self.bot = bot
        
    @commands.Cog.listener()
    async def on_ready(self):
        print(f'Loaded Cog API')

    # Image Genertor
    @commands.slash_command(name="generate", description="Generate an image from a prompt!")
    async def generate(inter, *, prompt: str):
        await inter.response.defer()
        ETA = int(time.time() + 60)
        loading_images = ["loading/loading.gif",
                          "loading/loading2.gif",
                          "loading/loading3.gif", 
                          "loading/loading4.gif",
                          "loading/loading5.gif"]
        embed = disnake.Embed(title=f"Loading...! Generating image... ETA: <t:{ETA}:R>", color=disnake.Color.random())
        embed.set_image(file=disnake.File(random.choice(loading_images)))
        await inter.send(embed=embed)
        async with aiohttp.request("POST", "https://backend.craiyon.com/generate", json={"prompt": prompt}) as resp:
            if resp.status != 200:
                return await inter.edit_original_response(content="An error occurred while generating the image.")
            data = await resp.json()
            img = Image.open(BytesIO(base64.b64decode(data["images"][0])))
            img.save("image.png")
            embed = disnake.Embed(title=f"The image you wanted generated: {prompt}", color=disnake.Color.random())
            embed.set_image(file=disnake.File('image.png'))
            await inter.edit_original_response(content=None, embed=embed)
            os.remove("image.png")

    # BitCoin Slash Command
    @commands.slash_command(name="bitcoin", description="Get the current price of Bitcoin!")
    async def bitcoin(inter):
        url = "https://api.coindesk.com/v1/bpi/currentprice.json"
        async with aiohttp.request("GET", url) as response:
            text = await response.text()
            value = json.loads(text)["bpi"]["USD"]["rate"]
            embed = disnake.Embed(title=f"Bitcoin Price", description=f"Current bitcoin price: ${value}", color=disnake.Color.random())
            embed.set_footer(text=f'Requested by {inter.author}', icon_url=inter.author.avatar.url)
            await inter.send(embed=embed)

def setup(bot):
    bot.add_cog(Apis(bot))
