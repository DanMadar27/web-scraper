from os import makedirs
from dotenv import load_dotenv
from src.services.telegram_bot import start
from src.config.files import OUTPUT_PATH

if __name__ == '__main__':
    print('Starting...')
    load_dotenv()  # take environment variables from .env.
    makedirs(OUTPUT_PATH, exist_ok = True) # Ensure the output directory exists, and if not, create it
    start()