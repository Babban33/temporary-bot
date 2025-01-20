import os
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, ContextTypes, filters
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
GROUP_A_ID = int(os.getenv("GROUP_A_ID"))
GROUP_B_ID = int(os.getenv("GROUP_B_ID"))
TOPIC_1_ID = int(os.getenv("TOPIC_1_ID"))
TOPIC_2_ID = int(os.getenv("TOPIC_2_ID"))
ADMIN_USER_ID = int(os.getenv("ADMIN_USER_ID"))

forwarding_enabled = True

async def forward_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if not forwarding_enabled:
        return

    if update.message and update.message.chat.id == GROUP_A_ID and update.message.message_thread_id == TOPIC_1_ID:
        try:
            sender_name = update.message.from_user.first_name
            message_text = f"From {sender_name}: {update.message.text}"
            await context.bot.send_message(chat_id=GROUP_B_ID, text=message_text, message_thread_id=TOPIC_2_ID)
        except Exception as e:
            print(f"Error forwarding message: {e}")

async def start_forwarding(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    global forwarding_enabled
    if update.message.from_user.id == ADMIN_USER_ID:
        forwarding_enabled = True
        await update.message.reply_text("Message forwarding started.")
    else:
        await update.message.reply_text("You don't have permission to use this command.")

async def stop_forwarding(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    global forwarding_enabled
    if update.message.from_user.id == ADMIN_USER_ID:
        forwarding_enabled = False
        await update.message.reply_text("Message forwarding stopped.")
    else:
        await update.message.reply_text("You don't have permission to use this command.")

def main() -> None:
    application = Application.builder().token(BOT_TOKEN).build()

    application.add_handler(CommandHandler("start", start_forwarding))
    application.add_handler(CommandHandler("stop", stop_forwarding))
    application.add_handler(MessageHandler(filters.ALL, forward_message))

    print("Starting bot...")
    application.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == "__main__":
    main()