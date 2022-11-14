

# Discord Python Bot Template

Discord Python Bot Template, for those looking for ideas or starting to learn Python!

Side note: This bot is going to improve in time, so as of now it may look very bad. However it will look and preform way better in the coming days!

## Features

- Slash Commands
- Prefix Used Commands
- Text to Image Generator
- Invite Command
- Fun Commands (Being worked on)

## Coming Soon

- Moderation
- Eco
- Thread support opener/closer
- Tickets
- + More

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
```

# How to run
The bot can be started with a python command:
```sh
python main.py
```
