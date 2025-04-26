from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import random
import os
from quotes import QUOTES

# load variables from the .env file
from dotenv import load_dotenv
load_dotenv()

# Get token from the env
TOKEN = os.getenv('TELEGRAM_TOKEN')
PORT = os.getenv('PORT', 4000)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Grüß Gott! 👋 Ich bin SöderDaily Bot.\nSchick mir /quote für eine stabile Weisheit.")

async def quote(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(random.choice(QUOTES) + "\n\n— Markus Söder")

if __name__ == '__main__':
    # Initialize the bot with token
    app = ApplicationBuilder().token(TOKEN).build()

    # Add handlers for commands
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("quote", quote))

    print("Bot gestartet!")
    app.run_webhook(listen="0.0.0.0", port=PORT, url_path=TOKEN, webhook_url="https://soederdaily.onrender.com/" + TOKEN)
