from typing import Any, Dict, List, Union
from dataclasses import dataclass

import httpx


TEMPLATE_URL = "{}/{}"


@dataclass
class Bot:
    avatar: str
    botID: str
    username: str
    discrim: str
    shortDesc: str
    prefix: str
    votes: int
    ownerID: str
    coowners: List[str]
    tags: List[str]
    longDesc: str
    certificate: str
    github: str
    support: str
    website: str
    owner: str = ""


class HttpClient:
    base_url = "https://monitor.betterbot.ru/api"
    client = httpx.AsyncClient()

    async def make_request(
            self,
            method: str,
            endpoint: str,
            headers: Dict[str, Any] = {}
    ) -> Any:
        url = TEMPLATE_URL.format(self.base_url, endpoint)

        headers.update({
            "Content-Type": "application/json"
        })

        req = self.client.build_request(method, url, headers=headers)
        r = await self.client.send(req)

        return r.json()

    async def get_bot_info(self, bot_id: str) -> Union[Bot, bool]:
        json = await self.make_request("GET", f"bots/{bot_id}")
        if json.get("error") is None:
            return Bot(**json)

        return False

    async def send_bot_stats(self, server_count: int, shard_count: int) -> bool:
        json = await self.make_request(
            "GET",
            f"bots/stats",
            {
                "Authorization": self.token,	
                "serverCount": str(server_count),
                "shardCount": str(shard_count)
            }
        )

        return not isinstance(json.get("error"), str)


class Client(HttpClient):
    def __init__(self, token: str = "") -> None:
        self.token = token