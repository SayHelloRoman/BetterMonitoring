import asyncio
import pprint 

from bettermonitoring import Client


async def main():
    client = Client("TOKEN")
    server_count = 10000
    shard_count = 100
    await client.send_bot_stats(server_count, shard_count)


asyncio.run(main())