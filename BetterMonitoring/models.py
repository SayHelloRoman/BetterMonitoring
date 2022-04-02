from typing import List
from dataclasses import dataclass


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


@dataclass
class User:
    id: str
    biography: str
    website: str
    github: str
    twitter: str
    instagram: str


@dataclass
class Server:
    id: str
    avatar: str
    name: str
    owner: str
    shortDesc: str
    longDesc: str
    votes: int
    bumps: int
    tags: list


@dataclass
class Comment:
    author: str
    star_rate: str
    message: str
    date: float