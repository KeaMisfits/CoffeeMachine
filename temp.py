###############################
# Load users
# This method load users from users file to a dictionary
def loadUsers():
    file = open(filenameUsers, "r")
    allUsers = list(csv.reader(file))
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

# Write users
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
#   Returns True if there is a user in the database with the given cardKey.
def isUser(cardKey):
    if cardKey in users:
        return True
    return False
#   Returns menu dictionary
def getMenu():
    return menu
#   Returns bankCards dictionary (PROTOTYPE method)
def getBankCards():
    return bankCards
###############################

###############################
# Mutators and appenders
def addOrder(order):
    if isinstance(order, Order): # Validate parameter input
        orders[order.id] = order
    else: # If the parameter input is invalid, show a warning and don't add
        # Show warning message
        print(f"WARNING in {__name__} at {addOrder.__name__}: "
        + "The input parameter is not of type Order. Database not updated."
        )
def addUser(user):
    if isinstance(user, User): # Validate parameter input
        users[user.cardKey] = user
    else: # If the parameter input is invalid, show a warning and don't add
        # Show warning message
        print(f"WARNING in {__name__} at {addOrder.__name__}: "
        + "The input parameter is not of type User. Database not updated."
        )
################################