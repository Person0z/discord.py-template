import disnake
from disnake.ext import commands
import os

class tickets(commands.Cog):
    
    def __init__(self, bot):
    	self.bot = bot
        
    @commands.Cog.listener()
    async def on_ready(self):
        print(f'Loaded Cog Tickets')
        

    # Ticket Category
    @commands.Cog.listener()
    async def on_guild_channel_create(self, channel):
        if channel.name.startswith('ticket-'):
            category = disnake.utils.get(channel.guild.categories, name='Tickets')
            await channel.edit(category=category)
   
    # Ticket Creation Slash Command 
    @commands.slash_command(name='ticket', description='Create a ticket')
    async def ticket(self, inter):
        guild = inter.guild
        channel = await guild.create_text_channel(f'ticket-{inter.author.name}')
        await channel.set_permissions(inter.author, send_messages=True, read_messages=True)
        await channel.set_permissions(inter.guild.default_role, send_messages=False, read_messages=False)
        await channel.send(f'{inter.author.mention} Welcome to your ticket! Please wait for a staff member to help you!')
        await inter.send(f'Your ticket has been created at {channel.mention}')

    # Close Ticket Slash Command
    @commands.slash_command(name='close', description='Close a ticket')
    async def close(self, inter):
        if inter.channel.name.startswith('ticket-'):
            await inter.channel.delete()
            await inter.send('Ticket has been closed!')
        else:
            await inter.send('This is not a ticket!')

    # Add User To Ticket Slash Command
    @commands.slash_command(name='add', description='Add a user to a ticket')
    async def add(self, inter, user: disnake.Member):
        if inter.channel.name.startswith('ticket-'):
            await inter.channel.set_permissions(user, send_messages=True, read_messages=True)
            await inter.send(f'{user.mention} has been added to the ticket!')
        else:
            await inter.send('This is not a ticket!')

    # Remove User From Ticket Slash Command
    @commands.slash_command(name='remove', description='Remove a user from a ticket')
    async def remove(self, inter, user: disnake.Member):
        if inter.channel.name.startswith('ticket-'):
            await inter.channel.set_permissions(user, send_messages=False, read_messages=False)
            await inter.send(f'{user.mention} has been removed from the ticket!')
        else:
            await inter.send('This is not a ticket!')

    # List Users In Ticket Slash Command
    @commands.slash_command(name='list', description='List users in a ticket')
    async def list(self, inter):
        if inter.channel.name.startswith('ticket-'):
            await inter.send(f'Users in the ticket: {inter.channel.members}')
        else:
            await inter.send('This is not a ticket!')
    
    # Make a transcript of the ticket
    @commands.slash_command(name='transcript', description='Make a transcript of the ticket')
    async def transcript(self, inter):
        if inter.channel.name.startswith('ticket-'):
            messages = await inter.channel.history(limit=None).flatten()
            with open(f'{inter.channel.name}.txt', 'w') as f:
                for message in messages:
                    f.write(f'{message.author}: {message.content}\n')
            await inter.send(file=disnake.File(f'{inter.channel.name}.txt'))
            os.remove(f'{inter.channel.name}.txt')


    # Ticket Help Slash Command
    @commands.slash_command(name='tickethelp', description='Ticket Help')
    async def tickethelp(self, inter):
        embed = disnake.Embed(title='Ticket Help', description='Here are the commands for the ticket system!', color=0x00ff00)
        embed.add_field(name='/ticket', value='Create a ticket', inline=False)
        embed.add_field(name='/close', value='Close a ticket', inline=False)
        embed.add_field(name='/add', value='Add a user to a ticket', inline=False)
        embed.add_field(name='/remove', value='Remove a user from a ticket', inline=False)
        embed.add_field(name='/list', value='List users in a ticket', inline=False)
        await inter.send(embed=embed)

    # Make sures the user has only one ticket open at a time
    @commands.Cog.listener()
    async def on_guild_channel_create(self, channel):
        if channel.name.startswith('ticket-'):
            for c in channel.guild.channels:
                if c.name.startswith('ticket-') and c != channel:
                    await c.delete()

def setup(bot):
    bot.add_cog(tickets(bot))
