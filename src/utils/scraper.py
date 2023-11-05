import random 

# Headers for the scraper requests
def headers():
    return {
        'User-Agent': random_user_agent(),
    }
    
def random_user_agent():
    user_agents = [ 
    	'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36', 
	    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36', 
    	'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36', 
	    'Mozilla/5.0 (iPhone; CPU iPhone OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148', 
    	'Mozilla/5.0 (Linux; Android 11; SM-G960U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.72 Mobile Safari/537.36' 
    ] 

    return random.choice(user_agents) 

def find_weapons_title(tag):
    return tag.name == 'h3' and tag.get_text().lower() == 'weapons'

def find_date(update_page):
    date = update_page.find('p', class_='dateline')
    return date.text if date else ''

def element_contains(element, element_type):
    return element.find(element_type) is not None
