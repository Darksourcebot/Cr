import asyncio
from pyrogram import Client, filters
from random import choice
from pyrogram import filters
from strings import get_command
from strings.filters import command
from config import BANNED_USERS
from config.config import OWNER_ID
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.types import (InlineKeyboardButton,CallbackQuery,
                            InlineKeyboardMarkup, Message)
from YukkiMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from typing import Union
from pyrogram.types import InlineKeyboardButton
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove, Message, ChatJoinRequest

#كسمك تحياتي😂
REPLY_MESSAGE = "**🧑🏻‍✈️︙اهلا بك بك عزيزي المطور الاساسي ♥️**\n**⤵️︙ اليـكـ ازرار التحـكـم خاصة ب سورس الميوزك💞**"

REPLY_MESSAGE_BUTTONS = [
    [
        ("🐊 ¦ مطور السورس"),
    ],
    [
        ("✨ ¦ قناة السورس"),
    ],
    [
        ("⛔ ¦ المحظورين")
    ],
    [
        ("🍁 ¦ حظر"),
        ("🖇 ¦ الغاء حظر")
    ],
    [
        ("🔥 ¦ المحظورين عام")
    ],
    [
        ("🗞 ¦ حظر عام"),
        ("🔖 ¦ الغاء العام")
    ],
    [
        ("🪂 ¦ الاحصائيات"),
        ("📡 ¦ بينج السرفر")
    ],
    [
        ("⏹ ¦ يوتيوب")
    ],
    [
        ("❎ ¦ حذف الكيبورد")
    ]
]

@app.on_message(command("/vega") & filters.private & ~filters.edited)
async def madison(client: Client, message: Message): 
    text = REPLY_MESSAGE
    reply_markup = ReplyKeyboardMarkup(REPLY_MESSAGE_BUTTONS, one_time_keyboard=True, resize_keyboard=True)
    await message.reply(
        text=text,
        reply_markup=reply_markup
    )


@app.on_message(command("❎ ¦ حذف الكيبورد") & filters.private & ~filters.edited)
async def upbkgt(client: Client, message: Message):
    await message.reply_text(
        text="""❎ ¦ تم حذف الكيبورد بنجاح""",
        reply_markup=ReplyKeyboardRemove()
    )

@app.on_message(command("⛔ ¦ المحظورين") & filters.private & ~filters.edited)
async def upbkgt(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/89840a4c57675832debf9.jpg",
        caption=f"""• اليك طريقه معرفه المحظورين .\n\n• قم بـ استخدام الامر هكذا : /blockedusers المحظورين ميوزك\n\n• 𝑺𝑶𝑼𝑹𝑪𝑬 ⛧𝑪𝑹⛧⚡ » @SOURCE_CR .\n•⊶⊶★─⊶『[𝔼𝟛𝔻𝔸𝕄](https://t.me/SOURCE_CR)』⊶⊶★─⊶•""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "• 𝑺𝑶𝑼𝑹𝑪𝑬 ⛧𝑪𝑹⛧⚡ .", url=f"https://t.me/SOURCE_CR"),
            ],
            ]
        ),
    )

@app.on_message(command("🍁 ¦ حظر") & filters.private & ~filters.edited)
async def upbkgt(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/5dc0bab3462bd868b3081.jpg",
        caption=f"""• اليك طريقه حظر اي شخص .\n\n• قم بـ استخدام الامر هكذا : /block حظر ميوزك\n\n• 𝑺𝑶𝑼𝑹𝑪𝑬 ⛧𝑪𝑹⛧⚡ » @SOURCE_CR .\n•⊶⊶★─⊶『[𝔼𝟛𝔻𝔸𝕄](https://t.me/SOURCE_CR)』⊶⊶★─⊶•""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "• 𝑺𝑶𝑼𝑹𝑪𝑬 ⛧𝑪𝑹⛧⚡ .", url=f"https://t.me/SOURCE_CR"),
            ],
            ]
        ),
    )

@app.on_message(command("🖇 ¦ الغاء حظر") & filters.private & ~filters.edited)
async def upbkgt(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/4268ef332d710c5547357.jpg",
        caption=f"""• اليك طريقه الغاء حظر شخص .\n\n• قم بـ استخدام الامر هكذا : /unblock الغاء حظر ميوزك\n\n• 𝑺𝑶𝑼𝑹𝑪𝑬 ⛧𝑪𝑹⛧⚡ » @SOURCE_CR .\n•⊶⊶★─⊶『[𝔼𝟛𝔻𝔸𝕄](https://t.me/SOURCE_CR)』⊶⊶★─⊶•""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "• 𝑺𝑶𝑼𝑹𝑪𝑬 ⛧𝑪𝑹⛧⚡ .", url=f"https://t.me/SOURCE_CR"),
            ],
            ]
        ),
    )

@app.on_message(command("🔥 ¦ المحظورين عام") & filters.private & ~filters.edited)
async def upbkgt(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/cc2b0b6c4eea77c43b8b4.jpg",
        caption=f"""• اليك طريقه معرفه المحظورين عام .\n\n• قم بـ استخدام الامر هكذا : /blockedusers المحظورين ميوزك\n\n• 𝑺𝑶𝑼𝑹𝑪𝑬 ⛧𝑪𝑹⛧⚡ » @SOURCE_CR .\n•⊶⊶★─⊶『[𝔼𝟛𝔻𝔸𝕄](https://t.me/SOURCE_CR)』⊶⊶★─⊶•""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "• 𝑺𝑶𝑼𝑹𝑪𝑬 ⛧𝑪𝑹⛧⚡ .", url=f"https://t.me/SOURCE_CR"),
            ],
            ]
        ),
    )

