import asyncio
import pprint 

from bettermonitoring import Client


async def main():
    client = Client("TOKEN")
    user_id = 389768884762312705
    vote = await client.check_vote_user(user_id)


asyncio.run(main())