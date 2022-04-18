import setuptools

setuptools.setup(
    name="antifishpy",                     # This is the name of the package
    version="1.1.0",                        # The initial release version
    author="Benjamin Churton",                     # Full name of the author
    description="A simple Python module for the Bitflow Anti-Fish API.",
    long_description="""# Bitflow Anti-Fish API

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
	
	# To get check for a matched domain, check for msg["match"] being True.
	# To get the domain trust rating, check msg["matches"][0]["trust_rating"].

	# You can also do af.is_scam(message), where it will return if there is a match and if the first domain match has a trust rating of over 0.95.

client.run("TOKEN")
```

## Credit where it's due

This module is powered by the [Bitflow Development's Anti-Fish API](https://anti-fish.bitflow.dev/).""",      # Long description read from the the readme file
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),    # List of all python modules to be installed
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],                                      # Information to filter the project on PyPi website
    python_requires='>=3.6',                # Minimum version requirement of the package
    py_modules=["antifishpy"],             # Name of the python package
    install_requires=["aiohttp"]                     # Install other dependencies if any
)
