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
import config
from helpers import errors


class tickets(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.tickets = []

    @commands.Cog.listener()
    async def on_ready(self):
        print(f'Loaded Cog Tickets')

    # Slash command for tickets which has options of opening a ticket, closing a ticket, and deleting a ticket

    @commands.slash_command()
    async def ticket(
        self,
        inter: disnake.ApplicationCommandInteraction,
        action: str = commands.Param(choices=["open", "close", "add", "remove"]),
        user: disnake.User = commands.Param(None, description="The user you want to add to the ticket")
    ):
        try:
            # If the user selects open, it will create a ticket
            if action == "open":
                if inter.author.id in self.tickets:
                    _channel: disnake.TextChannel = disnake.utils.get(
                        inter.guild.text_channels, name=f"ticket-{inter.author.name}")
                    if _channel:
                        embed = disnake.Embed(description=f"You already have a ticket opened. {_channel.mention}")
                    else:
                        embed = disnake.Embed(description="You already have a ticket opened.")
                    return await inter.send(embed=embed, delete_after=10.0)

                # Creates a ticket category if it doesn't exist
                if not disnake.utils.get(inter.guild.categories, name="Tickets"):
                    await inter.guild.create_category("Tickets")
                    
                # Creates the ticket channel
                channel = await inter.guild.create_text_channel(
                    name=f"ticket-{inter.author.name}",
                    category=disnake.utils.get(inter.guild.categories, name="Tickets"),
                    topic=f"Ticket created by {inter.author.name} | {inter.author.id} Time Created: {inter.created_at}",
                    reason=f"Ticket created by {inter.author.name}",
                )
                self.tickets.append(inter.author.id)
                # Sets the permissions for the ticket channel
                await channel.set_permissions(inter.author, send_messages=True, read_messages=True, read_message_history=True, attach_files=True, embed_links=True, add_reactions=True, external_emojis=True, use_external_emojis=True, use_slash_commands=True)
                await channel.set_permissions(inter.guild.default_role, send_messages=False, read_messages=False)
                
                # Sends a message to the ticket channel
                embed = disnake.Embed(title=f'Welcome to {inter.guild.name}, How may we help you?', description=f'Thank you for contacting {inter.guild.name}\'s support. Please list your issue or concerns while you wait for staff to come assist you today!')
                embed.set_footer(text=f'Command executed by {inter.author}', icon_url=inter.author.avatar.url)
                embed.set_thumbnail(url=inter.author.avatar.url)
                await channel.send(embed=embed)
                await channel.send(f'{inter.author.mention}', delete_after=0.1)

                # Sends a message to the user
                embed = disnake.Embed(title='Ticket Created', description=f"Your ticket has been created at {channel.mention} \n Please go to your ticket and list your issues / concerns", color=0x00FF00)
                embed.set_footer(text=f'Command executed by {inter.author}', icon_url=inter.author.avatar.url)
                embed.set_thumbnail(url=inter.author.avatar.url)
                await inter.response.send_message(embed=embed, ephemeral=True)

            # If the user selects close, it will close the ticket
            elif action == "close":
                async def close_ticket():
                    channel = disnake.utils.get(inter.guild.channels, name=f"ticket-{inter.author.name}")
                    transcript_channel = disnake.utils.get(inter.guild.channels, name="transcript")
                    if not transcript_channel:
                        category = disnake.utils.get(inter.guild.categories, name="Tickets")
                        if not category:
                            category = await inter.guild.create_category("Tickets")
                        transcript_channel = await inter.guild.create_text_channel("transcript", category=category)
                        overwrite = disnake.PermissionOverwrite()
                        overwrite.read_messages = False
                        await transcript_channel.set_permissions(inter.guild.default_role, overwrite=overwrite)
                    if inter.channel.name.startswith("ticket-"):
                        messages = []
                        async for message in inter.channel.history(limit=None):
                            if message.author.id == inter.guild.me.id:
                                continue
                            reply = ''
                            if message.reactions:
                                reply = f"(Reacted to by {[str(r.users) for r in message.reactions][0]})"
                            messages.append(f"{message.author} ({message.author.id}): {message.content} {reply}")
                        messages = messages[::-1]
                        transcript_file_name = f"transcript-ticket-{inter.author.name}.txt"
                        with open(transcript_file_name, "w") as f:
                            f.write("\n".join(messages))
                        await transcript_channel.send(file=disnake.File(transcript_file_name))
                        await inter.channel.delete()
                        os.remove(transcript_file_name)
                    if inter.author.id in self.tickets:
                        self.tickets.remove(inter.author.id)
                    else:
                        await inter.response.send_message("You don't have a ticket open.")

                await inter.response.defer()
                asyncio.create_task(close_ticket())
            
            # If the user selects add, it will add a user to the ticket Ex: /ticket action:add user:Person0z
            elif action == "add":
                channel = disnake.utils.get(
                    inter.guild.channels, name=f"ticket-{inter.author.name}")
                if inter.channel.name.startswith("ticket-"):
                    await channel.set_permissions(inter.user, send_messages=True, read_messages=True)
                    await inter.response.send_message(f"{user.mention} has been added to the ticket.")
                else:
                    await inter.response.send_message("You don't have a ticket open.")

            # If the user selects remove, it will remove a user from the ticket Ex: /ticket action:remove user:Person0z
            elif action == "remove":
                if inter.channel.name.startswith("ticket-"):
                    await inter.channel.set_permissions(user, send_messages=False, read_messages=False)
                    await inter.response.send_message(f"{user.mention} has been removed from the ticket.")
                else:
                    await inter.response.send_message("You don't have a ticket open.")

        except Exception as e:
            print(f'Error in ticket: {e}')


def setup(bot):
    bot.add_cog(tickets(bot))
