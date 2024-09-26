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
            "https://bymykel.github.io/CSGO-API/apippp/ru/agents.json",
            "https://www.google.com/search?q=pip3+install+aiohttp",
            "https://bymykel.github.io/CSGO-API/api/ru/stickers.json",
            "https://bymykel.github.io/CSGO-API/api/ru/collectibles.json",
            "https://bymykel.github.io/CSGO-API/api/ru/agents.json",
        ]
        tasks = [make_get_request(url_, session) for url_ in urls]
        results = await asyncio.gather(*tasks, return_exceptions=True)
        count = 0
        for res in results:
            if isinstance(res,  ClientError):
                print("Res error {code} and {message}".format(code=res.code, message=res.message))
            elif isinstance(res, Exception):
                print("Error {error}".format(error=res))
            else:
                print(res)


if __name__ == "__main__":
    asyncio.run(main())