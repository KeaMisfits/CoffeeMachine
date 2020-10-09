#####################
# CSV Structure
# Col 1         col 2           col 3           col 4 [%Y-%m-%d]    col 5
# cardKey       name            surname         expirationDate      lastCoffeeDate
#
from datetime import datetime, date
import csv
from user import User

global filenameUsers
filenameUsers = "users.csv"

global users
users = {}

###############################
# Load users
# This method load users from users file to a dictionary
def loadUsers():
    file = open(filenameUsers, "r")
    allUsers = list(csv.reader(file)) # This creates a list of lists

    # From every list (userLine) in the list, we create a new user object,
    #  that we put into the dictonary. We use cardKey value from the users
    #  as the key.
    for userLine in allUsers:
        # We initialize the user with valus from the list
        newUser = User(cardKey = userLine[0], name = userLine[1], surname = userLine[2], expiration = userLine[3], lastFreeCoffeeDate = userLine[4])
        users[newUser.cardKey] = newUser # Adds the newUser to the dictionary
###############################


###############################
# Write users
# Creates a writer objects, then loops through whole users dictionary
#  while converting users into list and writing each list as a new line.
# TODO. Implement a backup feature in the method.
def writeUsers():
    file = open(filenameUsers, "w+") # W+ means that we open for writing and erase all
    writer = csv.writer(file, delimiter = ",")

    # We loop through all of the items in our users dictionary.
    for userTuple in users.items():
        # The items() method returns a tuple {key, value}. We need only the value
        #  thus we take the second value of the tuple to be our user object.
        user = userTuple[1]
        # Make a list from one user
        userAsList = [user.cardKey, user.name, user.surname, user.expiration, user.lastFreeCoffeeDate]
        # Write the list as a new line in the file.
        writer.writerow(userAsList)
###############################


loadUsers()
print(users)

print(users.get("qwerty123").name)

users["abcabc123"] = User("abcabc123", name = "Jason", surname = "Statham")

writeUsers()

print("Done!")

#################
# #Date parser test
# dateInString = str(date(2020,10,1))
# print(f"orginal: {dateInString}")
# dateFromString = datetime.strptime(dateInString, "%Y-%m-%d").date()
#
# print(f"converted {dateFromString}")
