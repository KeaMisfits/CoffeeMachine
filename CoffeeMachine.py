# CoffeeMachine.py
from user import User

class CoffeeMachine(object):

    cmdPrompt = "> "

    #availableProducts: dict
    #availableProducts: dict
    #cardKey: str
    currentUser = None
    #coffeeAuthorized: boolean = False

    # TEMPORARY method for testing
    # Returns None in string form if user not found
    # Returns User object if user successfully found
    def TMP_getUser(self, cardKey):

        if cardKey == "qwerty123":
            return User(
            id = 1000,
            cardKey = "qwerty123",
            name = "Adam",
            surname = "Smith"
            )
        else:
            return None

    def promptCard(self):
        print("Please, scan your card")
        #cardKey = input(cmdPrompt)

        # Uses the input cardKey to check to which user it belongs
        #   by accessing the database
        feedback = self.TMP_getUser("qwerty123")
        # At this point we are not sure if the user was found
        #   thus, we make sure by checking whether the return
        #   value is of User type.
        if type(feedback) == type(User(0,0)): # A dummy user is created
            # If condition passes we know that its a valid user
            self.currentUser = feedback

            print(self.currentUser.name)
        else:
            # The condition didn't pass. It must be an error.
            print("Error: Scan failed")

    def chooseDelivery(self):
        print(
        f"Hi {self.currentUser.name}, what delivery option would you like?",
        "\nType '1' for menu or '2' for custom"
        )

    def buildCoffee(self):
        pass



machine = CoffeeMachine()
machine.promptCard()
machine.chooseDelivery()
