import disnake

def create_error_embed(error_message: str):
    embed = disnake.Embed(title="Command Error", description=error_message, color=disnake.Color.red())
    return embed
