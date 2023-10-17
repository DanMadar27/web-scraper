from os import makedirs
from src.services.scraper import get_updates, get_notes
from src.utils.files import htmlToPdf
from src.config.files import OUTPUT_PATH

if __name__ == '__main__':
    print('Starting...')

    # Ensure the output directory exists, and if not, create it
    makedirs(OUTPUT_PATH, exist_ok = True)

    # Get the updates
    updates = get_updates()
    update_notes = get_notes(updates[0])

    # Save the updates to a PDF file
    htmlToPdf(str(update_notes), OUTPUT_PATH + '/weapons.pdf')

    print('Finished successfully')