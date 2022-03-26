<h1> BetterMonitoring </h1>

---

<div style="text-align: center">

![dm](https://img.shields.io/pypi/dm/bettermonitoring)

</div>

## Installation

---

Enter one of these commands to install the library:

```
pip install bettermonitoring
```

## Examples

You can find other examples in an examples folder.

**Discord.py auto send example**

```py
from discord.ext import tasks, commands

from bettermonitoring import Client


bot = commands.Bot(command_prefix="!")
client_bm = Client("token bettermonitoring")

@bot.event
async def on_ready() -> None:
    auto_send.start()

@tasks.loop(seconds=360)
async def auto_send():
    await client.send_bot_stats(len(bot.guilds), 0)


bot.run("bot token")
```