from dotenv import load_dotenv
from os import getenv
def load_key() -> str:
    """ Loads a JSON file """
    load_dotenv('.env')
    return getenv('API_KEY')
    