#####################
# CSV Structure
# Col 1         col 2           col 3           col 4 [%Y-%m-%d]    col 5
# cardKey       name            surname         expirationDate      lastCoffeeDate
#
from datetime import datetime, date
import csv
from user import User
from order import Order

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
# TODO. Implement a backup feature in the method.
def writeUsers():
    file = open(filenameUsers, "w+")
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
def getUser(cardKey):
    return users[cardKey]

################################



################################
# Orders CSV Structure
# Colum1,  Column2, Column3
# orderId, orderDate, orderRevenue
#
################################\
global filenameOrder
filenameOrder = "orders.csv"

global orders
orders = {}

#loadOrders
# This function load orders from order file to a dictionary
def loadOrders():
    orderfile = open(filenameOrder, "r")
    eachOrder = list(csv.reader(orderfile))
    print(eachOrder)
    for userLine in eachOrder:
         # We initialize the user with valus from the list
         newOrder = Order(date = datetime.strptime(userLine[1], "%Y-%m-%d").date(),revenue = float(userLine[2]))
         orders[newOrder.id] = newOrder

#writeOrders
# This function writes orders to a dictionary
def writeOrders():
    file = open(filenameOrder, "w+", newline = "")
    writer = csv.writer(file, delimiter = ",")

    for id, order in orders.items():
        ordersList = [order.id, order.date, order.revenue]
        writer.writerow(ordersList)


########
# TEST #
########
loadOrders()
print(orders)
print(orders[1].date)

print(users)
newOrder = Order(date = date(2020,2,9), revenue = 3 )
orders[newOrder.id] = newOrder

orders[getNextId] = Order( date = date(2020,2,9), revenue = 3 )
orders[getNextId] = Order( date = date(2020,1,9), revenue = 18 )
writeOrders()

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
