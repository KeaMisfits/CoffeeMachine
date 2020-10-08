# order.py

from datetime import date

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
     def __init__(self, date = date(1990,1,1), revenue = 0):
         self.date = date
         self.revenue = revenue

##################### class end

# List of orders. This is your FAKE DATA. You can add more order.
allOrders = [
Order(date(2020,10,1), 3.50),
Order(date(2020,10,1), 2.95),
Order(date(2020,10,2), 2.50),
Order(date(2020,10,5), 1.50),
Order(date(2020,10,5), 2.95),
Order(date(2020,10,5), 7.95),
]
totalRevenueForOctober1 = 0

for i in range(5):
    if allOrders[i].date == date(2020,10,1):
         totalRevenueForOctober1 += allOrders[1].revenue

print(totalRevenueForOctober1)
