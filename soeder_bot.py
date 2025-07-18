from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import random
import os
from quotes import QUOTES
from gifs import GIFS

# load variables from the .env file
from dotenv import load_dotenv
load_dotenv()

# Get token from the env
TOKEN = os.getenv('TELEGRAM_TOKEN')
PORT = os.getenv('PORT', 4000)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Grüß Gott! 👋 Ich bin SöderDaily Bot.\n\n"
        "Hol dir:\n"
        "• /quote für eine stabile Weisheit\n"
        "• /gif für tägliches Södertainment"
    )


async def quote(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(random.choice(QUOTES) + "\n\n— Markus Söder")

async def send_gif(update: Update, context: ContextTypes.DEFAULT_TYPE):
    gif_url = random.choice(GIFS)
    await context.bot.send_animation(chat_id=update.effective_chat.id, animation=gif_url)

if __name__ == '__main__':
    # Initialize the bot with token
    app = ApplicationBuilder().token(TOKEN).build()

    # Add handlers for commands
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("quote", quote))
    app.add_handler(CommandHandler("gif", send_gif))

    print("Bot gestartet!")
    app.run_webhook(listen="0.0.0.0", port=PORT, url_path=TOKEN, webhook_url="https://soederdaily.onrender.com/" + TOKEN)
