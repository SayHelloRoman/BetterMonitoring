import asyncio
import pprint 

from bettermonitoring import Client


async def main():
    client = Client()
    server_id = 951837171361407066
    info = await client.get_server_info(server_id)
    pprint.pprint(info)


asyncio.run(main())