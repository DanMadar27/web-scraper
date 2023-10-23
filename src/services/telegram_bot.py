from os import environ
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import threading

from src.services.scraper import export_updates
from src.utils.logs import log_command
from src.utils.rateLimit import is_rate_limited, reset_rate_limit

async def start_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if is_rate_limited():
        return
    
    log_command('start', update.message.from_user)

    await update.message.reply_text(
        'Hello, I am the Call of Duty Bot. I will keep you updated with the latest patch notes.\n' +
        'Use /help to see the possible commands.'
    )

async def help_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if is_rate_limited():
        return
    
    log_command('help', update.message.from_user)

    await update.message.reply_text(
        'These are the possible commands:\n\n'
        '/start - Show a welcome message\n' +
        '/help - Show possible commands\n' + 
        '/updates - Get the latest patch notes of Call of Duty'
    )

async def updates_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if is_rate_limited():
        return
    
    log_command('updates', update.message.from_user)
    updates_file = export_updates()
    await context.bot.send_document(chat_id = update.message.chat_id, document = open(updates_file, 'rb'))

def start():
    app = ApplicationBuilder().token(environ.get('BOT_TOKEN')).build()

    app.add_handler(CommandHandler('start', start_handler))
    app.add_handler(CommandHandler('help', help_handler))
    app.add_handler(CommandHandler('updates', updates_handler))

    # Start rate limit reset thread
    threading.Thread(target = reset_rate_limit).start()

    app.run_polling()
