from os import environ
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import threading
from logging import basicConfig as logging_basicConfig, INFO

from src.services.scraper import get_updates, get_notes
from src.utils.files import modification_time, html_to_pdf
from src.utils.rateLimit import is_rate_limited, reset_rate_limit
from src.config.files import WEAPONS_PATH

logging_basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=INFO
)

async def start_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if is_rate_limited():
        return
    
    await update.message.reply_text(
        'Hello, I am the Call of Duty Bot. I will keep you updated with the latest patch notes.\n' +
        'Use /help to see the possible commands.'
    )

async def help_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if is_rate_limited():
        return
    
    await update.message.reply_text(
        '/start - Show a welcome message\n' +
        '/help - Show possible commands\n' + 
        '/updates - Get the latest patch notes of Call of Duty'
    )

async def updates_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if is_rate_limited():
        return
    
    # Get updates later than the last fetch
    updates = get_updates(modification_time(WEAPONS_PATH))

    # If there are latest patch notes, get the notes and convert to pdf
    if updates:
        try:
            update_notes = get_notes(updates[0])
            html_to_pdf(str(update_notes), WEAPONS_PATH)
            print('New updates found')
        except Exception as e:
            print('Error getting updates: ' + str(e))

    else:
        print('No new updates')

    await context.bot.send_document(chat_id = update.message.chat_id, document = open(WEAPONS_PATH, 'rb'))

def start():
    print('Starting bot...')
    app = ApplicationBuilder().token(environ.get('BOT_TOKEN')).build()

    app.add_handler(CommandHandler('start', start_handler))
    app.add_handler(CommandHandler('help', help_handler))
    app.add_handler(CommandHandler('updates', updates_handler))

    # Start rate limit reset thread
    threading.Thread(target = reset_rate_limit).start()

    app.run_polling()
