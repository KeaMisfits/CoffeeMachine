# CoffeeMachine.py
from user import User
import fakedata
import Database

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
    #coffeeAuthorized: boolean = False

    def TMP_initDatabase(self): # Temporary for initializing database without object
        Database.loadUsers()

    def promptCard(self):
        print("Please, scan your card")
        # Uses the input from the user, which should be cardKey
        #   to check to which user it belongs by accessing the database
        feedback = Database.getUser(input(cmdPrompt))
        # At this point we are not sure if the user was found
        #   thus, we make sure by checking whether the return
        #   value is of User type.
        if type(feedback) == type(User(0)): # A dummy user is created
            # If condition passes we know that its a valid user
            self.currentUser = feedback
        else:
            # The condition didn't pass. It must be an error.
            print("Error: Scan failed")

    def chooseDelivery(self):
        print(f"Hi {self.currentUser.name}, what delivery option would you like?")

        userInput = None

        while True: # The loop will exit using 'break' statements.
            print("Type '1' for menu or '2' for custom. Type 0 to exit")
            userInput = input(cmdPrompt)

            if userInput == "1": # Choose from menu
                self.chooseCoffee()
                break
            elif userInput == "2": # Custom
                self.buildCoffee()
                break
            elif userInput == "0": # Exit the loop
                break
            else:
                print("Unexpected input.")

    def buildCoffee(self):
        pass

    def chooseCoffee(self):
        menu = Database.getMenu()
        while True:
            print("Available coffees:")
            for key, coffee in menu.items():
                print(f"{key}\t: {coffee.name} for {coffee.price} kr.")
            print("0\t: <- Go back")
            print("Select the coffee you want")
            userInput = input(cmdPrompt)

            if userInput in menu:
                print(f"debug: you selected {menu[userInput].name}")
                break
            elif userInput == "0":
                self.chooseDelivery()
                return
            else:
                print("Unexpected input.")

    def checkout(self):
        pass
# Main executing code
machine = CoffeeMachine()

machine.TMP_initDatabase()
machine.promptCard()
machine.chooseDelivery()
