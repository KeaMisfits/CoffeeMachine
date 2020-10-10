# CoffeeMachine.py
from user import User
import fakedata
import Database
from datetime import date
from order import Order

class CoffeeMachine(object):

    # This declared cmdPrompt as a global (static) variable,
    #   meaning that its going to be the same across all isntances
    #   of the CoffeeMachine objects.
    #   This also means that it can be accessed without self. :)
    global cmdPrompt
    cmdPrompt = "> "

    #availableProducts: dict
    #cardKey: str
    currentUser = None

    def TMP_initDatabase(self): # Temporary for initializing database without object
        Database.loadUsers()
    #########
    # Prompts the user to provide the student card
    # Step 1
    # Checks whether the card is valid
    # If card is valid continues to Step 2
    # TODO: Implement loop to try again when failed
    def promptCard(self):
        print("Please, scan your card")
        # Uses the input from the user, which should be cardKey
        #   to check to which user it belongs by accessing the database
        feedback = Database.getUser(input(cmdPrompt))
        # At this point we are not sure if the user was found
        #   thus, we make sure by checking whether the return
        #   value is of User type.
        if isinstance(feedback, User):
            # If condition passes we know that its a valid user
            self.currentUser = feedback
            machine.chooseDelivery()
        else:
            # The condition didn't pass. It must be an error.
            print("Error: Scan failed")

    #########
    # Prompts the user to select one of the delivery methods
    # Step 2
    # Its return is based on the user userInput
    # Goes to Steps 3.x
    def chooseDelivery(self):
        print(f"Hi {self.currentUser.name}, what delivery option would you like?")

        # Loop here so that if the userInput is unexpected, it will ask again.
        while True: # The loop will exit using 'return' statements.
            print("Type '1' for menu or '2' for custom. Type 0 to exit")
            userInput = input(cmdPrompt)
            # Based on userInput we determine what to do next
            if userInput == "1": # Choose from menu
                # Returning a method means that we are ending what left in this
                #  method and continuing it with the following
                return self.chooseCoffee()
            elif userInput == "2": # Custom
                return self.buildCoffee()
            elif userInput == "0": # Exit the loop
                break
            else:
                print("Unexpected input.")

    def buildCoffee(self):
        pass
    #########
    # Prompts the user to select one of the delivery methods
    # Step 3.1
    # Proceeds to checkout with selected Coffee object
    # Goes to step 4
    def chooseCoffee(self):
        menu = Database.getMenu()
        while True: # The loop will exit using return statement
            print("Available coffees:")
            for key, coffee in menu.items():
                print(f"{key}: {coffee.name} for {coffee.price} kr.")
            print("0: <- Go back")
            print("Select the coffee you want")
            userInput = input(cmdPrompt)

            if userInput in menu:
                print(f"debug: you selected {menu[userInput].name}")
                return self.checkout(menu[userInput])
            elif userInput == "0":
                return self.chooseDelivery()
            else:
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
            tryToPay = True # Flag used to indicate whether user wants to retry
            while tryToPay:
                # Calls a function that will prompt credit card info, verify
                #  with the bank and return True/False based on success.
                cardAccepted = self.payWithCard(coffee.price) # Boolean
                if cardAccepted:
                    print("debug: Card accepted")
                    break
                    # Note, that this will continue execution outside else.
                else:
                    # Loop to retry input if the input is unexpected
                    while True: # Loop will be stopped by 'break'
                        print("Do you want to try again? (yes/no)")
                        userInput = input(cmdPrompt)
                        if userInput == "yes": # Breaks out of one loop.
                            tryToPay = True
                            break
                        elif userInput == "no": # Breaks out of both loops.
                            tryToPay = False
                            break
                        else: # Does not break any loop
                            print("Unexpected input.")
        # Register the order in the database TODO
        Database.addOrder(order)
        # Brew the coffee
        self.brewCoffee(coffee)
    #########
    # Prompts credit card info and verifies the payment with bank
    # Returns True if payemnt is successful.
    # Returns False if payment is unsuccessful
    def payWithCard(self, amount):
        print(f"Total: {amount} kr."z
            + "\nPlease input your credit card details."
            + "\n(User hyphens(-) to separate digit pairs)"
        )
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
        return False
    def brewCoffee(self, coffee):
        print("\n"
        + "\n-------------------------------------"
        + f"\nHere is your {coffee.name}."
        + "\nEnjoy!"
        + "\n-------------------------------------\n"
        )
# Calling code
machine = CoffeeMachine()

machine.TMP_initDatabase()
machine.promptCard()
