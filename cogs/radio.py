###############################################
#           Template made by Person0z         #
#          https://github.com/Person0z        #
#           Copyright© Person0z, 2022         #
#           Do Not Remove This Header         #
###############################################

# Importing Libraries
import disnake
from disnake.ext import commands
import asyncio
import config

class Radio(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(name="radio", description="Play a radio station")
    async def radio(self, inter):
        channel = inter.author.voice.channel
        embed = disnake.Embed(title="Radio", description="Playing Heart London", color=disnake.Color.random())

        vc = await channel.connect()
        stream_url = config.radio
        vc.play(disnake.FFmpegPCMAudio(stream_url))

        embed.set_footer(text=f'Requested by {inter.author}', icon_url=inter.author.avatar.url)
        await inter.send(embed=embed)


    @commands.slash_command(name="pause", description="pause the radio")
    async def pause(self, inter):
        vc = inter.voice_client
        vc.pause()

    @commands.slash_command(name="resume", description="resume the radio")
    async def resume(self, inter):
        vc = inter.voice_client
        vc.resume()

#    @commands.slash_command(name="stop", description="stop the radio") # Don't Work yet, Working on a fix.
#    async def stop(self, inter):
#        vc = inter.voice_client
#        vc.stop()
#        await vc.disconnect()


def setup(bot):
    bot.add_cog(Radio(bot))
