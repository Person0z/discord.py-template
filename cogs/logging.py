###############################################
#           Template made by Person0z         #
#          https://github.com/Person0z        #
#           Copyright© Person0z, 2022         #
#           Do Not Remove This Header         #
###############################################

# imports and stuff       
import os
import sqlite3
from datetime import datetime, timedelta
import disnake
from disnake.ext import commands
import config

class Logging(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.db_file = 'data/logging.db'
        self.channel_id = config.logs
        self.max_age_days = 7
        self.init_db()

    def init_db(self):
        conn = sqlite3.connect(self.db_file)
        c = conn.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS message_logs
                     (message_id INTEGER PRIMARY KEY, author_id INTEGER, content TEXT, attachments TEXT, timestamp REAL)''')
        conn.commit()
        conn.close()

    async def save_message_data(self, message):
        if message.author.bot:
            return

        now = datetime.utcnow()
        content = message.content
        attachment_urls = [attachment.url for attachment in message.attachments]
        conn = sqlite3.connect(self.db_file)
        conn.execute("PRAGMA journal_mode=WAL")  # Enable WAL
        c = conn.cursor()
        c.execute('''INSERT OR REPLACE INTO message_logs (message_id, author_id, content, attachments, timestamp) VALUES (?, ?, ?, ?, ?)''',
                (message.id, message.author.id, content, ",".join(attachment_urls), now.timestamp()))
        conn.commit()
        conn.close()

    async def delete_old_messages(self):
        cutoff_time = datetime.utcnow() - timedelta(days=self.max_age_days)

        conn = sqlite3.connect(self.db_file)
        c = conn.cursor()
        c.execute('''DELETE FROM message_logs WHERE timestamp < ?''', (cutoff_time.timestamp(),))
        conn.commit()
        conn.close()

    async def get_message_data(self, message_id):
        conn = sqlite3.connect(self.db_file)
        c = conn.cursor()
        c.execute('''SELECT author_id, content, attachments FROM message_logs WHERE message_id = ?''', (message_id,))
        row = c.fetchone()
        conn.close()

        if row:
            author_id, content, attachments = row
            return {
                'author_id': author_id,
                'content': content,
                'attachments': attachments.split(',') if attachments else []
            }
        return None

    @commands.Cog.listener()
    async def on_message(self, message):
#        print("New message:", message.content)
        await self.save_message_data(message)
        await self.delete_old_messages()

    @commands.Cog.listener()
    async def on_message_edit(self, before, after):
        if before.content == after.content:
            return

#        print("Message edited:", before.content, "=>", after.content)
        await self.save_message_data(after)
        await self.delete_old_messages()

        channel = self.bot.get_channel(self.channel_id)
        embed = disnake.Embed(title="Message edited", description=f"Message edited by {before.author.mention} in {before.channel.mention}:\nBefore: `{before.content}`\nAfter: `{after.content}`", color=0x00ff00)
        embed.set_footer(text=f"Message ID: {before.id}")
        await channel.send(embed=embed)

    @commands.Cog.listener()
    async def on_message_delete(self, message):
        if message.author.bot:
            return

        message_data = await self.get_message_data(message.id)

        if message_data:
            author_id = message_data['author_id']
            content = message_data['content']
            attachments = message_data['attachments']
            channel = self.bot.get_channel(self.channel_id)
            embed = disnake.Embed(title="Message deleted", description=f"Message deleted by <@{author_id}> in {message.channel.mention}:\n`{content}`", color=0xff0000)
            if attachments:
                embed.add_field(name="Attachments", value="\n".join(attachments))
            embed.set_footer(text=f"Message ID: {message.id}")
            await channel.send(embed=embed)
        else:
            channel = self.bot.get_channel(self.channel_id)
            embed = disnake.Embed(title="Message deleted", description=f"Message deleted by {message.author.mention} in {message.channel.mention}:\n`{message.content}`", color=0xff0000)
            embed.set_footer(text=f"Message ID: {message.id}")
            await channel.send(embed=embed)

    @commands.Cog.listener()
    async def on_raw_message_delete(self, payload):
        if payload.cached_message:
            return

        channel = self.bot.get_channel(self.channel_id)
        embed = disnake.Embed(title="Message deleted", description=f"Message deleted in <#{payload.channel_id}>:\nMessage ID: {payload.message_id}", color=0xff0000)
        await channel.send(embed=embed)

    @commands.Cog.listener()
    async def on_raw_message_edit(self, payload):
        if payload.cached_message:
            return
        if payload.data.get('author', {}).get('bot', False):
            return

        channel = self.bot.get_channel(self.channel_id)
        embed = disnake.Embed(title="Message edited", description=f"Message edited in <#{payload.channel_id}>:\nMessage ID: {payload.message_id}", color=0x00ff00)
        await channel.send(embed=embed)

def setup(bot):
    bot.add_cog(Logging(bot))