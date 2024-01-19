from Pizza import Pizza

class CustomPizza(Pizza):
    
    def __init__(self, size):
        super().__init__(size)
        self.topping = []
        if self.size == 'S':
            self.price = 8.00
        elif self.size == 'M':
            self.price = 10.00
        else:
            self.price = 12.00

    def addTopping(self, topping):
        str = '\t+ ' + topping + '\n'
        self.topping.append(str)
        if self.size == 'S':
            self.price += 0.50
        elif self.size == 'M':
            self.price += 0.75
        else:
            self.price += 1.00

    def getPizzaDetails(self):
        tops = ''
        for topping in range(len(self.topping)):
            tops += self.topping[topping]
        return f'CUSTOM PIZZA\nSize: {self.size}\nToppings:\n{tops}Price: ${self.price:.2f}\n'
