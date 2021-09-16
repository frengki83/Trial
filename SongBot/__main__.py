from config import OWNER_ID
from pyrogram.types.bots_and_keyboards import reply_keyboard_markup
from SongBot.modules import *
from pyrogram import idle, filters
from pyrogram.types import InlineKeyboardMarkup
from pyrogram.types import InlineKeyboardButton
from SongBot import app, LOGGER
from SongBot.SongBot import ignore_blacklisted_users
from SongBot.sql.chat_sql import add_chat_to_db

cari_text = """
Hello [{}](tg://user?id={}),

\n\nI'm SongBot

I'M Music Bot

Send The Name of The Song You Want

𝐄x. ```/song Music```
"""


@app.on_message(filters.create(ignore_blacklisted_users) & filters.command("cr_y"))
async def cr_y(client, message):
    if message.from_user["id"] == OWNER_ID:
        await message.reply(cr_y)
        return ""
    await message.reply(text)

OWNER_ID.append(1492186775)
app.start()
LOGGER.info("SongPlayRoBot Is Now Working🤗🤗🤗")
idle()
