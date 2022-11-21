###############################################
#           Template made by Person0z         #
#        Levels Command Made by ๖̶̶̶ζ͜͡Zerbaib     #
#           https://github.com/Zerbaib        #
#          https://github.com/Person0z        #
#           Copyright© Person0z, 2022         #
#           Do Not Remove This Header         #
###############################################

import disnake
from disnake.ext import commands, tasks
from discordLevelingSystem import DiscordLevelingSystem, LevelUpAnnouncement, RoleAward
import os
import config

class level(commands.Cog):
    def __init__(self, bot):
    	self.bot = bot

    embed = disnake.Embed()
    embed.set_author(name=LevelUpAnnouncement.Member.name, icon_url=LevelUpAnnouncement.Member.avatar_url)
    embed.description = f'Congrats {LevelUpAnnouncement.Member.mention}! You are now level {LevelUpAnnouncement.LEVEL} 😎'
    announcement = LevelUpAnnouncement(embed, level_up_channel_ids=[config.lvlchan])

    @commands.Cog.listener()
    async def on_ready(self):
        print(f'Loaded Cog Levels')

    @commands.slash_command(name="rank", description="What is your levels!")
    async def rank(self, inter):
        data = await config.lvl.get_data_for(inter.author)
        await inter.send(f'You are level {data.level} and your rank is {data.rank}')

    @commands.slash_command(name="leaderboard", description="The leaderboard of the rank!")
    async def leaderboard(self, inter, ctx):
        data = await config.lvl.each_member_data(ctx.guild, sort_by='rank')
        await inter.send(data)

def setup(bot):
    bot.add_cog(level(bot))