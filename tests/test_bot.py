import pytest
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from quotes import QUOTES
import random

# Mark the test as asynchronous
@pytest.mark.asyncio
async def test_flask_app():
    # Mock the client
    response = await app.test_client().get('/')
    assert response.status_code == 200
    assert b'Bot gestartet!' in response.data

# Asynchronous test for the "/quote" command
@pytest.mark.asyncio
async def test_quote():
    # Mock the Telegram bot
    mock_update = pytest.Mock(spec=Update)
    mock_context = pytest.Mock(spec=ContextTypes)

    # Generate a random quote from the list
    random_quote = random.choice(QUOTES)
    expected_response = f"{random_quote}\n\n— Markus Söder"

    # Run the quote command
    async def quote_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
        await update.message.reply_text(expected_response)

    # Check that the response contains one of the quotes
    await quote_handler(mock_update, mock_context)
    mock_update.message.reply_text.assert_called_with(expected_response)