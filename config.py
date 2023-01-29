import os
from dotenv import load_dotenv
load_dotenv()

TOKEN = os.getenv('TOKEN')
API_KEY = os.getenv('API_KEY')  # for https://v6.exchangerate-api.com/ server

keys = {
    'dollar': 'USD',
    'ruble': 'RUB',
    'euro': 'EUR'
}
