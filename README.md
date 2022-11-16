

# Discord Python Bot Template

Discord Python Bot Template, for those looking for ideas or starting to learn Python!

Side note: This bot is going to improve in time, so as of now it may look very bad. However it will look and preform way better in the coming days!

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
status = 'Made By Person0z'

# Colors
Success = disnake.Color.green
Error = disnake.Color.red
Random = disnake.Color.random

# Owner ID
owner_ids = [000000000000000, 000000000000000] # You can add more owner ids by adding a comma and the id

# Welcomes & Goodbyes Channel ID
welcome_channel = 000000000000000000
```

# How to run
The bot can be started with a python command:
```sh
python main.py
```
