# Bitflow Anti-Fish API
This is a simple Python module for the [Bitflow Anti-Fish API](https://anti-fish.bitflow.dev/)!

## Installation
Use the package manager [pip](https://pypi.org/project/antifishpy/) to install this module.

```bash
pip install antifishpy
```

## Examples

```python
from antifishpy import antifish
from discord.ext import commands

client = commands.Bot(command_prefix="!")
af = antifish("Your Bot Name | Application Link") # This is to pass your application name as the User-Agent header.

@client.event
async def on_message(message):
    msg = await af.check_message(message)

    # expect True or False.
    print(msg.match)

    # expect True or False. this returns True if the trust_rating threshold is >= 0.95.
    print(msg.is_scam)

    # the serialized first element of the "matches" array.
    print(msg.matches)

# use this when the bot is about to exit! (highly recommended)
async def some_exit_function():
    await af.close()

client.run("TOKEN")
```

## Credit where it's due

This module is powered by the [Bitflow Development's Anti-Fish API](https://anti-fish.bitflow.dev/).
