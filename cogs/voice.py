###############################################
#           Template made by Person0z         #
#          https://github.com/Person0z        #
#           Copyright© Person0z, 2022         #
#           Do Not Remove This Header         #
###############################################

import json
import typing
import disnake
from disnake.ext import commands
import asyncio
import config
from helpers import errors

class voice(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f'Loaded Cog voice')

    # Deafen on join
    @commands.Cog.listener()
    async def on_voice_state_update(self, member, before, after, **kwargs):
        if member == self.bot.user and before.deaf != after.deaf and not after.deaf:
            await member.edit(deafen=True)

    # Deafen + play/pause
    @commands.Cog.listener()
    async def on_voice_state_update(self, member, before, after, **kwargs):
        if member == self.bot.user and before.deaf != after.deaf and not after.deaf:
            await member.edit(deafen=True)
        if after.channel is None:
            channel = self.bot.get_channel(before.channel.id)
        else:
            channel = self.bot.get_channel(after.channel.id)
        voice_client = channel.guild.voice_client

        if voice_client and voice_client.channel.id == channel.id:
            users_in_channel = [m for m in channel.members if not m.bot]
            if not users_in_channel:
                if voice_client.is_playing():
                    voice_client.pause()
            else:
                if voice_client.is_paused():
                    voice_client.resume()

    @commands.slash_command()
    async def radio(
        inter: disnake.ApplicationCommandInteraction,
        region: typing.Literal["US", "UK", "FR"],
        action: str
    ):
        try:
            stations = open("data/stations.json")
            _stations = json.load(stations)
            if inter.author.voice is None:
                embed = disnake.Embed(
                    title="Radio", description="```You are not in a voice channel.```", color=disnake.Color.red())
                return await inter.send(embed=embed)

            voice_client = inter.author.voice.channel.guild.voice_client

            if voice_client is None:
                await inter.author.voice.channel.connect()
                voice_client = inter.author.voice.channel.guild.voice_client

            if voice_client.is_playing():
                voice_client.stop()

            source = disnake.PCMVolumeTransformer(
                disnake.FFmpegPCMAudio(_stations[f"{region}_Stations"][action]))
            voice_client.play(source, after=lambda e: print(
                f'Player error: {e}') if e else None)

            embed = disnake.Embed(
                title="Radio | Connect", description=f"```Now playing {action} in {inter.author.voice.channel}```", color=disnake.Color.green())

            embed.set_thumbnail(url=_stations[f"{region}_Images"][action])
            embed.set_footer(
                text=f"Requested by {inter.author}", icon_url=inter.author.avatar.url)

            await inter.send(embed=embed)
        except Exception as e:
            print(f'Error sending radio message: {e}')
            await inter.send(embed=errors.create_error_embed(f"Error sending radio command: {e}"))

    @radio.autocomplete('action')
    async def radio_audiocomplete(self, inter: disnake.ApplicationCommandInteraction, action: str):
        try:
            stations = []
            region = inter.filled_options["region"]
            with open("data/stations.json") as f:
                data = json.load(f)
                for i in data[f"{region}_Stations"]:
                    if action in i:
                        stations.append(i)
            return stations
        except Exception as e:
            print(f'Error sending radio autocomplete: {e}')
            
    @commands.slash_command(name="disconnect", description="Disconnects the bot from the voice channel")
    async def disconnect(inter: disnake.ApplicationCommandInteraction):
        try:
            voice_client = inter.guild.voice_client
            if voice_client is None:
                embed = disnake.Embed(
                    title="Radio | Disconnect", description="```I am not currently connected to any voice channels.```", color=disnake.Color.red())
                embed.set_footer(
                    text=f"Requested by {inter.author}", icon_url=inter.author.avatar.url)
                embed.set_thumbnail(url=inter.guild.me.avatar.url)
                await inter.send(embed=embed)
            else:
                await voice_client.disconnect()
                embed = disnake.Embed(
                    title="Radio | Disconnect", description="```I have successfully disconnected from the voice channel.```", color=disnake.Color.green())
                embed.set_footer(
                    text=f"Requested by {inter.author}", icon_url=inter.author.avatar.url)
                embed.set_thumbnail(url=inter.guild.me.avatar.url)
                await inter.send(embed=embed)
        except Exception as e:
            print(f'Error sending disconnect command: {e}')
            
    @commands.slash_command(name="volume", description="volume of the bot")
    async def volume(self, ctx, volume: int):
        try:
            guild = ctx.guild
            voice_client = guild.voice_client
            if voice_client is None:
                return await ctx.send("Not connected to a voice channel.")
            if volume > 100:
                volume = 100
                await ctx.send("Volume cannot be set higher than 100.")
            voice_client.source.volume = volume / 100
            message = await ctx.send(f"Changed volume to {volume}%")
            await asyncio.sleep(10)
            await message.edit(content=f"Changed volume to {volume}%")
        except Exception as e:
            print(f'Error sending volume command: {e}')
            await ctx.send(f"Error sending volume command: {e}")

def setup(bot):
    bot.add_cog(voice(bot))