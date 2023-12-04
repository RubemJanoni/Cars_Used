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


keys = data[0]
values = data[1:]


#Get a new data from user and add to worksheet
def new_car():
    new_car_data = {}
    for key in keys:
        new_car_data[key] = str(input(f'{key}: ')).upper()

    ultimlin = len(values) + 2  # Obtém a próxima linha disponível
    cars.insert_row(list(new_car_data.values()), index=ultimlin)

    print("\nRegistration completed successfully!")


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

# user answer validation function
def error_text(r):
    while r != "Y" and r != "N" and r != "YES" and r != "NO":
        r = input("Invalid Input. Try again.\n").upper()
    if r == "YES":
        r = "Y"
    elif r == "NO":
        r = "N"
    return r

def delete_data(model):
    data = cars.get_all_values()
    for i, row in enumerate(data[1:], start=2):
        if model == row[0]:
            cars.delete_rows(i)
            print("\nCar removed successfully!")
            return True
    print(colored("Car not found", 'red'))
    return False


print(80 * "*")
print(30 * " " + colored("WELCOME TO CARS USED", 'magenta'))
print(80 * "*")
while True:
    menu = ""
    print("Menu:\n"
          "1 - Search a car\n"
          "2 - Add a car on the DATABASE\n"
          "3 - Delete\n"
          "4 - Exit")
    while True:
        menu = str(input("Choose an Option: "))
        if menu != '1' and menu != '2' and menu != '3' and menu != '4':
            print("Invalid Input, try again.")
        else:
            print()
            break
    if menu == "4":
        print("END")
        break
    else:
        while True:
            cars = SHEET.worksheet('cars')
            data = cars.get_all_values()
            keys = data[0]
            values = data[1:]

            if menu == "1":
                print(colored("Get a car NOW!", 'green'))
                print(colored("Search a car and get the specs and prices.\n", 'cyan'))
                car_model = input("Type a brand and model, like BMW Z4:\n").upper()
                new_data = get_data_cars(car_model)
                if not new_data:
                    print(colored("CAR NOT FOUND", 'red'))
                    print(colored("Choose an option below:", 'green'))
                    menu = input("1 - Search a new car\n"
                                 "2 - Register a new car\n"
                                 "3 - Back to Menu\n")
                                 
                    while menu != "1" and menu != "2" and menu != "3":
                        resposta = input("Invalid input.\n")
                    if menu == "3":
                        menu = ""
                        break
                else:
                    print(colored("Specifications:\n", 'green'))
                    for key, value in new_data[0].items():
                        print(colored(f"{key.capitalize()}: {value}\n", 'blue'))
                    resposta = input(colored("Would you like to try another model? Y/N?\n", 'magenta'))
                    resposta = error_text(resposta.upper())
                    if resposta.lower() != "y":
                        print()
                        break
                    else:
                        print()
            elif menu == "2":
                while True:
                    data = cars.get_all_values()
                    values = data[1:]
                    print("Enter vehicle specifications.")
                    new_car()
                    resposta = input("Would you like a new register? Y/N?\n").upper()
                    resposta = error_text(resposta)
                    if resposta.lower() != "y":
                        menu = ""
                        print()
                        break
                    else:
                        print()
                        continue
            elif menu == "3":
                while True:
                    data = cars.get_all_values()
                    values = data[1:]
                    car_model = input("Type a brand and model, such as BMW Z4:\n").upper()
                    achou = delete_data(car_model)
                    if achou is False:
                        print(colored("Car not found", 'red'))
                        resposta = input("1 - Delete another car\n"
                                     "2 - Back to menu\n"
                                     "Choose an option above: ")
                        while resposta != "1" and resposta != "2":
                            resposta = input("Invalid Input, try again.\n")
                        if resposta == "1":
                            menu = "3"
                            break
                        elif resposta == "2":
                            menu = ""
                            break
                    else:
                        resposta = input(colored("Would you like to try another model? Y/N?\n", 'magenta'))
                        resposta = error_text(resposta.upper())
                        if resposta.lower() != "y":
                            menu = ""
                            print()
                            break
                        else:
                            print()
                            break
            else:
                break