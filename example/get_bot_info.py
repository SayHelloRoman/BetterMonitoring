import asyncio
import pprint 

from bettermonitoring import Client


async def main():
    client = Client()
    info = await client.get_bot_info(869661490649645067)
    pprint.pprint(info)


asyncio.run(main())