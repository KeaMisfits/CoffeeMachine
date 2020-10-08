# CoffeeMachine.py
from user import User

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

    # TEMPORARY method for testing
    # Returns None in string form if user not found
    # Returns User object if user successfully found
    def TMP_getUser(self, cardKey):

        if cardKey == "qwerty123":
            newUser = User(
            cardKey = "qwerty123",
            name = "Adam",
            surname = "Smith"
            )

            newUser.expirationDate


            return newUser
        else:
            return None

    def promptCard(self):
        print("Please, scan your card")
        # Uses the input from the user, which should be cardKey
        #   to check to which user it belongs by accessing the database
        feedback = self.TMP_getUser(input(cmdPrompt))
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

        while True:
            print("Type '1' for menu or '2' for custom. Type 0 to exit")
            userInput = input(cmdPrompt)

            if userInput == "1":
                break
            elif userInput == "2":
                break
            elif userInput == "0": # 0 Exits the loop
                break
            else:
                print("Unexpected input")


    def buildCoffee(self):
        pass

    def chooseCoffee(self):
        pass

    def checkout(self):
        pass


machine = CoffeeMachine()
machine.promptCard()
machine.chooseDelivery()
