# fakedata.py
# Temporary Class to substitute a database
from user import User

global menu

# menu = {"latte"
#
# }

# Returns None in string form if user not found
# Returns User object if user successfully found
def getUser(cardKey):

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
