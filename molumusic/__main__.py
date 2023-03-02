import asyncio
import importlib
import sys

from pyrogram import idle
from pytgcalls.exceptions import NoActiveGroupCall

import config
from config import BANNED_USERS
from molumusic import LOGGER, app, userbot
from molumusic.core.call import molu
from molumusic.plugins import ALL_MODULES
from molumusic.utils.database import get_banned_users, get_gbanned

loop = asyncio.get_event_loop()


async def init():
    if (
        not config.STRING1
        and not config.STRING2
        and not config.STRING3
        and not config.STRING4
        and not config.STRING5
    ):
        LOGGER("molumusic").error("Add Pyrogram string session and then try...")
    try:
        users = await get_gbanned()
        for user_id in users:
            BANNED_USERS.add(user_id)
        users = await get_banned_users()
        for user_id in users:
            BANNED_USERS.add(user_id)
    except:
        pass
    await app.start()
    for all_module in ALL_MODULES:
        importlib.import_module("molumusic.plugins" + all_module)
    LOGGER("molumusic.plugins").info("Necessary Modules Imported Successfully.")
    await userbot.start()
    await molu.start()
    try:
        await molu.stream_call("https://te.legra.ph/file/29f784eb49d230ab62e9e.mp4")
    except NoActiveGroupCall:
        LOGGER("molumusic").error(
            "[ERROR] - \n\nTurn on group voice chat and don't put it off otherwise I'll stop working thanks."
        )
        sys.exit()
    except:
        pass
    await molu.decorators()
    LOGGER("molumusic").info("Music Bot Started Successfully")
    await idle()


if __name__ == "__main__":
    loop.run_until_complete(init())
    LOGGER("molumusic").info("Stopping Music Bot")
