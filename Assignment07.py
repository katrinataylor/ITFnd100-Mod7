# ------------------------------------------------- #
# Title: Assignment07-1
# Description: An example of pickling
# ChangeLog: (Who, When, What)
# Katrina Taylor,8.24.2020,Created Script
# ------------------------------------------------- #

import pickle # Load the Pickle function

# Create an object to save (in this case a dictionary of kids vocabulary)
kids_dict = {"a": "apple", "b": "banana", "c": "carrot"}

# Write the kids dictionary to a file using the dump method
objFile = open("KidsDictionary.dat", "ab")
pickle.dump(kids_dict, objFile)
objFile.close()

# Read the kids dictionary from the saved file using load method
objFile = open("KidsDictionary.dat", "rb")
objFileData = pickle.load(objFile)
objFile.close()
print(objFileData)
