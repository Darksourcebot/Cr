import asyncio
from pyrogram import Client, filters
from datetime import datetime

@app.on_message(filters.member_joined)
async def get_chat_info(chat, already=False):
    if not already:
        chat = await app.get_chat(chat)
    chat_id = chat.id
    members = chat.members_count
	await message.reply_text(f"""
● نورت يقمر ♥♡
{message.from_user.first_name}
●  يجب احترام الادمنية
●  الالتزام بالقوانين في الوصف
●  الاعضاء  {members} 
""")


@app.on_message(filters.member_left)
async def leftmem(chat):
    await message.reply_text(f"""
    ★انت مش جدع يا «{ message.from_user.first_name}» 
★ ✞ حد يكون فى بار جامد زى ده ويخرج ❤️‍🔥🌚
✞ ده حتى كلنا اخوات يجدع ❤️‍🔥🌚
✞يلا في دهيه 🌚❤️‍🔥
√""")