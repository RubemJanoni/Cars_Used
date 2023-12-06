# Cars Used Code

Cars Used is a Python terminal code which runs in the Code Institute mock terminal on Heroku.

The Cars Used code aims to offer to the user the experience of consulting the desired car in the database and obtaining technical information about the car.

The user can also enter any car model and its specifications into our database, but there is also the option to delete a specific vehicle from the database. The database has been recorded in a spreadsheet hosted on Google Cloud.

The live link can be found here - [Cars Used](https://carsused.herokuapp.com/)

![cars used](https://github.com/RubemJanoni/Cars_Used/blob/main/views/codep302.jpg)

## How to run

When running the code, an excel spreadsheet containing the database, information about available cars, is loaded and assigned to a variable. Then the user is invited to search for a car model, the model provided through the input will be consulted in the available database, having the desired car, all specifications are presented on the screen.

### Features

Despite running in the terminal, some colors were used through the termcolor library, in an attempt to make it more user-friendly.
In this project, the gspread and google-auth libraries were also used.

![cars used](https://github.com/RubemJanoni/Cars_Used/blob/main/views/codep304.jpg)

Through option 1 in the menu (Search a car), the user can search for a car in the database.

![cars used](https://github.com/RubemJanoni/Cars_Used/blob/main/views/pp3-tela01.jpg)

![cars used](https://github.com/RubemJanoni/Cars_Used/blob/main/views/pp3-tela02.jpg)

Thus, the user receives, as a response, a list of the car specifications, such as fuel type, power, torque, engine, and price.

![cars used](https://github.com/RubemJanoni/Cars_Used/blob/main/views/pp3-tela03.jpg)

In option 2 of the menu (Add a car), the user can insert a vehicle of their choice into the database, starting with the model name.

![cars used](https://github.com/RubemJanoni/Cars_Used/blob/main/views/pp3-tela04.jpg)

Options 3 (Delete) and (Exit) allow the user, respectively, to DELETE a vehicle from the spreadsheet and EXIT the system at any time.


### Data Model

I decided to use a dictionary to store the information obtained from the database, through a for loop, the information provided by the user is compared with the respective dictionary key, if it matches, return the rest of the information.

The project model basically consists of four functions and a while loop. The first function, "new_car()," handles the insertion of data into the spreadsheet, taking user input and inserting it into the last row of the spreadsheet. The second function, "get_data_cars()," receives the user's car model and checks if it exists in the spreadsheet, returning the result if positive. The third function, "error_test()," deals with possible user input errors. The last function, "delete_data()," is responsible for deleting a specific car in the spreadsheet as entered by the user.

### Testing

I have manually tested this project by doing the following:
- Passed the code through a Code Institute PEP8 linter and comfirmed there are no problems, except for the error w292 (no newline at the end of line), nothing that interrupts the execution or visualization of the code.
  

### Validator Testing

    "No error that could compromise the system's functionality was returned."





### Deployment

This project was deployed Code Institute's mock terminal for Heroku.

- Steps for deployment:
  - Fork or clone this repository
  - Create a new Heroku app
  - Set the buildpacks to Python and Node.js in that order
  - Link the Heroku app to the repository
  - Click on deploy

### Credits

- Code Institute for the deployment terminal.
- Kaggle for dataset used in this project. (kaggle.com)


