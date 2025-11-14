import base64
import re
import asyncio
from pyrogram import filters
from pyrogram.enums import ChatMemberStatus
from config import ADMINS, FORCE_SUB, FSUB_PIC
from database.fsub_db import get_fsub
from pyrogram.errors.exceptions.bad_request_400 import UserNotParticipant
from pyrogram.errors import FloodWait
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

        
async def encode(string):
    string_bytes = string.encode("ascii")
    base64_bytes = base64.urlsafe_b64encode(string_bytes)
    base64_string = (base64_bytes.decode("ascii")).strip("=")
    return base64_string

async def decode(base64_string):
    base64_string = base64_string.strip("=") # links generated before this commit will be having = sign, hence striping them to handle padding errors.
    base64_bytes = (base64_string + "=" * (-len(base64_string) % 4)).encode("ascii")
    string_bytes = base64.urlsafe_b64decode(base64_bytes) 
    string = string_bytes.decode("ascii")
    return string


def get_readable_time(seconds: int) -> str:
    count = 0
    up_time = ""
    time_list = []
    time_suffix_list = ["s", "m", "h", "days"]
    while count < 4:
        count += 1
        remainder, result = divmod(seconds, 60) if count < 3 else divmod(seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)
    hmm = len(time_list)
    for x in range(hmm):
        time_list[x] = str(time_list[x]) + time_suffix_list[x]
    if len(time_list) == 4:
        up_time += f"{time_list.pop()}, "
    time_list.reverse()
    up_time += ":".join(time_list)
    return up_time


async def force_sub(client, message):
    if FORCE_SUB == "False":
        return True

    if message.from_user.id in ADMINS:
        return True

    fsub_channel = await get_fsub()
    if not fsub_channel:
        return True

    try:
        await client.get_chat_member(fsub_channel['chat_id'], message.from_user.id)
    except UserNotParticipant:
        try:
            invite_link = await client.create_chat_invite_link(fsub_channel['chat_id'])
        except Exception as e:
            print(e)
            return False

        if FSUB_PIC:
            await message.reply_photo(
                photo=FSUB_PIC,
                caption="You must join our channel to use this bot.",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton("Join Channel", url=invite_link.invite_link)
                        ]
                    ]
                )
            )
        else:
            await message.reply_text(
                "You must join our channel to use this bot.",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton("Join Channel", url=invite_link.invite_link)
                        ]
                    ]
                )
            )
        return False

    return True
