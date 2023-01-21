import disnake
from disnake.ext import commands
import asyncio
import config

class Radio(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.Cog.listener()
    async def on_ready(self):
        print(f'Loaded Cog Radio')
        
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
        action: str = commands.Param(choices=["98.7 The Shark", "HeartFM", '106.1 KISS FM', "HOT 99.5", 'NPR']),
    ):
        stations = {
            "98.7 The Shark": "https://26313.live.streamtheworld.com/WPBBFMAAC.aac?apv=a2&source=webA2",
            "HeartFM": "http://media-ice.musicradio.com/HeartLondonMP3",
            "106.1 KISS FM": "https://ample.revma.ihrhls.com/zc2245/22_13dmvikifum3q02/playlist.m3u8?zip=75002&callLetters=KHKS-FM&country=US&streamid=2245&site-url=https%3A%2F%2Fwww.iheart.com%2Flive%2F1061-kiss-fm-2245%2F&dist=iheart&partnertok=eyJraWQiOiJpaGVhcnQiLCJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJsc2lkIjoiY29va2llOmEzOTUyMzczLWQ4MjgtNDQ1MC05NDU1LTUyNGFjZDQ3MTcxMyIsImF1ZCI6InRkIiwic3ViIjoiMTc2MzE4NTkwOSIsImNvcHBhIjowLCJpc3MiOiJpaGVhcnQiLCJ1c19wcml2YWN5IjoiMVlOTiIsImRpc3QiOiJpaGVhcnQiLCJleHAiOjE2NzM5MTkxNTIsImlhdCI6MTY3MzgzMjc1Miwib21pZCI6MH0.F5O5DYz6W4uwlBrr11DFMe1htqO1azgYG63aiYPYNz4&terminalid=159&locale=en-US&clientType=web&modTime=1673905997795&profileid=1763185909&triton-uid=cookie%3Ac05e0a92-568f-48ad-8ec1-2037e3dbda5f&host=webapp.US&us_privacy=1-N-&devicename=web-desktop&subscription_type=free&territory=US&stationid=2245",
            "HOT 99.5": "https://stream.revma.ihrhls.com/zc2509/hls.m3u8?streamid=2509&zip=&aw_0_1st.playerid=iHeartRadioWebPlayer&aw_0_1st.skey=6549968366&clientType=web&companionAds=false&deviceName=web-mobile&dist=iheart&host=webapp.US&listenerId=&playedFrom=157&pname=live_profile&profileId=6549968366&stationid=2509&terminalId=159&territory=US",
            "NPR": "https://npr-ice.streamguys1.com/live.mp3",
        }

        images = {
            "98.7 The Shark": "https://us-east-1.tixte.net/uploads/person0z.with-your.mom/WPBBFM_Logo.webp",
            "HeartFM": "https://us-east-1.tixte.net/uploads/person0z.with-your.mom/heart_400x400.jpg",
            "106.1 KISS FM": "https://us-east-1.tixte.net/uploads/person0z.with-your.mom/logod.webp",
            "HOT 99.5": "https://us-east-1.tixte.net/uploads/person0z.with-your.mom/hiot.png",
            "NPR": "https://us-east-1.tixte.net/uploads/person0z.with-your.mom/npr-national-public-radio-vector-logo-small.png",
        }

        if inter.author.voice is None:
            embed = disnake.Embed(title="Radio", description="```You are not in a voice channel.```", color=disnake.Color.red())
            await inter.send(embed=embed)
            return
        voice_client = inter.author.voice.channel.guild.voice_client
        if voice_client is None:
            await inter.author.voice.channel.connect()
            voice_client = inter.author.voice.channel.guild.voice_client
        if voice_client.is_playing():
            voice_client.stop()
        source = disnake.PCMVolumeTransformer(disnake.FFmpegPCMAudio(stations[action]))
        voice_client.play(source, after=lambda e: print(f'Player error: {e}') if e else None)


        embed = disnake.Embed(title="Radio | Connect", description=f"```Now playing {action} in {inter.author.voice.channel}```", color=disnake.Color.green())

        embed.set_thumbnail(url=images[action])
        embed.set_footer(text=f"Requested by {inter.author}", icon_url=inter.author.avatar.url)

        await inter.send(embed=embed)

    @commands.slash_command(name="disconnect", description="Disconnects the bot from the voice channel")
    async def disconnect(inter: disnake.ApplicationCommandInteraction):
        voice_client = inter.guild.voice_client
        if voice_client is None:
            embed = disnake.Embed(title="Radio | Disconnect", description="```I am not currently connected to any voice channels.```", color=disnake.Color.red())
            embed.set_footer(text=f"Requested by {inter.author}", icon_url=inter.author.avatar.url)
            embed.set_thumbnail(url=inter.guild.me.avatar.url)
            await inter.send(embed=embed)
        else:
            await voice_client.disconnect()
            embed = disnake.Embed(title="Radio | Disconnect", description="```I have successfully disconnected from the voice channel.```", color=disnake.Color.green())
            embed.set_footer(text=f"Requested by {inter.author}", icon_url=inter.author.avatar.url)
            embed.set_thumbnail(url=inter.guild.me.avatar.url)
            await inter.send(embed=embed)

def setup(bot):
    bot.add_cog(Radio(bot))
