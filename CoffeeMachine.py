# CoffeeMachine.py
from user import User
import Database
import statistics
from datetime import date, timedelta
from order import Order
import calendar
from CustomCoffee import CustomCoffee
import os

def cls():
    os.system('cls' if os.name=='nt' else 'clear')
cls()

class CoffeeMachine(object):
    # This declared cmdPrompt as a global (static) variable,
    #   meaning that its going to be the same across all isntances
    #   of the CoffeeMachine objects.
    #   This also means that it can be accessed without self. :)
    global cmdPrompt
    cmdPrompt = "> "
    #availableProducts: dict

    currentUser = None
    #########
    # A method to manually create or overwrite a user using command line input
    # The method does two things with the new user:
    #  Adds it to the databse;
    #  Returns the refference to the new user.
    def createUser(self, cardKey):
        # Creates new user using the input from command line.
        newUser = User(cardKey,
            name = input("Name: " + cmdPrompt),
            surname = input("Surname: " + cmdPrompt)
        )
        if not isinstance(newUser, User): # Validate the user
            raise Exception("ERROR: User creation failed!")

        Database.addUser(newUser) # Add the user to the database
        return newUser # Return the newUse

    def buyMembership(self, user):
        order = Order(date = date.today(), revenue = Database.membershipPrice)
        # Pay with card will return True if payment is successful.
        if payWithCard(order):
            user.expiration = date.today() + timedelta(days = 30)
            Database.addOrder(order)
            Database.writeAll() # Write database values to files immediatelly
            cls()
            print(f"Membership is now valid until {user.expiration}")
        else:
            cls()
            print("Membership purchase operation aborted")
        # In any case returns to the choose delivery part.

        return self.chooseDelivery()
    #########
    # Prompts the user to provide the student card
    # Step 1
    # Checks whether the card is registered in the data base
    # If the user is not registered in the database, it creates the user
    #  (in this prototype case, it will prompt for manual name, surname input)
    # If card is finally recognized continues to Step 2
    # TODO: Implement loop to try again when failed
    def promptCard(self):
        print("\n======================================\n")
        print("       Please, scan your card \n")
        print("======================================")
        print("(Type in Card-Name to load existing one or create a new user)\n")
        # Uses the input from the user, which should be cardKey
        #   to check to which user it belongs by accessing the database
        userInput = input(cmdPrompt)
        # If the user exists in the database, set it to currentUser imediatelly
        if Database.isUser(userInput):
            self.currentUser = Database.getUser(userInput)
        # If the user does not exist, create the user and then set it to current
        else:
            # The user does not exist in the database.
            # Prompts to create a new user
            print("======================================================\n")
            print("User not found in the database. Resgistering new user.\n")
            print("======================================================\n")
            self.currentUser = self.createUser(userInput)
        print(f"Hi {self.currentUser.name}")
        cls()
        return machine.chooseDelivery() # Fianlly, proceed.

    #########
    # Prompts the user to select one of the delivery methods
    #
    # Step 2
    # Its return is based on the user userInput
    # Goes to Steps 3.x
    def chooseDelivery(self):
        while True:
            print("======================================")
            print("        CHOOSE AN OPTION            ")
            print("---------------------------------------")
            print("What delivery option would you like?")
            print("(Type in function name to continue)")
            print("____________________________________")
            # Loop here so that if the userInput is unexpected, it will ask again.
            # The loop will exit using 'return' statements.
            print("menu: Choose a coffee from menu. "
            + "\ncustom: Create a custom coffee"
            + "\nmembership: Buy or extend a memberhip"
            + "\nstats: See the statistics"
            + "\nback: Exit the application")
            print("======================================")

            userInput = input(cmdPrompt)
            # Based on userInput we determine what to do next
            cls()
            if userInput == "menu": # Choose from menu
                # Returning a method means that we are ending what left in this
                #  method and continuing it with the following
                return self.chooseCoffee()
            elif userInput == "custom": # Custom
                return self.buildCoffee()
            elif userInput == "membership": # Update membership
                return self.buyMembership(self.currentUser)
            elif userInput == "stats":
                return statistics.showStatistics()
            elif userInput == "exit" or userInput == "back" : # Exit the loop
                break
            else:
                print("Unexpected input.")


    def buildCoffee(self):
        # Prcess of creating own a coffees
        # User input determines diffrent Layers
        price = 0
        global firstLayer
        global secondLayer
        global thirdLayer
        print("\n======================================\n")
        print("        MAKE YOUR OWN COFFEE             \n")
        print("---------------------------------------\n")
        print("FIRST LAYER : BASE\n\n")
        print("1.One espresso shot\n")
        print("2.Two espresso shots\n")
        print("0. Go back\n")
        firstLayer = input(cmdPrompt)
        while firstLayer not in ("1", "2","0"):
            print("try again")
            firstLayer = input(cmdPrompt)
        else:
            if firstLayer == "1":
                firstLayer = "One espresso shot"
                price += 10
            elif firstLayer == "2":
                firstLayer = "Two espresso shots"
                price += 14
            elif firstLayer == "0":
                cls()
                return self.chooseDelivery()
        cls()
        print("\n======================================\n")
        print("        MAKE YOUR OWN COFFEE             \n")
        print("---------------------------------------\n")
        print ("SECOND LAYER: MILK\n\n")
        print("1.No milk\n")
        print("2.Regular milk\n")
        print("3.Skinny milk\n")
        print("4.Soy milk\n")
        secondLayer = input(cmdPrompt)
        while secondLayer not in ("1","2","3","4"):
            print("try again")
            secondLayer = input(cmdPrompt)
        else:
            if secondLayer == "1":
                secondLayer = "No milk"
            elif secondLayer == "2":
                price += 3
                secondLayer = "Regural milk"
            elif secondLayer == "3":
                secondLayer = "Skinny milk"
                price +=3
            elif secondLayer == "4":
                secondLayer = "Soy milk"
                price +=5
        cls()
        print("\n======================================\n")
        print("        MAKE YOUR OWN COFFEE             \n")
        print("---------------------------------------\n")
        print ("THIRD lAYER: TOPPINGS\n\n")
        print("1.No topping\n")
        print("2.Vanilla Syrup\n")
        print("3.Caramel Syrup\n")
        print("4.Hazelnut Syrup\n")
        thirdLayer = input (cmdPrompt)
        while thirdLayer not in ("1","2","3","4"):
            print("try again")
            thirdLayer = input(cmdPrompt)
        else:
            if thirdLayer == "1":
                thirdLayer = "No topping"
            elif thirdLayer == "2":
                thirdLayer = "Vanilla Syrup"
                price += 4
            elif thirdLayer == "3":
                thirdLayer = "Caramel Syrup"
                price +=4
            elif thirdLayer == "4":
                thirdLayer = "Hazelnut Syrup"
                price +=4
        cls()
        print("\n======================================\n")
        print("        MAKE YOUR OWN COFFEE             \n")
        print("---------------------------------------\n")
        print("How Do you name your coffe?")
        print ("Leave blank if you don't want to")
        customCoffeeName = input(cmdPrompt)
        cls()
        print("\n======================================\n")
        print("        MAKE YOUR OWN COFFEE             \n")
        print("---------------------------------------\n")
        print ("Your coffe:", customCoffeeName)
        print(firstLayer,"with",secondLayer,"and", thirdLayer)
        print("price:", price)
        print()
        print("press 1 to continue")
        print("press 0 to go back")
        decisionInput = input(cmdPrompt)
        if decisionInput == "1":
            cls()
            myCustomCoffee = CustomCoffee(nameId = 0, name = customCoffeeName, price = price, firstLayer = firstLayer, secondLayer = secondLayer, thirdLayer = thirdLayer)
            self.checkout(myCustomCoffee)
        elif decisionInput == "0":
            cls()
            return self.buildCoffee()
    # Prompts the user to select one of the delivery methods
    # Step 3.1
    # Proceeds to checkout with selected Coffee object
    # Goes to step 4
    def chooseCoffee(self):
        menu = Database.getMenu()
        while True: # The loop will exit using return statement
            print("\n======================================\n")
            print("Available coffees:\n")
            for key, coffee in menu.items():
                print(f"{key}: {coffee.name} for {coffee.price} kr.")
            print("---------------------------------------")
            print("\nback: Go back\n\n")
            print("Select the coffee you want")
            print("\n======================================\n")
            userInput = input(cmdPrompt)

            if userInput in menu:
                cls()
                return self.checkout(menu[userInput])
            elif userInput == "back":
                cls()
                return self.chooseDelivery()
            else:
                cls()
                print("Unexpected input.")
    #########
    # Step 4
    # This will determine payment method (membership free coffee or bank ard);
    #  will create a Order object in the database if order was successful;
    #  will proceed to brew coffee.
    #  Goes to Step 5
    def checkout(self, coffee):
        # Intiate an order object
        # Use todays date and set revenue equal to the price of coffee.
        # Note 1: that this will call __init__ of Order once, meaning that
        #  if auto-id was used, it will take up one id, whether the order
        #  will be registered to database or not. (2020-10-09)
        # Note 2: This order is not registered yet
        order = Order(date = date.today(), revenue = coffee.price)

        # OPTION 1: Use free coffee
        # Check if the user can have free coffee
        if self.currentUser.isFreeCoffee(): # If its true
            # Mark that the user had free coffee today
            # Keep in mind that this also stays up-to-date with Database
            #  since in currentUser we store a reference to
            #  an object in database
            self.currentUser.lastFreeCoffeeDate = date.today()
            # Set revenue in order to zero - its free coffee.
            order.revenue = 0.00
        else:
            # OPTION 2: Pay with card
            if payWithCard(order):
                pass # Just let it run the following code after if.
            else:
                return self.chooseDelivery()
        # Register the order in the database TODO
        Database.addOrder(order)
        # Brew the coffee
        self.brewCoffee(coffee)
    #########
    # Prompts credit card info and verifies the payment with bank
    # This is a universal method for paying with card, meaning that it can
    #  be used to pay for coffee and membership too
    # Returns True if payemnt is successful.
    # Returns False if payment is unsuccessful
    def brewCoffee(self, coffee):
        cls()
        print("\n====================================\n")
        print("           SERVING COFFEE        ")
        print(""
        + "\n-------------------------------------"
        + f"\n    Here is your {coffee.name}")
        print()
        if isinstance(coffee, CustomCoffee):
            print(firstLayer,"with",secondLayer,"and", thirdLayer)
        print("""
            Enjoy!
-------------------------------------
        """)

