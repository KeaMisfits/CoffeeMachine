from datetime import datetime
#helloow
#HEELLO EHLLLo
#Heyyy
class User(object):

	expirationDate = datetime(1990, 1, 1)
	lastFreeCoffeeDate = datetime(1990, 1, 1)

	def isActiveMember(self):
		if self.expiration > datetime.now():
			return True
		return False

	def isFreeCoffee(self):
		if self.isActiveMember() == False:
			return False
		else:
			now = datetime.now()
			if now.year > self.lastFreeCoffeeDate.year:
				return True
			elif now.month > self.lastFreeCoffeeDate.month:
				return True
			elif now.day > self.lastFreeCoffeeDate.day:
				return True
			else:
				return False


user = User()
user.expiration = datetime(2020, 10, 10)
user.lastFreeCoffeeDate = datetime(2020, 10, 7)

print(user.isFreeCoffee())
