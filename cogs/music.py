import disnake
from disnake.ext import commands
import config
import os
import youtube_dl

class music(commands.Cog):
    def __init__(self, bot):
    	self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f'Loaded Cog Music')

    @commands.slash_command(name="play", description="play music on youtube")
    async def play(self, inter: disnake.ApplicationCommandInteraction, name: int):
        embed = disnake.Embed(title=f"Successfully add music {name} to queue", color=config.Success())
        embed.set_footer(text=f'Set by {inter.author}', icon_url=inter.author.avatar.url)
        await inter.response.send_message(embed=embed)


        song_there = os.path.isfile("song.mp3")
        try:
            if song_there:
                os.remove("song.mp3")
        except PermissionError:
            em8 = disnake.Embed(title = "Music Is Currently Playing", description = 'Please wait for the current playing music to end or use %leave <:_Paimon6:827074349450133524>.\nMusic provided by {ctx.author.mention} <:_Paimon6:827074349450133524>',color = ctx.author.color)
            await inter.send(embed = em8)
            return

        voiceChannel = disnake.utils.get(inter.guild.voice_channels)
        await voiceChannel.connect()
        voice = disnake.utils.get(bot.voice_clients, guild=inter.guild)
        em6 = disnake.Embed(title = "Downloading Youtube Music", description = f'{url}\n\nPlease wait for paimon to setup the music you provide.\nMusic provided by {ctx.author.mention} <:_Paimon6:827074349450133524>',color = ctx.author.color)
        await inter.send(embed = em6, delete_after = 2)
        await inter.message.delete()

        ydl_opts = {
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '196',
            }],
        }
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        for file in os.listdir("./"):
            if file.endswith(".mp3"):
                os.rename(file, "song.mp3")
        voice.play(disnake.FFmpegPCMAudio("song.mp3"))
        em1 = disnake.Embed(title = "Now Listening Youtube Music", description = f'{url}\n\nPlease use %leave first to change music.\nMusic provided by {ctx.author.mention} <:_Paimon6:827074349450133524>',color = ctx.author.color)

        videoID = url.split("watch?v=")[1].split("&")[0]

        em1.set_thumbnail(url = f'https://img.youtube.com/vi/{videoID}/default.jpg'.format(videoID = videoID))
        await inter.send(embed = em1)

def setup(bot):
    bot.add_cog(music(bot))