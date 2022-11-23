import disnake
from disnake.ext import commands
import os
import json

class Tag(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # Tag view command 
    @commands.slash_command(name="tag", description="View a tag")
    async def tag(self, inter, tag: str):
        with open("tags.json", "r") as f:
            tags = json.load(f)

        if tag not in tags:
            return await inter.send("That tag does not exist!")

        embed = disnake.Embed(title=tag, description=tags[tag], color=disnake.Color.random())
        await inter.send(embed=embed)

    # Tag add command
    @commands.slash_command(name="addtag", description="Add a tag")
    async def addtag(self, inter, tag: str, *, content: str):
        with open("tags.json", "r") as f:
            tags = json.load(f)

        if tag in tags:
            return await inter.send("That tag already exists!")

        tags[tag] = content

        with open("tags.json", "w") as f:
            json.dump(tags, f, indent=4)

        await inter.send(f"Added tag {tag}")

    # Tag remove command
    @commands.slash_command(name="removetag", description="Remove a tag")
    async def removetag(self, inter, tag: str):
        with open("tags.json", "r") as f:
            tags = json.load(f)

        if tag not in tags:
            return await inter.send("That tag does not exist!")

        tags.pop(tag)

        with open("tags.json", "w") as f:
            json.dump(tags, f, indent=4)

        await inter.send(f"Removed tag {tag}")

    # Tag list command
    @commands.slash_command(name="taglist", description="List all tags")
    async def taglist(self, inter):
        with open("tags.json", "r") as f:
            tags = json.load(f)

        embed = disnake.Embed(title="Tags", description=", ".join(tags.keys()), color=disnake.Color.random())
        await inter.send(embed=embed)

    # Tag edit command
    @commands.slash_command(name="edittag", description="Edit a tag")
    async def edittag(self, inter, tag: str, *, content: str):
        with open("tags.json", "r") as f:
            tags = json.load(f)

        if tag not in tags:
            return await inter.send("That tag does not exist!")

        tags[tag] = content

        with open("tags.json", "w") as f:
            json.dump(tags, f, indent=4)

        await inter.send(f"Edited tag {tag}")

def setup(bot):
    bot.add_cog(Tag(bot))
