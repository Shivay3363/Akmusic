import requests
from BrandrdXMusic import app
import time
from pyrogram.enums import ChatAction, ParseMode
from pyrogram import filters
from MukeshAPI import api

@app.on_message(filters.text)
async def chat_gpt(bot, message):
    try:
        await bot.send_chat_action(message.chat.id, ChatAction.TYPING)
        name = message.from_user.first_name if message.from_user else "User"
        query = message.text
        keywords = ["hello", "hi", "how are you", "what is your name"]
        if any(keyword in query.lower() for keyword in keywords):
            response = api.gemini(query)["results"]
            await message.reply_text(f"{response}", parse_mode=ParseMode.MARKDOWN)
        else:
            await message.reply_text(f"Hello {name}, How can I help you today?")
    except Exception as e:
        await message.reply_text(f"Error: {e}")
