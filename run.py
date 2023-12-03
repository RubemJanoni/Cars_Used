import gspread
from google.oauth2.service_account import Credentials
from termcolor import colored
import xlwings as xw
from xlwings.constants import DeleteShiftDirection

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
print(30*" " + colored("WELCOME TO CARS USED", 'magenta'))
print(80*"*")
print(colored("Get a car NOW!", 'green'))
print(colored("Search a car and get the specs and prices.\n", 'cyan'))
car_model = input("Type a brand and model, such as BMW Z4:\n").upper()

keys = data[0]
values = data[1:]


#Get a new data from user and add to worksheet
def new_car():
    newCar = []
    for c in keys:
        newCar.append(str(input(f'{c}: ')).upper())
    cars.range(f'A{ultimlin + 1}').value = newCar
    wb.save('cars_used.xlsx')
    print("\nCadastro realizado com sucesso!")

def get_data_cars(car_model):
    """
    Get car_model input from the user.
    Run a for loop and build a dictionary from
    the two lists keys and values, check if the key 'car_name'
    of the dictionary is equal to the variable car_model
    and assign the variable result.
    """
    values = data[1:]
    result = []
    for v in values:
        my_dict = dict(zip(keys, v))
        if my_dict['car_name'].upper() == car_model:
            result.append(my_dict)
    return result