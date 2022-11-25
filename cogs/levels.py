import disnake
from disnake.ext import commands
import discordLevelingSysteme
import config
import configlvl

class level(commands.Cogs):
    def __init__(self, bot):
    	self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f'Loaded Cog Levels')

    @bot.event
    async def on_message(message):
        await lvl.award_xp(amount=[15, 25], message=message, bonus=DiscordLevelingSystem.Bonus([nitro_booster, associate_role], 20, multiply=False))

def setup(bot):
    bot.add_cog(level())