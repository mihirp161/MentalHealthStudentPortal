Install flask on your computer.

To run the application in debug mode, go to the folder where the flask application is installed. Open the cmd and run:

flask --app app --debug run

Credentials currently registered are:
email == 'user@example.com' 
password == 'password123'

This validations occur on app.py on the home() function

Creating the users should be done on app.py def register():

Reading and storing the dataset should be done in app.py __name__== '__main__'