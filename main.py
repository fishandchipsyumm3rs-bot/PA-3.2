# Countries Woah!
from pyscript import display, document

def countries_capital(e):
    document.getElementById('output').innerHTML = ''
    user_input = document.getElementById('input1').value.capitalize()

    countries = {
    'Madagascar' : 'Antananarivo',
    'Mongolia' : 'Ulaambaatar',
    'Egypt' : 'Cairo',
    'Philippines' : 'Manila',
    'Denmark' : 'Copenhagen',
    'Luxenberg' : 'Luxenberg'
    }
    countries_checkers = user_input in countries
    display_message = (f'Sorry {user_input} in the list', f'{user_input} is in the list')

    display(display_message[countries_checkers], target='result')
