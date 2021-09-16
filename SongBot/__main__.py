from config import OWNER_ID
from pyrogram.types.bots_and_keyboards import reply_keyboard_markup
from SongBot.modules import *
from pyrogram import idle, filters
from pyrogram.types import InlineKeyboardMarkup
from pyrogram.types import InlineKeyboardButton
from SongBot import app, LOGGER
from SongBot.SongBot import ignore_blacklisted_users
from SongBot.sql.chat_sql import add_chat_to_db

start_text = """
👋 𝗛𝗲𝗹𝗹𝗼 [{}](tg://user?id={}),

\n\n𝗜 𝗔𝗺 🎸𝐒𝐨𝐧𝐠 𝐏𝐥𝐚𝐲 𝐁𝐨𝐭[🎶](https://telegra.ph/file/6cb884fe1cb943ec12df1.mp4)

I'M Music Bot By @SongBot 🤖

𝗦𝗲𝗻𝗱 𝗧𝗵𝗲 𝗡𝗮𝗺𝗲 𝗢𝗳 𝗧𝗵𝗲 𝗦𝗼𝗻𝗴 𝗬𝗼𝘂 𝗪𝗮𝗻𝘁... 😍🥰🤗

𝐄x. ```/song Music```
"""

@app.on_message(filters.create(ignore_blacklisted_users) & filters.command("cr_y"))

LOGGER.info("SongPlayRoBot Is Now Working🤗🤗🤗")
idle()
