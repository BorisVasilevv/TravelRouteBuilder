import aiohttp
from config.enviroment import transport_url


async def get_transport(origin, destination, date, preferred_transport):
    url = transport_url
    headers = {'Content-Type': 'application/json'}
    payload = {
        "origin": origin,
        "destination": destination,
        "date": date,
        "preferred_transport": preferred_transport
    }

    async with aiohttp.ClientSession() as session:
        async with session.post(url, headers=headers, json=payload) as response:
            return await response.json()
