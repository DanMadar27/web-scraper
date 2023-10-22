def find_weapons_title(tag):
    return tag.name == 'h3' and tag.get_text().lower() == 'weapons'

def find_date(update_page):
    date = update_page.find('p', class_='dateline')
    return date.text if date else ''

def element_contains(element, element_type):
    return element.find(element_type) is not None
