import asyncio
import pprint 

from bettermonitoring import Client


async def main():
    client = Client()
    user_id = 389768884762312705
    info = await client.get_user_info(user_id)
    pprint.pprint(info)


asyncio.run(main())