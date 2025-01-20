import os
from telegram import Bot
from telegram.error import TelegramError

BOT_TOKEN = '8038716867:AAE9I3SMEKbvC726HnaXCRbuKwQD8N1j0Rs'

async def get_chat_info(update):
    chat = update.message.chat
    message_thread_id = update.message.message_thread_id
    print(f"Chat ID: {chat.id}")
    print(f"Chat Type: {chat.type}")
    print(f"Chat Title: {chat.title or 'N/A'}")
    print(f"Topic ID: {message_thread_id or 'N/A'}")
    print(f"From User ID: {update.message.from_user.id}")
    print("--------------------")

async def main():
    bot = Bot(token=BOT_TOKEN)
    
    try:
        print("Fetching updates...")
        updates = await bot.get_updates()
        
        if not updates:
            print("No recent updates found.")
            return

        for update in updates:
            if update.message:
                await get_chat_info(update)
    
    except TelegramError as e:
        print(f"Error: {e}")

if __name__ == '__main__':
    import asyncio
    asyncio.run(main())