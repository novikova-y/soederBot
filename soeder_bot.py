import os
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import random

# load variables from the .env file
load_dotenv()

# Get token from the env
TOKEN = os.getenv('TELEGRAM_TOKEN')

QUOTES = [
    "„Bayern ist das bessere Deutschland.“",
    "„Der Einfluss der Freien Wähler in Berlin ist genauso groß wie auf dem Mond.“",
    "„Corona ist wie ein Tsunami.“",
    "„Ich sehe mich nicht als Kanzlerkandidat.“",
    "„Wir bleiben stabil.“",
    "„Ich bin ein großer Fan von Star Wars.“",
    "„Wissen Sie, was das schönste an Berlin ist? Der Weg zurück nach Bayern.“",
]

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

    # Get the port from environment variable or use default (8080)
    port = int(os.getenv('PORT', 8080))

    # Use long polling to get updates and listen on the specified port
    app.run_polling(allowed_updates=Update.ALL_TYPES, listen="0.0.0.0", port=port)
