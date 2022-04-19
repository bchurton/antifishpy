from aiohttp import ClientSession
from collections import namedtuple
from enum import Enum
import re

class DomainType(Enum):
    PHISHING = 0
    IP_LOGGER = 1

INITIAL_MATCH_REGEX = re.compile("(?:[A-z0-9](?:[A-z0-9-]{0,61}[A-z0-9])?\.)+[A-z0-9][A-z0-9-]{0,61}[A-z0-9]")

Matches = namedtuple("Matches", "followed domain source type trust_rating url is_scam")
AntiFishMatches = namedtuple("AntiFishMatches", "match matches is_scam")

def create_matches(data: dict) -> "Matches":
    data["type"] = DomainType.PHISHING if data["type"] == "PHISHING" else DomainType.IP_LOGGER
    data["is_scam"] = data["trust_rating"] >= 0.95
    
    return Matches(**data)

class antifish:
    __slots__ = ("session",)
    
    def __init__(self, application: str):
        self.session = ClientSession(headers={
            "User-Agent": f"{application} - via Antifish-py module"
        })
    
    def __repr__(self) -> str:
        return f"Antifish(\"{self.session.headers['User-Agent'][:-25]}\")"
    
    async def check_message(self, content: str) -> "AntiFishMatches":
        """ Checks the message. """
        
        if not INITIAL_MATCH_REGEX.search(content):
            return AntiFishMatches(False, None, False)

        async with self.session.get("https://anti-fish.bitflow.dev/check", json={ "message": content }) as response:
            json = await response.json()
            
            matches = [create_matches(m) for m in json.get("matches", [])]
            return AntiFishMatches(json["match"], matches or None, any(m.trust_rating >= 0.95 for m in matches))
    
    async def close(self):
        """ Closes the antifish instance. """
        if not self.session.closed:
            await self.session.close()
