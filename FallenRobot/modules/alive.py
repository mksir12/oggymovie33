from pyrogram import Client, filters, __version__ as pyrogram_version
import random 
from telethon import __version__ as telethon_version
from telegram import __version__ as ptbver
import time
StartTime = time.time()
from pyrogram.types import Message
from pyrogram.types.bots_and_keyboards.inline_keyboard_button import InlineKeyboardButton
from pyrogram.types.bots_and_keyboards.inline_keyboard_markup import InlineKeyboardMarkup
from info import SUPPORT_CHAT, BOT_USERNAME
from plugins.dev import get_readable_time
from pyrogram.types import CallbackQuery


@Client.on_message(filters.command("alive"))
async def alive(_, m: Message):
    user = m.from_user
    uptime = get_readable_time((time.time() - StartTime))
    msg = await m.reply_text("Initialising")
    await msg.edit("Initialising ✪●●●●●")
    time.sleep(1)
    await msg.edit("Initialising ✪✪●●●●")
    time.sleep(1)
    await msg.edit("Initialising ✪✪✪●●●")
    time.sleep(1)
    await msg.edit("Initialising ✪✪✪✪●●")
    time.sleep(1)
    await msg.edit("Initialising ✪✪✪✪✪●")
    time.sleep(1)
    await msg.edit("Initialising ✪✪✪✪✪✪")
    time.sleep(1)
    await msg.edit("✪︎Connection Successful✪")
    pm_caption = f"** ♡ Hey [{user.first_name}](tg://user?id={user.id}) \nI,m VijayTG ✨ **\n\n"
    pm_caption += f"**♡ My Uptime :** `{uptime}`\n\n"
    pm_caption += f"**♡ Telethon Version :** `{telethon_version}`\n\n"
    pm_caption += f"**♡ Pyrogram Version :** `{pyrogram_version}`\n\n"
    pm_caption += f"**♡ PTB Version :** `{ptbver}`\n\n"
    pm_caption += "**♡ My Master :** [Naveen-TG](https://t.me/Naveen_TG) "
    await msg.edit_text(text=(pm_caption),disable_web_page_preview=True)

           
