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
	msg = af.check_message(message)
	print(msg)
	# This will return the API response seen at https://anti-fish.bitflow.dev
	
	# To get check for a matched domain, check for msg.match being True.
	# To get the domain trust rating, check msg.matches[0]["trust_rating"].

	# You can also do af.is_scam(), where it will check if there is a match and if the first domain match has a trust rating of over 0.95.

client.run("TOKEN")
```

## Credit where it's due

This module is powered by the [Bitflow Development's Anti-Fish API](https://anti-fish.bitflow.dev/).
