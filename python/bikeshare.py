import time
import pandas as pd
import numpy as np
import datetime as dt
import click

CITY_DATA_MAP = {'chicago': 'chicago.csv',
                 'new york city': 'new_york_city.csv',
                 'washington': 'washington.csv'}

MONTHS = ('january', 'february', 'march', 'april', 'may', 'june')

WEEKDAYS = ('sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday',
            'saturday')


def get_user_choice(prompt, choices=('y', 'n')):
    """Accepts user input and ensures it is a valid choice."""
    while True:
        user_input = input(prompt).lower().strip()
        if user_input == 'end':
            raise SystemExit
        elif ',' not in user_input:
            if user_input in choices:
                break
        elif ',' in user_input:
            user_input = [i.strip().lower() for i in user_input.split(',')]
            if list(filter(lambda x: x in choices, user_input)) == user_input:
                break

        prompt = ("\nInvalid input. Please check the formatting and enter a valid option:\n>")

    return user_input


def get_data_filters():
    """Prompt the user to specify city(ies), month(s), and weekday(s)."""
    print("\n\nLet's explore some US bikeshare data!\n")

    print("Type 'end' at any time to exit the program.\n")

    while True:
        cities = get_user_choice("\nWhich city(ies) would you like to select data for? "
                                 "New York City, Chicago, or Washington? Use commas "
                                 "to separate the names.\n>", CITY_DATA_MAP.keys())
        months = get_user_choice("\nFrom January to June, which month(s) would you like to "
                                 "filter data by? Use commas to separate the names.\n>",
                                 MONTHS)
        weekdays = get_user_choice("\nFor which weekday(s) would you like to filter bikeshare "
                                   "data? Use commas to separate the names.\n>", WEEKDAYS)

        confirmation = get_user_choice("\nPlease confirm the selected filter(s) for the bikeshare data:"
                                       "\n\n City(ies): {}\n Month(s): {}\n Weekday(s): {}\n\n [y] Yes\n [n] No\n\n>"
                                       .format(cities, months, weekdays))
        if confirmation == 'y':
            break
        else:
            print("\nLet's try again!")

    print('-'*40)
    return cities, months, weekdays

