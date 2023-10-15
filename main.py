from src.services import scraper

if __name__ == '__main__':
    print('Starting...')
    updates = scraper.get_updates()
    print(updates)
    update_notes = scraper.get_notes(updates[0])
    print(update_notes)