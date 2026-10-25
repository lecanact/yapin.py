# yapin.py

Unofficial Python library for building bots on [Yapin'](https://www.yapin.gg/developers).

## Install

```bash
pip install yapin.py
```

## Quick start

```python
import yapin

bot = yapin.Bot()  # reads YAPIN_BOT_TOKEN from .env or you can do yapin.bot(token="yb_")

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

Set `YAPIN_BOT_TOKEN` in your environment (token starts with `yb_`).

## Main concepts

- **Commands**: register slash/prefix commands with `@bot.command(...)`.
- **Events**: listen with `@bot.on("event_name")` or `@bot.event`.
- **Interactions**: handle button clicks with `@bot.button("prefix:")`.
- **Components**: build rows/buttons with `yapin.row(...)`, `yapin.btn(...)`, and `yapin.link_button(...)`.
- **Cogs/extensions**: split features into classes/files using `yapin.Cog`, `bot.add_cog(...)`, `bot.load_extension(...)`, and `bot.load_extensions(...)`.

## Useful bot methods

- Messaging: `send`, `edit`, `delete`, `react`
- Interactions: `respond`
- Server data: `servers`, `server`, `channels`, `members`, `roles`, `user`
- Moderation: `add_role`, `remove_role`, `kick`, `ban`, `unban`, `timeout`
- Presence/profile: `set_status`, `set_profile`

## API reference

Use the official Yapin' developer docs for API payload details:
https://www.yapin.gg/developers
