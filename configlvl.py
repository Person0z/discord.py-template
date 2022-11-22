import disnake
from discordLevelingSystem import DiscordLevelingSystem, LevelUpAnnouncement, RoleAward

# lvl create
lvlchan = 1043720420458774670

# lvl role boost
nitro_booster = 000000000000000
role1 = 000000000000000

lvl = DiscordLevelingSystem()

embed = disnake.Embed()
embed.set_author(name=LevelUpAnnouncement.Member.name, icon_url=LevelUpAnnouncement.Member.avatar_url)
embed.description = f'Congrats {LevelUpAnnouncement.Member.mention}! You are now level {LevelUpAnnouncement.LEVEL} 😎'
announcement = LevelUpAnnouncement(embed, level_up_channel_ids=lvlchan)

lvl = DiscordLevelingSystem(level_up_announcement=announcement, level_up_channel_ids=lvlchan)
lvl.connect_to_database_file(r'db\DiscordLevelingSystem.db')
