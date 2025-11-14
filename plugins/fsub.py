from pyrogram import Client, filters
from pyrogram.types import Message
from config import OWNER_ID
from database.fsub_db import add_fsub, rm_fsub, get_fsub
from bot import Bot
from pyrogram.enums import ChatType

@Bot.on_message(filters.command('addfsub') & filters.user(OWNER_ID))
async def add_fsub_command(client: Bot, message: Message):
    if len(message.command) != 2:
        return await message.reply_text("Please provide a channel ID. Usage: /addfsub -100xxxxxxxx")

    try:
        channel_id = int(message.command[1])
    except ValueError:
        return await message.reply_text("Invalid channel ID. Please provide a valid integer.")

    try:
        chat = await client.get_chat(channel_id)
    except Exception as e:
        return await message.reply_text(f"Failed to access the chat. Make sure the bot is a member. Error: {e}")

    if chat.type not in [ChatType.CHANNEL, ChatType.SUPERGROUP]:
        return await message.reply_text(f"The provided ID is not a channel or supergroup. Detected type: {chat.type}")

    await add_fsub(channel_id)
    await message.reply_text(f"Successfully added {chat.title} as the force subscribe channel.")
@Bot.on_message(filters.command('rmfsub') & filters.user(OWNER_ID))
async def rm_fsub_command(client: Bot, message: Message):
    await rm_fsub()
    await message.reply_text("Successfully removed the force subscribe channel.")

@Bot.on_message(filters.command('fsub') & filters.user(OWNER_ID))
async def fsub_command(client: Bot, message: Message):
    fsub_channel = await get_fsub()
    if fsub_channel:
        try:
            chat = await client.get_chat(fsub_channel['chat_id'])
            await message.reply_text(f"Current force subscribe channel: {chat.title} ({fsub_channel['chat_id']})")
        except Exception as e:
            await message.reply_text(f"Error: {e}")
    else:
        await message.reply_text("No force subscribe channel is currently set.")
