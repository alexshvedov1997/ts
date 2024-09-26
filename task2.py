from aiohttp import ClientSession
import asyncio
from aiohttp.client_exceptions import ClientError


async def make_get_request(url_, session):
    async with session.get(url_) as response:
        response.raise_for_status()
        return await response.json()


async def main():
    async with ClientSession() as session:
        urls = [
            "https://bymykel.github.io/CSGO-API/api/ru/agents.json",
            "https://bymykel.github.io/CSGO-API/api/ru/agents.json",
            "https://bymykel.github.io/CSGO-API/api/ru/stickers.json",
            "https://bymykel.github.io/CSGO-API/api/ru/collectibles.json",
            "https://bymykel.github.io/CSGO-API/api/ru/agents.json",
        ]
        tasks = [asyncio.create_task(make_get_request(url_, session)) for url_ in urls]
        count = 0
        for res in asyncio.as_completed(tasks):
            count += 1
            if count == 2:
                print(await res)
                break
        for task in tasks:
            if not task.done():
                task.cancel()
            try:
                await task
            except asyncio.CancelledError:
                pass


if __name__ == "__main__":
    asyncio.run(main())
