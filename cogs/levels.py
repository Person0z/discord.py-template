###############################################
#           Template made by Person0z         #
#        Levels Command Made by ๖̶̶̶ζ͜͡Zerbaib     #
#           https://github.com/Zerbaib        #
#          https://github.com/Person0z        #
#           Copyright© Person0z, 2022         #
#           Do Not Remove This Header         #
###############################################

import disnake
from disnake.ext import commands
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

    @bot.event
    async def on_message(message):
        await config.lvl.award_xp(amount=[15, 25], message=message, multiply=False)

    @bot.command()
    async def rank(ctx):
        data = await lvl.get_data_for(ctx.author)
        await ctx.send(f'You are level {data.level} and your rank is {data.rank}')

    @bot.command()
    async def leaderboard(ctx):
        data = await lvl.each_member_data(ctx.guild, sort_by='rank')

def setup(bot):
    bot.add_cog(level(bot))