from Beverage import Beverage

class FruitJuice(Beverage):

    def __init__(self, ounces, price, fruits):
        super().__init__(ounces, price)
        self.fruits = fruits


    def getInfo(self):
        
        fruitslist = self.fruits
        a = ""
        for fru in fruitslist:
            a += fru + "/"
        a = a[:-1]

        s1 = f'{a} Juice, '
        s1 += super().getInfo()
        return s1
            
#juice = FruitJuice(16, 4.5, ["Apple", "Guava"])
#print(juice.getInfo())
