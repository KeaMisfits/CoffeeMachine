from datetime import date

class User(object):

	# Probably the following is redundant but cooming from Java
	# 	I feel like its handy to have a list of object
	#	variables at the top of the class
	name = None
	surname = None
	cardKey = None
	# ---

	expirationDate = date(1990, 1, 1)
	lastFreeCoffeeDate = date(1990, 1, 1)

	def __init__(self, cardKey, name = "Unknown", surname = "Unknown"):
		self.cardKey = cardKey
		self.name = name
		self.surname = surname

	def isActiveMember(self):
		if self.expiration > date.today(): # Checks if expiration date is later than today.
			return True
		return False

	def isFreeCoffee(self):
		if self.isActiveMember() == False:
			return False
		else:
			now = date.today()
			if now.year > self.lastFreeCoffeeDate.year:
				return True
			elif now.month > self.lastFreeCoffeeDate.month:
				return True
			elif now.day > self.lastFreeCoffeeDate.day:
				return True
			else:
				return False


# user = User(1001, "testId")
# user.expiration = date(2020, 10, 10)
# user.lastFreeCoffeeDate = date(2020, 10, 7)
# print(date.today())
# print(user.isFreeCoffee())
