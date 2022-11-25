import disnake
import discordLevelingSysteme

lvl = DiscordLevelingSystem()
lvl.connect_to_database_file(r'db\DiscordLevelingSystem.db')

nitro_booster = 851379776111116329
associate_role = 851400453904400385
lvlupchan = 00000000000000

embed = discord.Embed()
embed.set_author(name=LevelUpAnnouncement.Member.name, icon_url=LevelUpAnnouncement.Member.avatar_url)
embed.description = f'Congrats {LevelUpAnnouncement.Member.mention}! You are now level {LevelUpAnnouncement.LEVEL} 😎'
announcement = LevelUpAnnouncement(embed, level_up_channel_ids=[lvlupchan])