
# Discord Python Bot Template

Discord Python Bot Template, for those looking for ideas or starting to learn Python!

Side Note: Please keep in mind this bot is still in the working, you will have bugs, code thats not clean (still will work), and updates every day. The bot is going to  improve. Just please give it time and hold on. Remeber nothong good comes fast.

## Features

- Slash Commands (Mostly everything has this)
- Prefix Used Commands (Used only for commands that owners should only have access too)
- Text to Image Generator (Finished)
- Invite Command (will be cleaned up and more info added on the embed)
- Fun Commands (Adding more soon, needs to be cleaned up)
- Moderation (adding more soon, not adding /ban, /kick as discord has that added already)
- Tickets (needs to be cleaned)

## Coming Soon
- Eco
- Thread support opener/closer
- Levels

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
```

# How to run
The bot can be started with a python command:
```sh
python main.py
```
or you can run start.bat/.sh