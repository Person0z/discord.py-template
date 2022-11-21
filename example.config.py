###############################################
#           Template made by Person0z         #
#          https://github.com/Person0z        #
#           Copyright© Person0z, 2022         #
#           Do Not Remove This Header         #
###############################################

# Imports
import disnake
from discordLevelingSystem import DiscordLevelingSystem

# Discord Token
token = 'TOKEN'

# Your Discord Server ID Will Go Here 
guild = 'GUILD ID'

# The Prefix You Want For Your Discord Bot
prefix = '!'

# Bot Status
activity = ["/help", "discord.py", "With Python", "Made by Person0z", "V.1.3-beta"]

# Colors
Success = disnake.Color.green
Error = disnake.Color.red
Random = disnake.Color.random

# Owner ID
owner_ids = [000000000000000, 000000000000000] # You can add more owner ids by adding a comma and the id

# Welcomes & Goodbyes Channel ID
welcome_channel = 0000000000000000

# lvl create
lvl = DiscordLevelingSystem(level_up_announcement=announcement)
lvlchan = 0000000000000000
lvl.connect_to_database_file(r'db\DiscordLevelingSystem.db')
# lvl role boost
nitro_booster = 000000000000000
role1 = 000000000000000