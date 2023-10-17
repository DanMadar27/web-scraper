from bs4 import BeautifulSoup
import requests

from ..config import cod
from ..utils.scraper import *

def get_updates():
    """Get the latest updates from the Call of Duty website."""
    response = requests.get(cod.COD_PATCHES_URL)
    soup = BeautifulSoup(response.text, 'html.parser')
    updates = soup.find_all('div', class_='card-inner')
    return updates

def get_notes(update_card):
    """Get notes for a specific update_card."""
    h2_tag = update_card.find('h2')
    link = h2_tag.find('a')
    response = requests.get(cod.COD_URL + link['href'])
    return weapons_info(response)

def weapons_info(update_page):
    """Get the weapons info for a specific update."""
    soup = BeautifulSoup(update_page.text, 'html.parser')
    h3_tag = soup.find(find_weapons_title)
    weapons_info = h3_tag.find_next('ul')
    return weapons_info