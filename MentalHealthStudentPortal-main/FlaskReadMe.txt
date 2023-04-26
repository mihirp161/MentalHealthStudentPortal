Install flask on your computer.

To run the application in debug mode, go to the folder where the flask application is installed. Open the cmd and run:

flask --app app --debug run

Credentials currently registered are:
ID == '0001' 
password == 'password123'



This validations occur on app.py on the home() function

Creating the users should be done on app.py def register():

Reading and storing the dataset should be done in app.py __name__== '__main__'


************************************************
For the timer, we can do something as simple as:

import time

# Start the timer
start_time = time.time()

# Execute whatever procees we need to execute

# Calculate the duration of the process
end_time = time.time()
duration = end_time - start_time

# Print the duration with 5 decimal spaces
print("Duration: {:.5f} seconds".format(duration))
************************************************

********************************************
Please note this lines that need your input

line 6-10
line 25
line 28-29
line 37
line 39
Line 61
Line 71-73
Line 90
Line 99-101
Line 109 (Review this, Ricardo)
Line 116 (Review this, Ricardo)
Line 152-182
Line 193-196 (Review this, Ricardo)

... Adding more soon

********************************************