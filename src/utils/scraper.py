def find_weapons_title(tag):
    return tag.name == 'h3' and tag.get_text().lower() == 'weapons'

def element_contains(element, element_type):
    return element.find(element_type) is not None
