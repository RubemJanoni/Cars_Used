import gspread
from google.oauth2.service_account import Credentials
from termcolor import colored

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('cars_used')

cars = SHEET.worksheet('cars')
data = cars.get_all_values()

print(80*"*")
print(30*" " + "WELCOME TO CARS USED")
print(80*"*")
print(colored("Get a car NOW!", 'red'))
print(colored("Search a car and get the specs and prices.\n", 'red'))
car_model = input("Type a brand and model, such as BMW Z4:\n").upper()

keys = data[0]
values = data[1:]

