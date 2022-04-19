from aiohttp import ClientSession
from collections import namedtuple
import re

INITIAL_MATCH_REGEX = re.compile("(?:[A-z0-9](?:[A-z0-9-]{0,61}[A-z0-9])?\.)+[A-z0-9][A-z0-9-]{0,61}[A-z0-9]")

Matches = namedtuple("Matches", "followed domain source type trust_rating")
AntiFishMatches = namedtuple("AntiFishMatches", "match matches is_scam")

class antifish:
    __slots__ = ("session",)
    
    def __init__(self, application: str):
        self.session = ClientSession(headers={
            "User-Agent": f"{application} - via Antifish-py module"
        })
    
    async def check_message(self, message):
        """ Checks the message. """
        
        if not INITIAL_MATCH_REGEX.search(message.content):
            return Matches(False, None, False)

        async with self.session.get("https://anti-fish.bitflow.dev/check", json={ "message": message.content }) as response:
            json = await response.json()
            
            matches = json.get("matches", [ None ])[0]
            is_scam = matches and json["match"] and matches["trust_rating"] >= 0.95
            
            return Matches(json["match"], Matches(**matches) if matches is not None else None, is_scam)
    
    async def close(self):
        """ Closes the antifish instance. """
        if not self.session.closed:
            await self.session.close()