@app.on_message(command("🗞 ¦ حظر عام") & filters.private & ~filters.edited)
async def upbkgt(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/d0db8351713f77bb8450b.jpg",
        caption=f"""• اليك طريقه الحظر العام .\n\n• قم بـ استخدام الامر هكذا :/ح ع\n\n• 𝑺𝑶𝑼𝑹𝑪𝑬 ⛧𝑪𝑹⛧⚡ » @SOURCE_CR .\n•⊶⊶★─⊶『[𝔼𝟛𝔻𝔸𝕄](https://t.me/SOURCE_CR)』⊶⊶★─⊶•""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "• 𝑺𝑶𝑼𝑹𝑪𝑬 ⛧𝑪𝑹⛧⚡ .", url=f"https://t.me/SOURCE_CR"),
            ],
            ]
        ),
    )

@app.on_message(command("🔖 ¦ الغاء العام") & filters.private & ~filters.edited)
async def upbkgt(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/611ee77edc1763ea2b07b.jpg",
        caption=f"""• اليك طريقه الغاء الحظر العام .\n\n• قم بـ استخدام الامر هكذا : /unblock الغاء حظر ميوزك\n\n• 𝑺𝑶𝑼𝑹𝑪𝑬 ⛧𝑪𝑹⛧⚡ » @SOURCE_CR .\n•⊶⊶★─⊶『[𝔼𝟛𝔻𝔸𝕄](https://t.me/SOURCE_CR)』⊶⊶★─⊶•""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "• 𝑺𝑶𝑼𝑹𝑪𝑬 ⛧𝑪𝑹⛧⚡ .", url=f"https://t.me/SOURCE_CR"),
            ],
            ]
        ),
    )

@app.on_message(command("🪂 ¦ الاحصائيات") & filters.private & ~filters.edited)
async def upbkgt(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/571e1fb1857c8ae6e6be1.jpg",
        caption=f"""• اليك طريقه معرفه الاحصائيات .\n\n• قم بـ استخدام الامر هكذا : الاحصائيات\n\n• 𝑺𝑶𝑼𝑹𝑪𝑬 ⛧𝑪𝑹⛧⚡ » @SOURCE_CR .\n•⊶⊶★─⊶『[𝔼𝟛𝔻𝔸𝕄](https://t.me/SOURCE_CR)』⊶⊶★─⊶•""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "• 𝑺𝑶𝑼𝑹𝑪𝑬 ⛧𝑪𝑹⛧⚡ .", url=f"https://t.me/SOURCE_CR"),
            ],
            ]
        ),
    )

@app.on_message(command("📡 ¦ بينج السرفر") & filters.private & ~filters.edited)
async def upbkgt(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/a9e24a3f58f9e8e2da866.jpg",
        caption=f"""• اليك طريقه معرفه سرعه البوت .\n\n• قم بـ استخدام الامر هكذا : بينج\n\n• 𝑺𝑶𝑼𝑹𝑪𝑬 ⛧𝑪𝑹⛧⚡ » @SOURCE_CR .\n•⊶⊶★─⊶『[𝔼𝟛𝔻𝔸𝕄](https://t.me/SOURCE_CR)』⊶⊶★─⊶•""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "• 𝑺𝑶𝑼𝑹𝑪𝑬 ⛧𝑪𝑹⛧⚡ .", url=f"https://t.me/SOURCE_CR"),
            ],
            ]
        ),
    )


@app.on_message(command("⏹ ¦ يوتيوب") & filters.private & ~filters.edited)
async def upbkgt(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/ae683f3b89e1a0566446b.jpg",
        caption=f"""• اليك طريقه معرفه اليوتيوب .\n\n• للبحث عن اغنيه اكتب . \n•  بحث + اسم الاغنيه\n•  تحميل + اسم الاغنيه\n• يوتيوب + اسم الاغنيه\n• 𝑺𝑶𝑼𝑹𝑪𝑬 ⛧𝑪𝑹⛧⚡ » @SOURCE_CR .\n\n•⊶⊶★─⊶『[𝔼𝟛𝔻𝔸𝕄](https://t.me/SOURCE_CR)』⊶⊶★─⊶•""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "• 𝑺𝑶𝑼𝑹𝑪𝑬 ⛧𝑪𝑹⛧⚡ .", url=f"https://t.me/SOURCE_CR"),
            ],
            ]
        ),
    )
