from Pizza import Pizza
from CustomPizza import CustomPizza
from SpecialtyPizza import SpecialtyPizza

class PizzaOrder:

    def __init__(self, time):
        self.pizzas = []
        self.time = time


    def getTime(self):
        return self.time


    def setTime(self, time):
        self.time = time


    def addPizza(self, pizza):
        self.pizzas.append(pizza)


    def getOrderDescription(self):
        des = ''
        total = 0
        for n in range(len(self.pizzas)):
            total += self.pizzas[n].getPrice()
            des += self.pizzas[n].getPizzaDetails() +'\n' + '----\n'
        return f'******\nOrder Time: {self.time}\n{des}TOTAL ORDER PRICE: ${total:.2f}\n******\n'

