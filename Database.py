#####################
# CSV Structure for users.csv
# Col 1         col 2           col 3           col 4 [%Y-%m-%d]    col 5
# cardKey       name            surname         expirationDate      lastCoffeeDate
#
from datetime import datetime, date
import csv
from user import User
from Coffee import Coffee

# Filenames
global filenameUsers
filenameUsers = "users.csv"

# Data from files
global users
users = {}

#################
# Hard-coded data
#   Menu has key for coffeNameId and Coffee as value
menu = {
"latte": Coffee("latte", "Latte", 12.50),
"capuchino": Coffee("capuchino", "Capuchino", 15.00)
}

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
        newUser = User(cardKey = userLine[0],
         name = userLine[1],
         surname = userLine[2],
         expiration = datetime.strptime(userLine[3], "%Y-%m-%d").date(),
         lastFreeCoffeeDate = datetime.strptime(userLine[4], "%Y-%m-%d").date()
        )
        users[newUser.cardKey] = newUser # Adds the newUser to the dictionary

###############################


###############################
# Write users
# TODO. Implement a backup feature in the method.
def writeUsers():
    # We use the "w+" to open and truncate the file
    # We also use newline="" so that the writer does not make empty gaps
    file = open(filenameUsers, "w+", newline="")
    writer = csv.writer(file, delimiter = ",")

    # We loop through all of the items in our users dictionary.
    for key, user in users.items():
        # The items() method returns a tuple {key, value}. We need only the value
        #  thus we take the second value of the tuple to be our user object.
        # Make a list from one user
        userAsList = [user.cardKey, user.name, user.surname, user.expiration, user.lastFreeCoffeeDate]
        # Write the list as a new line in the file.
        writer.writerow(userAsList)

###############################

###############################
# Accessers
#   Returns usser object from all user data
def getUser(cardKey):
    return users[cardKey]
#   Returns menu dictionary
def getMenu():
    return menu
#   Returns Coffee object from the menu.
#    TODO: may be useless
def getMenuCoffee(nameId):
    return menu[nameId]

###############################

#################
# #Date parser test
# dateInString = str(date(2020,10,1))
# print(f"orginal: {dateInString}")
#dateFromString = datetime.strptime(dateInString, "%Y-%m-%d").date()
#
# print(f"converted {dateFromString}")
