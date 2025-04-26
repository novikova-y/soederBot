import pytest
from unittest.mock import AsyncMock, Mock
from telegram import Update
from telegram.ext import ContextTypes, ApplicationBuilder
from quotes import QUOTES
import random

@pytest.fixture
async def bot_app():
    app = await ApplicationBuilder().token('TELEGRAM_TOKEN').build()
    yield app
    await app.shutdown()

# Asynchronous test for the "/quote" command
@pytest.mark.asyncio
async def test_quote(bot_app):
    # Mock the Telegram bot with AsyncMock for async methods
    mock_update = Mock(spec=Update)
    mock_update.message.reply_text = AsyncMock()

    mock_context = Mock(spec=ContextTypes)

    # Generate a random quote from the list
    random_quote = random.choice(QUOTES)
    expected_response = f"{random_quote}\n\n— Markus Söder"

    # Run the quote command
    async def quote_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
        await update.message.reply_text(expected_response)

    # Check that the response contains one of the quotes
    await quote_handler(mock_update, mock_context)
    
    # Check that reply_text was called with the expected response
    mock_update.message.reply_text.assert_called_with(expected_response)
