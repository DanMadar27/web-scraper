from os import makedirs
from src.services.scraper import get_updates, get_notes
from src.utils.files import modification_time, html_to_pdf
from src.config.files import OUTPUT_PATH, WEAPONS_PATH

if __name__ == '__main__':
    print('Starting...')

    # Ensure the output directory exists, and if not, create it
    makedirs(OUTPUT_PATH, exist_ok = True)

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

    print('Finished successfully')