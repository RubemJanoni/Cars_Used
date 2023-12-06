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

![cars used](https://github.com/RubemJanoni/Cars_Used/blob/main/views/codep304.jpg)

### Data Model

I decided to use a dictionary to store the information obtained from the database, through a for loop, the information provided by the user is compared with the respective dictionary key, if it matches, return the rest of the information.

The project model basically consists of four functions and a while loop. The first function, "new_car()," handles the insertion of data into the spreadsheet, taking user input and inserting it into the last row of the spreadsheet. The second function, "get_data_cars()," receives the user's car model and checks if it exists in the spreadsheet, returning the result if positive. The third function, "error_test()," deals with possible user input errors. The last function, "delete_data()," is responsible for deleting a specific car in the spreadsheet as entered by the user.

### Testing

I have manually tested this project by doing the following:
- Passed the code through a Code Institute PEP8 linter and comfirmed there are no problems, except for the error E501 (line too long), nothing that interrupts the execution or visualization of the code.
- Given invalid inputs, the program continues without interruption.

![cars used](https://github.com/RubemJanoni/Cars_Used/blob/main/views/codep301.jpg)

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


