###############################################
#           Template made by Person0z         #
#          https://github.com/Person0z        #
#           Copyright© Person0z, 2022         #
#           Do Not Remove This Header         #
###############################################

# importing the required modules
import disnake
from disnake.ext import commands
import os
import asyncio

class tickets(commands.Cog):
    
    def __init__(self, bot):
    	self.bot = bot
        
    @commands.Cog.listener()
    async def on_ready(self):
        print(f'Loaded Cog Tickets')
        

#    @commands.slash_command()
#    async def blep(
#        inter: disnake.ApplicationCommandInteraction,
#        animal: str = commands.Param(choices=["Dog", "Cat", "Penguin"])
#    ):
#        await inter.response.send_message(animal)

    # Slash command for tickets which has options of opening a ticket, closing a ticket, and deleting a ticket
    @commands.slash_command()
    async def ticket(
        inter: disnake.ApplicationCommandInteraction,
        action: str = commands.Param(choices=["open", "close", "add"]),
        user: disnake.User = commands.Param(description="The user you want to add to the ticket")
    ):
        # If the user selects open, it will create a ticket
        if action == "open":
            # Creates a ticket category if it doesn't exist
            if not disnake.utils.get(inter.guild.categories, name="Tickets"):
                await inter.guild.create_category("Tickets")
            # Creates the ticket channel
            channel = await inter.guild.create_text_channel(
                name=f"ticket-{inter.author.name}",
                category=disnake.utils.get(inter.guild.categories, name="Tickets"),
                topic=f"Ticket for {inter.author.name}",
                reason=f"Ticket created by {inter.author.name}",
            )
            # Sets the permissions for the ticket channel
            await channel.set_permissions(inter.author, send_messages=True, read_messages=True)
            await channel.set_permissions(inter.guild.default_role, send_messages=False, read_messages=False)

            # Sends a message to the ticket channel
            await channel.send(
                f"Hello {inter.author.mention}, welcome to your ticket! Please wait for a staff member to help you."
            )
            # Sends a message to the user
            await inter.response.send_message(
                f"Your ticket has been created at {channel.mention}"
            )
        # If the user selects close, it will close the ticket
        elif action == "close":
            channel = disnake.utils.get(inter.guild.channels, name=f"ticket-{inter.author.name}")
            if inter.channel.name.startswith("ticket-"):
                await inter.channel.delete()
                await inter.response.send_message("Your ticket has been closed.")
            else:
                await inter.response.send_message("You don't have a ticket open.")
        # If the user selects add, it will add a user to the ticket Ex: /ticket action:add user:Person0z
        elif action == "add":
            channel = disnake.utils.get(inter.guild.channels, name=f"ticket-{inter.author.name}")
            if inter.channel.name.startswith("ticket-"):
                await channel.set_permissions(inter.user, send_messages=True, read_messages=True)
                await inter.response.send_message(f"{user.mention} has been added to the ticket.")
            else:
                await inter.response.send_message("You don't have a ticket open.")


def setup(bot):
    bot.add_cog(tickets(bot))
