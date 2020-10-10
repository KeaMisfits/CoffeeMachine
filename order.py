# order.py
from datetime import date

nextId = 0
def getNextId():
    global nextId
    nextId += 1
    return nextId


class Order(object):
##################### class start
     ####
     # Initialization method.
     # It also assigns default values for date and revenue.
     # Create a new obejct of class Order by:
     # myVariable = Order(date(2020, 10, 1), 4.50)
     # The above will create an order at 2020-10-01 for 4.50 kr.
     # Access the new order variables by:
     # orderDate = myVariable.date
     # orderRevenue = myVariable.revenue
     ###
    def __init__(self, id = 0, date = date(1990,1,1), revenue = 0):
        self.id = getNextId()
        self.date = date
        self.revenue = revenue
    # def myGet(self):
    #     print(self.id,",",self.date,",",self.revenue)


##################### class end

#oneOrder = Order()
#print(oneOrder.revenue)
#rint(oneOrder.date)
