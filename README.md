
<h1 align="center">
  Discord Python Bot Template
</h1>

<p align="center">Discord Python Bot Template, for those looking for ideas or starting to learn Python!<p>
<p align="center">
  <a href="https://discord.gg/D8rjRN3uJQ"><img src="https://img.shields.io/discord/1054287234544713788?logo=discord"></a>
  <a href="//github.com/Person0z/discord.py-template"><img src="https://img.shields.io/github/repo-size/Person0z/discord.py-template"></a>
  <a href="//github.com/Person0z/discord.py-template/commits"><img src="https://img.shields.io/github/last-commit/Person0z/discord.py-template"></a>
  <a href="//github.com/Person0z/discord.py-template/contributors"><img src="https://img.shields.io/github/contributors/Person0z/discord.py-template"></a>
</p>

## Features

- Slash Commands (Slash commands: /help, /radio.. etc)
- Prefix Used Commands (Owners Only: !update. Updates the bot via git)
- Text to Image Generator (/generate: Generate a AI made image of whatever you want)
- Invite Command (will be cleaned up and more info added on the embed)
- Fun Commands (/help fun: Commands like 8ball, bitcoin etc if you wanna mess around.)
- Moderation (/ban, /warn, /kick.. etc: Smart warns - 3 warns = kick, 5 = ban.)
- Tickets (/tickets: needs to be redone)
- Radios (Play radio's from online sources)
- Pastebin (uploads files to a pastebin so you dont have to download files that you dont trust)

## Coming Soon
- better optimized code
- per server tags + warns
- logging messages + more
- Someway to make updating the bot faster

If you have suggestions on adding something, feel free to ask and or make a PR!

### Install the dependencies

```sh
pip install -r requirements.txt
```

### Setting up the bot properties

> When setting up the bot remove "example" from example.config.py!!

```python
# Imports
import disnake

# Discord Token
token = 'TOKEN'

# Version
version = '1.5.5'

# Your Discord Server ID Will Go Here 
guild = 'GUILD ID'

# The Prefix You Want For Your Discord Bot
prefix = '!'

# Bot Status
activity = ["/help", "discord.py", "With Python", "Made by Person0z", "v1.5.6"]

# Colors
Success = disnake.Color.green
Error = disnake.Color.red
Random = disnake.Color.random

# Owner ID
owner_ids = [000000000000000, 000000000000000] # You can add more owner ids by adding a comma and the id

# Welcomes & Goodbyes Channel ID
welcome_channel = 0000000000000000
join_role = 'Member' # The role you want to give to new members

# Logging Channel ID
logs = [0000000000000000] # You can add more channels by doing this: [channel_id, channel_id, channel_id]
```

# How to run
The bot can be started with a python command:
```sh
python main.py OR python3 main.py OR .sh/bat files
```

# Sponsers
[Zluqe, Experience hassle-free bot hosting with Zluqe. Our platform offers free hosting for both Python, Java and JavaScript bots, making it the one-stop solution for all your Discord needs.](https://zluqe.com/)
