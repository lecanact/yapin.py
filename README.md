# yapper.py

Unofficial Python library for building bots on [Yapper](https://www.yapper.website/developers).

## Install

```bash
pip install yapper.py
```

## Quick start

```python
from dotenv import load_dotenv
import yapper

load_dotenv()

bot = yapper.Bot()  # reads YAPPER_BOT_TOKEN from env

@bot.command("ping", "Check if the bot is alive")
def ping(msg):
    msg.reply("pong")

@bot.on("member_join")
def welcome(ev):
    print(f"{ev.username} joined")

@bot.button("vote:")
def vote(i):
    i.ephemeral("You picked " + i.custom_id[5:])

bot.run()
```

Set `YAPPER_BOT_TOKEN` in your environment (token starts with `yb_`).

## Main concepts

- **Commands**: register slash/prefix commands with `@bot.command(...)`.
- **Events**: listen with `@bot.on("event_name")` or `@bot.event`.
- **Interactions**: handle button clicks with `@bot.button("prefix:")`.
- **Components**: build rows/buttons with `yapper.row(...)`, `yapper.btn(...)`, and `yapper.link_button(...)`.
- **Cogs/extensions**: split features into classes/files using `yapper.Cog`, `bot.add_cog(...)`, `bot.load_extension(...)`, and `bot.load_extensions(...)`.

## Useful bot methods

- Messaging: `send`, `edit`, `delete`, `react`
- Interactions: `respond`
- Server data: `servers`, `server`, `channels`, `members`, `roles`, `user`
- Moderation: `add_role`, `remove_role`, `kick`, `ban`, `unban`, `timeout`
- Presence/profile: `set_status`, `set_profile`

## API reference

Use the official Yapper developer docs for API payload details:
https://www.yapper.website/developers
