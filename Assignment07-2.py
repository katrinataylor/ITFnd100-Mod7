# ------------------------------------------------- #
# Title: Assignment07-2
# Description: An example of exception handling
# ChangeLog: (Who, When, What)
# Katrina Taylor,8.24.2020,Created Script
# ------------------------------------------------- #
try:
    print("Welcome to Kelley Blue Book 2.0!")
    miles = int(input("How many miles are logged on your car? "))
except ValueError as e: # Error message for when a numeric value is not provided
    print("Only numbers can be inputted.")
except Exception as e: # Error message for all other errors
    print("There was a non-specific error!")
    print("Built-In Python error info: ")
    print(e, e.__doc__, type(e), sep='\n')
else: # When there is no error
    print("You inputted " + miles + "miles driven using your car.")
