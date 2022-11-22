import disnake
from disnake.ext import commands
import os
import json

class Tag(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # Tag Command in tag/<tag_name>.json
    @commands.command()
    async def tag(self, ctx, tag_name):
        with open(f"tag/{tag_name}.json", "r") as f:
            tag = json.load(f)
        await ctx.send(tag["content"])


    # Tag Create Command
    @commands.slash_command()
    async def tag_create(self, ctx, tag_name, *, content):
        with open(f"tag/{tag_name}.json", "w") as f:
            json.dump({"content": content}, f)
        await ctx.send("Tag Created!")

    # Tag Delete Command
    @commands.slash_command()
    async def tag_delete(self, ctx, tag_name):
        os.remove(f"tag/{tag_name}.json")
        await ctx.send("Tag Deleted!")

    # Tag Edit Command
    @commands.slash_command()
    async def tag_edit(self, ctx, tag_name, *, content):
        with open(f"tag/{tag_name}.json", "w") as f:
            json.dump({"content": content}, f)
        await ctx.send("Tag Edited!")

    # Tag List Command
    @commands.slash_command()
    async def tag_list(self, ctx):
        tags = []
        for file in os.listdir("tag"):
            if file.endswith(".json"):
                tags.append(file[:-5])
        await ctx.send(f"Tags: {', '.join(tags)}")
        
def setup(bot):
    bot.add_cog(Tag(bot))
