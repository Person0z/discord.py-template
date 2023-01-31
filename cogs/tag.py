import disnake
from disnake.ext import commands
from helpers import errors
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
            
    # Tag view command 
    @commands.slash_command(name="tag", description="View a tag")
    async def tag(self, inter, tag: str):
        try:
            with open("tags.json", "r") as f:
                tags = json.load(f)

            if tag not in tags:
                return await inter.send("That tag does not exist!")

            embed = disnake.Embed(title=tag, description=tags[tag], color=disnake.Color.random())
            await inter.send(embed=embed)
        except Exception as e:
            print(f'Error in tag: {e}')
            await inter.send(embed=errors.create_error_embed(f"Error sending tag command: {e}"))

    # Tag add command
    @commands.slash_command(name="addtag", description="Add a tag")
    async def addtag(self, inter, tag: str, *, content: str):
        try:
            with open("tags.json", "r") as f:
                tags = json.load(f)

            if tag in tags:
                return await inter.send("That tag already exists!")

            tags[tag] = content

            with open("tags.json", "w") as f:
                json.dump(tags, f, indent=4)

            await inter.send(f"Added tag {tag}")
        except Exception as e:
            print(f'Error in addtag: {e}')
            await inter.send(embed=errors.create_error_embed(f"Error sending addtag command: {e}"))

    # Tag remove command
    @commands.slash_command(name="removetag", description="Remove a tag")
    async def removetag(self, inter, tag: str):
        try:
            with open("tags.json", "r") as f:
                tags = json.load(f)

            if tag not in tags:
                return await inter.send("That tag does not exist!")

            tags.pop(tag)

            with open("tags.json", "w") as f:
                json.dump(tags, f, indent=4)

            await inter.send(f"Removed tag {tag}")
        except Exception as e:
            print(f'Error in removetag: {e}')
            await inter.send(embed=errors.create_error_embed(f"Error sending removetag command: {e}"))

    # Tag list command
    @commands.slash_command(name="taglist", description="List all tags")
    async def taglist(self, inter):
        try:
            with open("tags.json", "r") as f:
                tags = json.load(f)

            embed = disnake.Embed(title="Tags", description=", ".join(tags.keys()), color=disnake.Color.random())
            await inter.send(embed=embed)
        except Exception as e:
            print(f'Error in taglist: {e}')

    # Tag edit command
    @commands.slash_command(name="edittag", description="Edit a tag")
    async def edittag(self, inter, tag: str, *, content: str):
        try:
            with open("tags.json", "r") as f:
                tags = json.load(f)

            if tag not in tags:
                return await inter.send("That tag does not exist!")

            tags[tag] = content

            with open("tags.json", "w") as f:
                json.dump(tags, f, indent=4)

            await inter.send(f"Edited tag {tag}")
        except Exception as e:
            print(f'Error in edittag: {e}')
            await inter.send(embed=errors.create_error_embed(f"Error sending edittag command: {e}"))

def setup(bot):
    bot.add_cog(Tag(bot))