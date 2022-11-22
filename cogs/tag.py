import disnake
from disnake.ext import commands
import os
import json

class Tag(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # Tag parent command
    @commands.slash_command()
    async def tag(
        inter: disnake.ApplicationCommandInteraction,
        action: str = commands.Param(choices=["create", "delete", "edit", "info"]),
        name: str = commands.Param(description="The name of the tag"),
        content: str = commands.Param(description="The content of the tag"),
    ):
        # If the user selects create, it will create a tag
        if action == "create":
            # Checks if the tag already exists
            if os.path.exists(f"tags/{name}.json"):
                await inter.response.send_message("That tag already exists.")
            else:
                # Creates the tag
                with open(f"tags/{name}.json", "w") as f:
                    json.dump({"name": name, "content": content}, f)
                await inter.response.send_message(f"Tag {name} has been created.")
        # If the user selects delete, it will delete the tag
        elif action == "delete":
            # Checks if the tag exists
            if os.path.exists(f"tags/{name}.json"):
                # Deletes the tag
                os.remove(f"tags/{name}.json")
                await inter.response.send_message(f"Tag {name} has been deleted.")
            else:
                await inter.response.send_message("That tag doesn't exist.")
        # If the user selects edit, it will edit the tag
        elif action == "edit":
            # Checks if the tag exists
            if os.path.exists(f"tags/{name}.json"):
                # Edits the tag
                with open(f"tags/{name}.json", "w") as f:
                    json.dump({"name": name, "content": content}, f)
                await inter.response.send_message(f"Tag {name} has been edited.")
            else:
                await inter.response.send_message("That tag doesn't exist.")
        # If the user selects info, it will show info about the tag
        elif action == "info":
            # Checks if the tag exists
            if os.path.exists(f"tags/{name}.json"):
                # Gets the tag info
                with open(f"tags/{name}.json", "r") as f:
                    tag = json.load(f)
                await inter.response.send_message(
                    f"Name: {tag['name']}\nContent: {tag['content']}"
                )
            else:
                await inter.response.send_message("That tag doesn't exist.")
                


                

        
def setup(bot):
    bot.add_cog(Tag(bot))
