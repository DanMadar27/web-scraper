from os import makedirs
from src.services.telegram_bot import start
from src.config.files import OUTPUT_PATH

if __name__ == '__main__':
    print('Starting...')
    makedirs(OUTPUT_PATH, exist_ok = True) # Ensure the output directory exists, and if not, create it
    start()