import os

import re

import asyncio

import time

from pyrogram import *

from pyrogram.types import *

os.system("apt install git curl python3-pip ffmpeg -y")

from FallenRobot import BOT_NAME, BOT_USERNAME, OWNER_ID, START_IMG, SUPPORT_CHAT, pbot

##Copy from here 

@pbot.on_message(filters.private & filters.command("clone"))

async def clone(bot: pbot, msg: Message):

    chat = msg.chat

    text = await msg.reply("Usage:\n\n /clone token")

    cmd = msg.command

    phone = msg.command[1]

    try:

        await text.edit("Starting Your Client")

                   # change this Directry according to ur repo

        pbot = Client(":memory:", bot_token=phone, plugins={"root": "handlers"})

        await client.start()

        idle()

        user = await client.get_me()

        await msg.reply(f"Your Client Has Been Successfully Started As @{user.username}! ✅ \n\nThanks for Cloning.")

    except Exception as e:

        await msg.reply(f"ERROR: {str(e)}\nPress /start to Start again.")

#End

##This code fit with every pyrogram Codes just import then @Client Xyz!

help = """

clone this bot

 â /clone *:* send me bot token from bot father"""

mod_name = "Cʟᴏɴᴇ"
