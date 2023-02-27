###############################################
#           Template made by Person0z         #
#          https://github.com/Person0z        #
#           Copyright© Person0z, 2022         #
#           Do Not Remove This Header         #
###############################################

# importing the required modulesimport disnake
import disnake
from disnake.ext import commands
import os
import json
import config
from helpers import errors

class Tag(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f'Loaded Cog Tags')
            
class Tag(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command()
    async def tag(
        self,
        inter: disnake.ApplicationCommandInteraction,
        action: str = commands.Param(choices=["open", "create", "edit", "remove", "list"]),
        tag: str = commands.Param(description="What Tag To Open", default=None)
    ):
        try:
            if action == "open":
                with open("data/tags.json", "r") as f:
                    tags = json.load(f)
                if tag in tags:
                    embed = disnake.Embed(title=f"Tag: {tag}", description=tags[tag])
                    return await inter.send(embed=embed)
                else:
                    embed = disnake.Embed(title=f"Tag: {tag}", description="Tag Not Found")
                    return await inter.send(embed=embed)
            if action == "create":
                with open("data/tags.json", "r") as f:
                    tags = json.load(f)
                if tag in tags:
                    embed = disnake.Embed(title=f"Tag: {tag}", description="Tag Already Exists")
                    return await inter.send(embed=embed)
                else:
                    embed = disnake.Embed(title=f"Tag: {tag}", description="What Do You Want The Tag To Be?")
                    await inter.send(embed=embed)
                    def check(m):
                        return m.author == inter.author and m.channel == inter.channel
                    msg = await self.bot.wait_for("message", check=check)
                    tags[tag] = msg.content
                    with open("data/tags.json", "w") as f:
                        json.dump(tags, f, indent=4)
                    embed = disnake.Embed(title=f"Tag: {tag}", description="Tag Created")
                    return await inter.send(embed=embed)
            if action == "edit":
                with open("data/tags.json", "r") as f:
                    tags = json.load(f)
                if tag in tags:
                    embed = disnake.Embed(title=f"Tag: {tag}", description="What Do You Want The Tag To Be?")
                    await inter.send(embed=embed)
                    def check(m):
                        return m.author == inter.author and m.channel == inter.channel
                    msg = await self.bot.wait_for("message", check=check)
                    tags[tag] = msg.content
                    with open("data/tags.json", "w") as f:
                        json.dump(tags, f, indent=4)
                    embed = disnake.Embed(title=f"Tag: {tag}", description="Tag Edited")
                    return await inter.send(embed=embed)
                else:
                    embed = disnake.Embed(title=f"Tag: {tag}", description="Tag Not Found")
                    return await inter.send(embed=embed)
            if action == "remove":
                with open("data/tags.json", "r") as f:
                    tags = json.load(f)
                if tag in tags:
                    del tags[tag]
                    with open("data/tags.json", "w") as f:
                        json.dump(tags, f, indent=4)
                    embed = disnake.Embed(title=f"Tag: {tag}", description="Tag Removed")
                    return await inter.send(embed=embed)
                else:
                    embed = disnake.Embed(title=f"Tag: {tag}", description="Tag Not Found")
                    return await inter.send(embed=embed)
            if action == "list":
                with open("data/tags.json", "r") as f:
                    tags = json.load(f)
                embed = disnake.Embed(title="Tags", description=", ".join(tags))
                return await inter.send(embed=embed)
        except Exception as e:
            print(e)
            embed = disnake.Embed(title="Error", description="An Error Occured")
            return await inter.send(embed=embed)

def setup(bot):
    bot.add_cog(Tag(bot))