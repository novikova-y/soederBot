from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import random
import os

# load variables from the .env file
from dotenv import load_dotenv
load_dotenv()

# Get token from the env
TOKEN = os.getenv('TELEGRAM_TOKEN')
PORT = os.getenv('PORT', 4000)

QUOTES = [
    "„Bayern ist das bessere Deutschland.“",
    "„Der Einfluss der Freien Wähler in Berlin ist genauso groß wie auf dem Mond.“",
    "„Corona ist wie ein Tsunami.“",
    "„Ich sehe mich nicht als Kanzlerkandidat.“",
    "„Wir bleiben stabil.“",
    "„Ich bin ein großer Fan von Star Wars.“",
    "„Wissen Sie, was das schönste an Berlin ist? Der Weg zurück nach Bayern.“",
    "„Weihnachten bemisst sich offenkundig dieses Jahr nicht in dem Wert von Konsum und Geschenken. Vielleicht sollten wir jetzt mal reflektieren, dass das tollste Geschenk Gesundheit und Gemeinsamkeit ist.“",
    "„Das ganze Leben ist ein großer Kompromiss, das fängt bei der Ehe an und endet in der Politik.“",
    "„Wir machen in Bayern grüne Politik, aber wir brauchen die Grünen nicht dazu.“",
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
    app.run_webhook(listen="0.0.0.0", port=PORT, url_path=TOKEN, webhook_url="https://soederdaily.onrender.com/" + TOKEN)
