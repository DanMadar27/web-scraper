def find_weapons_title(tag):
    return tag.name == 'h3' and tag.get_text() == 'Weapons'
