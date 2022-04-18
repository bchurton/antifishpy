import aiohttp
import re

class antifish:
    def __init__(self, application):
        self.application = application
    
    async def check_message(self, message):
        if not self.application:
            raise Exception("You haven't set your application! Please do `af = antifish('Application name | Application link')` so we can send this info as the User-Agent header.")

        if len(self.application) < 1:
            raise Exception("You haven't set your application! Please do `af = antifish('Application name | Application link')` so we can send this info as the User-Agent header.")

        if not re.search("(?:[A-z0-9](?:[A-z0-9-]{0,61}[A-z0-9])?\.)+[A-z0-9][A-z0-9-]{0,61}[A-z0-9]", message.content):
            return { "match": False }

        headers = {
            "User-Agent":f"{self.application} - via Antifish-py module"
        }

        async with aiohttp.ClientSession(headers=headers) as session:
            async with session.get("https://anti-fish.bitflow.dev/check", json={ "message":message.content }) as response:
                return await response.json()
        
    async def is_scam(self, message):
        if not self.application:
            raise Exception("You haven't set your application! Please do `af = antifish('Application name | Application link')` so we can send this info as the User-Agent header.")

        if len(self.application) < 1:
            raise Exception("You haven't set your application! Please do `af = antifish('Application name | Application link')` so we can send this info as the User-Agent header.")

        if not re.search("(?:[A-z0-9](?:[A-z0-9-]{0,61}[A-z0-9])?\.)+[A-z0-9][A-z0-9-]{0,61}[A-z0-9]", message.content):
            return { "match": False }

        headers = {
            "User-Agent":f"{self.application} - via Antifish-py module"
        }

        async with aiohttp.ClientSession(headers=headers) as session:
            async with session.get("https://anti-fish.bitflow.dev/check", json={ "message":message.content }) as response:
                res = await response.json()
                if res["match"] is True and res["matches"][0]["trust_rating"] >= 0.95:
                    return { "match":True, "match":{ "followed":res["matches"][0]["followed"], "domain":res["matches"][0]["domain"], "source":res["matches"][0]["source"], "type":res["matches"][0]["type"], "trust_rating":res["matches"][0]["trust_rating"] } }
                else:
                    return { "match":False }
        