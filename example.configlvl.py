import disnake
from discordLevelingSystem import DiscordLevelingSystem, LevelUpAnnouncement, RoleAward

lvl = DiscordLevelingSystem()
lvl.connect_to_database_file(r'db/DiscordLevelingSystem.db')

nitro_booster = 00000000000000
associate_role = 00000000000000
lvlupchan = 00000000000000

embed = disnake.Embed()
embed.set_author(name=LevelUpAnnouncement.Member.name, icon_url=LevelUpAnnouncement.Member.avatar_url)
embed.description = f'Congrats {LevelUpAnnouncement.Member.mention}! You are now level {LevelUpAnnouncement.LEVEL} 😎'
announcement = LevelUpAnnouncement(embed, level_up_channel_ids=[lvlupchan])