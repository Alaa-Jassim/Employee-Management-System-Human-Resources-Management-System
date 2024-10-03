

import json
import os 


def get_language():
    """Charge la langue préférée depuis un fichier de configuration ou renvoie 'English' par défaut."""
    try:
        with open(f'{get_path("config")}.json', 'r', encoding='utf-8') as file:
            config = json.load(file)
            return config.get('preferred_language', 'English')
    except FileNotFoundError:
        return 'English'

def get_translation(language):
    """Charge les traductions spécifiques à une langue."""
    with open(f'{get_path(language)}.json', 'r', encoding='utf-8') as file:
        return json.load(file)

def save_language(language):
    """Sauvegarde la langue préférée dans un fichier de configuration."""
    with open(f'{get_path("config")}.json', 'w', encoding='utf-8') as file:
        json.dump({'preferred_language': language}, file)


def get_path(filename):
    base_path = os.path.dirname(__file__)
    resources_path = os.path.join(base_path, '..', 'resources')
    os.makedirs(resources_path, exist_ok=True)
    db_path = os.path.join(resources_path, filename)
    return db_path







