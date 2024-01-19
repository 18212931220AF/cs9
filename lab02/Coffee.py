from Beverage import Beverage

class Coffee(Beverage):
    
    def __init__(self, ounces, price, style = str):
        super().__init__(ounces, price)
        self.style = style

    def getInfo(self):
        s = f'{self.style} Coffee, '
        s += super().getInfo()
        return s



        
#c1 = Coffee(8, 3.0, "Espresso")
#c1.getInfo()
        
