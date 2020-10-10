from Coffee import Coffee

class CustomCoffee(Coffee):
    def __init__(self,firstLayer, secondLayer, thirdLayer, nameId = "CustomCoffee", name = "0", price = 0.00):
        super().__init__(nameId = nameId, name = name, price = price)
        self.firstLayer = firstLayer
        self.secondLayer = secondLayer
        self.thirdLayer = thirdLayer
