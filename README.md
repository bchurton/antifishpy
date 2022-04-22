# Bitflow Anti-Fish API
This is a simple Python module for the [Bitflow Anti-Fish API](https://anti-fish.bitflow.dev/)!

## Installation
Use the package manager [pip](https://pypi.org/project/antifishpy/) to install this module.

```bash
pip install antifishpy
```

## Example
```python
from antifishpy import antifish
from collections import namedtuple
import asyncio

async def main():
    af = antifish("amogus application")
    
    # check a scam URL like the one below;
    res = await af.check_message("https://discord-nitro.com")
    
    print(res.match, res.is_scam)
    
    for m in res.matches:
        print(m.domain, m.url, m.trust_rating, m.is_scam)
    
    await af.close()

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
```

## Credit where it's due

This module is powered by the [Bitflow Development's Anti-Fish API](https://anti-fish.bitflow.dev/).
