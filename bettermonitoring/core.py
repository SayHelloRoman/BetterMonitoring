from typing import Any, Dict, List, Union, Optional

import httpx

from .models import Bot, User, Server, Comment

TEMPLATE_URL = "{}/{}"


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

    async def get_bot_info(self, bot_id: str) -> Optional[Bot]:
        json = await self.make_request(
            "GET",
            f"bots/{bot_id}"
        )

        if json.get("error") is None:
            return Bot(**json)

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

    async def check_vote_user(self, user_id: int) -> bool:
        json = await self.make_request(
            "GET",
            f"bots/check/{user_id}",
            {
                "Authorization": self.token
            }
        )

        return json["vote"]
    
    async def get_bot_comments(self, bot_id: int) -> List[Comment]:
        json = await self.make_request(
            "GET",
            f"bots/{bot_id}/comments"
        )

        if json.get("error") is None:
            return list(
                map(
                    lambda i: Comment(**i),
                    json
                )
            )
    
    async def get_user_info(self, user_id: int) -> Optional[User]:
        json = await self.make_request(
            "GET",
            f"profile/{user_id}"
        )

        if json.get("error") is None:
            return User(**json)
    
    async def get_server_info(self, server_id: int) -> Optional[Server]:
        json = await self.make_request(
            "GET",
            f"server/{server_id}"
        )

        if json.get("error") is None:
            return Server(**json)


class Client(HttpClient):
    def __init__(self, token: str = "") -> None:
        self.token = token