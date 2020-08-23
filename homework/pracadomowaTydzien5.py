wqfrom requests.exceptions import Timeout
import requests
from datetime import datetime
import time
import sys


def decor(function):
    def inside():
        print('Aktualne kursy Euro, wyniki zwracane co 5 secund')
        print('Przerwanie działania programu, naciśnij Ctrl+F2')
        return function()
    return inside


def current_value():
    print('------------------------------------------------------')
    try:
        r = requests.get('http://api.nbp.pl/api/exchangerates/rates/A/EUR')
    except requests.exceptions.ConnectionError:
        print('Problem with Internet Connection')
        print('Exit')
        sys.exit(0)

    date_response = datetime.now()
    r_dictionary = r.json()

    print(f"Kurs Euro: {r_dictionary.get('rates')[0].get('mid')}")
    print(
        f'Data i godzina: {date_response.year}-{date_response.month}-{date_response.day} {date_response.hour}:{date_response.minute}:{date_response.second}')
    print(f'Czas wykonania zapytania: {r.elapsed.total_seconds()}')


new_function = decor(current_value)

while True:
        new_function()
        time.sleep(5)




