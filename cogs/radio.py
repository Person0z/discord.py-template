import disnake
from disnake.ext import commands
import asyncio
import config

class Music(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command()
    async def radio(
        inter: disnake.ApplicationCommandInteraction,
        action: str = commands.Param(choices=["98.7 The Shark", "HeartFM", 'NPR']),
    ):

        stations = {
            "98.7 The Shark": "https://26313.live.streamtheworld.com/WPBBFMAAC.aac?apv=a2&source=webA2",
            "HeartFM": "http://media-ice.musicradio.com/HeartLondonMP3",
            "NPR": "https://npr-ice.streamguys1.com/live.mp3",
        }

        images = {
            "98.7 The Shark": "https://us-east-1.tixte.net/uploads/person0z.with-your.mom/WPBBFM_Logo.webp",
            "HeartFM": "https://us-east-1.tixte.net/uploads/person0z.with-your.mom/heart_400x400.jpg",
            "NPR": "https://us-east-1.tixte.net/uploads/person0z.with-your.mom/npr-national-public-radio-vector-logo-small.png",
        }

        if inter.author.voice is None:
            await inter.send("You are not in a voice channel.")
            return
        voice_client = inter.author.voice.channel.guild.voice_client
        if voice_client is None:
            await inter.author.voice.channel.connect()
            voice_client = inter.author.voice.channel.guild.voice_client
        if voice_client.is_playing():
            voice_client.stop()
        source = disnake.PCMVolumeTransformer(disnake.FFmpegPCMAudio(stations[action]))
        voice_client.play(source, after=lambda e: print(f'Player error: {e}') if e else None)


        embed = disnake.Embed(title="Radio", description=f"```Now playing {action} in {inter.author.voice.channel}```", color=disnake.Color.green())

        embed.set_thumbnail(url=images[action])
        embed.set_footer(text=f"Requested by {inter.author}", icon_url=inter.author.avatar.url)

        await inter.send(embed=embed)


def setup(bot):
    bot.add_cog(Music(bot))