def payWithCard(order):
    print("\n======================================\n")
    print("             Card Payment                \n ")
    print("---------------------------------------\n")
    print(f"\nOrder id: {order.id}\n"
        + f"\nTotal: {order.revenue} kr.\n"
        + f"---------------------------------------\n"
        + "\nPlease input your credit card details.\n"
        + "\n(User hyphens(-) to separate digit pairs)")
    print("\n======================================\n")

    while True:
        cardNumber = input("Number: " + cmdPrompt)
        CVC = input("CVC: " + cmdPrompt)

        # Verify payment with bank
        # PROTOTYPE implementation
        # Check if cardNumber exists
        if cardNumber in Database.bankCards:
            # Check if the CVC is a match
            if Database.bankCards[cardNumber] == CVC:
                # Returns true if its a match
                return True
        print("Invalid credit card detail.")
        # Loop to retry input if the input is unexpected
        while True: # Loop will be stopped by 'break'.
            print("Do you want to try again? (yes/no)")
            userInput = input(cmdPrompt)
            if userInput == "yes": # Breaks out of one loop.
                break
            elif userInput == "no": # Breaks out of sboth loops.
                return False
                break
            else: # Does not break any loop
                print("Unexpected input.")
    def brewCoffee(self, coffee):
        print("\n"
        + "\n-------------------------------------"
        + f"\nHere is your {coffee.name}")
        print()
        if isinstance(coffee, CustomCoffee):
            print(firstLayer,"with",secondLayer,"and", thirdLayer)
        print("""
Enjoy!
-------------------------------------
        """)

# Calling code
machine = CoffeeMachine()

#Load from database
Database.loadUsers()
Database.loadOrders()

machine.promptCard()

# Write database values to files.
Database.writeUsers()
Database.writeOrders()
