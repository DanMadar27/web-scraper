from bs4 import BeautifulSoup
import requests
from datetime import datetime

from ..config import cod
from src.config.files import WEAPONS_PATH

from ..utils.scraper import *
from src.utils.files import modification_time, html_to_pdf

# Get the latest updates from the Call of Duty website
def get_updates(date):
    try:
        response = requests.get(cod.COD_PATCHES_URL)
        soup = BeautifulSoup(response.text, 'html.parser')
        updates = soup.find_all('div', class_='card-inner')

        if is_new_update(updates[0], date):
            return updates
        
        return None
    
    except Exception as e:
        print(e)
        return None

# Get notes for a specific update_card
def get_notes(update_card):
    h2_tag = update_card.find('h2')
    link = h2_tag.find('a')
    response = requests.get(cod.COD_URL + link['href'])
    return weapons_info(response)

# Get the weapons info for a specific update
def weapons_info(update_page):
    soup = BeautifulSoup(update_page.text, 'html.parser')
    h3_tag = soup.find(find_weapons_title)

    if h3_tag:

        if h3_tag.find_next().name == 'ul' or h3_tag.find_next().name == 'ol':
            return h3_tag.find_next()

        # Find wrapper of the ul
        element = h3_tag.find_next('div')

        while element and not element_contains(element, 'ul'):
            element = element.find_next('div')

            # Ensure that the element is not a new section    
            if element_contains(element, 'h3'):
                return ''
        
        return element if element else ''
    
    return ''

# Check if the update is newer than the date
def is_new_update(update, date):
    if date is None:
        return True
    
    update_date = update.find('div', class_='date')

    if update_date:
        # %B %d, %Y" corresponds to the month name, day of the month, and year
        return datetime.strptime(update_date.text, "%B %d, %Y").date() > date.date()
    
    return False
    
def export_updates():
    # Get updates later than the last fetch
    updates = get_updates(modification_time(WEAPONS_PATH))

    # If there are latest patch notes, get the notes and convert to pdf
    if updates:
        try:
            update_notes = get_notes(updates[0])
            html_to_pdf(str(update_notes), WEAPONS_PATH, 'Updates')
            print('New updates found')

        except Exception as e:
            print('Error getting updates: ' + str(e))

    else:
        print('No new updates')

    return WEAPONS_PATH