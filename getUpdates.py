from telegram import Bot
BOT_TOKEN = '8038716867:AAE9I3SMEKbvC726HnaXCRbuKwQD8N1j0Rs'
bot = Bot(token=BOT_TOKEN)
updates = bot.get_updates()
print(updates)