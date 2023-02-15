    ###############################################
#           Template made by Person0z         #
#          https://github.com/Person0z        #
#           Copyright© Person0z, 2022         #
#           Do Not Remove This Header         #
###############################################

import disnake
from disnake.ext import commands
import os
import config

class reaction(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
        self.ROLE_MESSAGE_ID = config.roleMSG  # message ID goes here
        self.EMOJI_TO_ROLE = {
            disnake.PartialEmoji(name="📢"): config.annoncement,  
            disnake.PartialEmoji(name="⬆️"): config.patchNote,
            disnake.PartialEmoji(name="💬"): config.inactiveChat,
            disnake.PartialEmoji(name="🎉"): config.givewayReact, 
        }



    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload: disnake.RawReactionActionEvent):
        """Gives a role based on a reaction emoji."""
        if payload.guild_id is None or payload.member is None:
            return

        # Make sure that the message the user is reacting to is the one we care about.
        if payload.message_id != self.ROLE_MESSAGE_ID:
            return

        guild = self.bot.get_guild(payload.guild_id)
        if guild is None:
            # Check if we're still in the guild and it's cached.
            return

        try:
            role_id = self.EMOJI_TO_ROLE[payload.emoji]
        except KeyError:
            # If the emoji isn't the one we care about then exit as well.
            return

        role = guild.get_role(role_id)
        if role is None:
            # Make sure the role still exists and is valid.
            return

        try:
            # Finally, add the role.
            await payload.member.add_roles(role)
        except disnake.HTTPException as e:
            print(f"Failed to add role {role.name} to {payload.member.display_name}: {e}")

    @commands.Cog.listener()
    async def on_raw_reaction_remove(self, payload: disnake.RawReactionActionEvent):
        """Removes a role based on a reaction emoji."""
        if payload.guild_id is None:
            return

        # Make sure that the message the user is reacting to is the one we care about.
        if payload.message_id != self.ROLE_MESSAGE_ID:
            return

        guild = self.bot.get_guild(payload.guild_id)
        if guild is None:
            # Check if we're still in the guild and it's cached.
            return

        try:
            role_id = self.EMOJI_TO_ROLE[payload.emoji]
        except KeyError:
            # If the emoji isn't the one we care about then exit as well.
            return

        role = guild.get_role(role_id)
        if role is None:
            # Make sure the role still exists and is valid.
            return

        # The payload for `on_raw_reaction_remove` does not provide `.member`
        # so we must get the member ourselves from the payload's `.user_id`.
        member = guild.get_member(payload.user_id)
        if member is None:
            # Make sure the member still exists and is valid.
            return

        try:
            # Finally, remove the role.
            await member.remove_roles(role)
        except disnake.HTTPException as e:
            print(f"Failed to remove role {role.name} from {member.display_name}: {e}")

def setup(bot):
    bot.add_cog(reaction(bot))