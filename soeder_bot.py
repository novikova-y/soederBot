from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, CallbackQueryHandler
import random
import os
from quotes import QUOTES
from gifs import GIFS

# Load variables from the .env file
from dotenv import load_dotenv
load_dotenv()

# Get token and port from environment
TOKEN = os.getenv('TELEGRAM_TOKEN')
PORT = int(os.getenv('PORT', 4000))

# Define inline keyboard with options
def main_menu_keyboard():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("Noch ein Zitat", callback_data='quote')],
        [InlineKeyboardButton("Noch ein GIF", callback_data='gif')]
    ])

# Start command handler
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Grüß Gott! 👋 Ich bin SöderDaily Bot.\n\n"
        "Hol dir:\n"
        "• /quote für eine stabile Weisheit\n"
        "• /gif für tägliches Södertainment"
    )

# Quote command handler
async def quote(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = random.choice(QUOTES) + "\n\n— Markus Söder"
    await update.message.reply_text(text, reply_markup=main_menu_keyboard())

# GIF command handler
async def send_gif(update: Update, context: ContextTypes.DEFAULT_TYPE):
    gif_url = random.choice(GIFS)
    await context.bot.send_animation(chat_id=update.effective_chat.id, animation=gif_url, reply_markup=main_menu_keyboard())

# Handler for inline button presses
async def handle_button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()  # Acknowledge the button press

    if query.data == 'quote':
        text = random.choice(QUOTES) + "\n\n— Markus Söder"
        await query.message.reply_text(text, reply_markup=main_menu_keyboard())
    elif query.data == 'gif':
        gif_url = random.choice(GIFS)
        await context.bot.send_animation(chat_id=query.message.chat_id, animation=gif_url, reply_markup=main_menu_keyboard())

# Start the bot
if __name__ == '__main__':
    # Initialize the bot with token
    app = ApplicationBuilder().token(TOKEN).build()

    # Add command handlers
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("quote", quote))
    app.add_handler(CommandHandler("gif", send_gif))

    # Add button handler
    app.add_handler(CallbackQueryHandler(handle_button))

    print("Bot gestartet!")
    app.run_webhook(
        listen="0.0.0.0",
        port=PORT,
        url_path=TOKEN,
        webhook_url="https://soederdaily.onrender.com/" + TOKEN
    )