import disnake
from disnake.ext import commands
import youtube_dl

class Music(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(name="play", description="Play a song.")
    async def play(self, ctx, *, url):
        voice_channel = ctx.author.voice.channel
        if voice_channel is None:
            return await ctx.send("You need to be in a voice channel to use this command.")

        vc = await voice_channel.connect()

        ydl_opts = {
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
        }

        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=False)
            title = info.get('title', None)
            filename = info.get('url', None)

        source = disnake.PCMVolumeTransformer(disnake.FFmpegPCMAudio(filename))
        ctx.vc.play(source)
        await ctx.send(f"Playing: {title}")

    @commands.slash_command(name="pause", description="Pauses the currently playing song.")
    async def pause(self, ctx):
        voice_client = ctx.voice_client

        if not voice_client:
            await ctx.send("Not connected to a voice channel.")
            return

        if not voice_client.is_playing():
            await ctx.send("Nothing playing.")
            return 

        voice_client.pause()
        await ctx.send("Paused the music.")

    @commands.slash_command(name="resume", description="Resumes the currently paused song.")
    async def resume(self, ctx):
        if not ctx.author.voice:
            await ctx.send("You need to be in a voice channel to use this command.")
            return
        
        # Check if the bot is connected to a voice channel
        if not self.bot.voice_clients:
            await ctx.send("The bot is not connected to a voice channel.")
            return

        # Resume the music
        voice_client = self.bot.voice_clients[0]
        if not voice_client.is_playing():
            voice_client.resume()
            await ctx.send("Music resumed.")
        else:
            await ctx.send("Music is already playing.")

    @commands.slash_command(name="stop", description="Stops the currently playing song.")
    async def stop(self, ctx):
        voice_client = ctx.voice_clients
        if voice_client is not None:
            await voice_client.disconnect()
            await ctx.send("Stop playing")
        else:
            await ctx.send("I'm not playing now")
        

def setup(bot):
    bot.add_cog(Music(bot))