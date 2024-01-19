from Beverage import Beverage
from Coffee import Coffee
from FruitJuice import FruitJuice

class DrinkOrder:

    def __init__(self):
        self.drinks = []

    def addBeverage(self, beverage):
        self.drinks.append(beverage)


    def getTotalOrder(self):
        
        if self.drinks != []:
          s2 = "Order Items:\n"
          totalprice = 0
          for drink in self.drinks:
              totalprice += drink.getPrice()
              s2 += '* ' + drink.getInfo() +'\n'
          s2 += f'Total Price: ${totalprice:.2f}'
          return s2
        else:
          return f'Order Items:\nTotal Price: $0.00'


