import asyncio

import os
import time
import requests
from config import START_IMG_URL
from pyrogram import filters
import random
from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from strings.filters import command
from YukkiMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from YukkiMusic import app
from random import  choice, randint

#       #             #  #####  #####      ####
#        #           #  #         #            #     #
#          #        #  #####   #            #####     
#           #    #    #          #     ##    #     #
#              #       #####   ######   #     #
                
                
@app.on_message(
    command(["مطورين سي آر","المطورين","مطورين"])
    & ~filters.edited
)
async def huhh(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/185c4b44ed5e161403c1a.jpg",
        caption=f"""**⩹━★⊷━𝑺𝑶𝑼𝑹𝑪𝑬 ⛧𝑪𝑹⛧━⊶★━⩺**\nمرحبا بك عزيزي {message.from_user.mention} في قسم مطورين سي آر ميوزك\nللتحدث مع مطورين اضغط علي الازرار بالاسفل👇\n**⩹━★⊷━𝑺𝑶𝑼𝑹𝑪𝑬 ⛧𝑪𝑹⛧━⊶★━⩺**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "⎖᳒‏ 𝔼𝟛𝔻𝔸𝕄⌯‹♱༄►", url=f"https://t.me/DAD_E3DAM"), 
                 ],[
                    InlineKeyboardButton(
                        "𓆩ᯓ𝐂𝐇↯𓆪", url=f"https://t.me/YYIU4T"),
                    InlineKeyboardButton(
                        "SIR MONZER", url=f"https://t.me/BBlBFZ"),
                ],[
                
                    InlineKeyboardButton(
                        "★𝑺𝑶𝑼𝑹𝑪𝑬 ⛧𝑪𝑹⛧⚡", url=f"https://t.me/SOURCE_CR"),
                ],

            ]

        ),

    )








@app.on_message(
    command(["بودي العالمي","بودي","العالمي","مبرمج","ve"])
    & filters.group
    & ~filters.edited
)
async def yas(client, message):
    usr = await client.get_chat("ZI_EP")
    name = usr.first_name
    photo = await app.download_media(usr.photo.big_file_id)
    await message.reply_photo(photo,       caption=f"**⩹━★⊷━𝑺𝑶𝑼𝑹𝑪𝑬 ⛧𝑪𝑹⛧━⊶★━⩺\n\n🧞‍♂️ ¦𝙺𝙸𝙽𝙶 :{name}\n🎯 ¦𝚄𝚂𝙴𝚁 :@{usr.username}\n💣 ¦𝙸𝙳 :`{usr.id}`\n🚀 ¦𝙱𝙸𝙾 :{usr.bio}\n\n**⩹━★⊷━𝑺𝑶𝑼𝑹𝑪𝑬 ⛧𝑪𝑹⛧━⊶★━⩺**", 
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        name, url=f"https://t.me/{usr.username}")
                ],
            ]
        ),
    )
