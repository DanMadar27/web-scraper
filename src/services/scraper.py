from bs4 import BeautifulSoup
import requests
import random 
from datetime import datetime

from ..config import cod
from src.config.files import WEAPONS_PATH

from ..utils.scraper import *
from src.utils.files import modification_time, html_to_pdf

# Headers for the scraper requests
def headers():
    return {
        'User-Agent': random_user_agent(),
    }

# Get the latest updates from the Call of Duty website
def get_updates(date):
    try:
        response = requests.get(cod.COD_PATCHES_URL, headers = headers())
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
    # Get the link to the update page
    h_tag = update_card.find(['h2', 'h3'])
    link = h_tag.find('a')
    response = requests.get(cod.COD_URL + link['href'], headers = headers())

    update_page = BeautifulSoup(response.text, 'html.parser')

    # Get the title of the update
    title = update_page.find('h1')
    title = title.text if title else ''

    # Get the date of the update
    date = update_page.find('p', class_='dateline')
    date = date.text if date else ''

    # Get the weapons info
    weapons = weapons_info(update_page)
    
    return (weapons, title, date)

# Get the weapons info for a specific update
def weapons_info(update_page):
    h3_tag = update_page.find(find_weapons_title)

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
            (update_notes, title, date) = get_notes(updates[0])
            html_to_pdf(str(update_notes), WEAPONS_PATH, title, date)
            print('New updates found')

        except Exception as e:
            print('Error getting updates: ' + str(e))

    else:
        print('No new updates')

    return WEAPONS_PATH

def random_user_agent():
    user_agents = [ 
	'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36', 
	'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36', 
	'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36', 
	'Mozilla/5.0 (iPhone; CPU iPhone OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148', 
	'Mozilla/5.0 (Linux; Android 11; SM-G960U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.72 Mobile Safari/537.36' 
    ] 

    return random.choice(user_agents) 