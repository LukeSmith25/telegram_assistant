from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext
from config import BOT_TOKEN

# Initialize bot application
app = Application.builder().token(BOT_TOKEN).build()

# Start Command
async def start(update: Update, context: CallbackContext):
    await update.message.reply_text("Hello! I'm your assistant bot. How can I help?")

# Help Command
async def help_command(update: Update, context: CallbackContext):
    await update.message.reply_text("Available commands:\n/start - Start the bot\n/help - List commands\n/links - Get helpful links")

# Fetch Quick Links
async def links(update: Update, context: CallbackContext):
    response = """Here are some useful links:
    - [Telegram Bot API](https://core.telegram.org/bots/api#authorizing-your-bot)
    - [FastAPI Documentation](https://fastapi.tiangolo.com/)
    - [python-telegram-bot Docs](https://python-telegram-bot.readthedocs.io/en/stable/)
    """
    await update.message.reply_text(response)

# Echo Handler (Repeats messages)
async def echo(update: Update, context: CallbackContext):
    await update.message.reply_text(f"You said: {update.message.text}")

# Register Handlers
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("help", help_command))
app.add_handler(CommandHandler("links", links))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

# Run Bot in Polling Mode
if __name__ == "__main__":
    print("Bot is running...")
    app.run_polling()
