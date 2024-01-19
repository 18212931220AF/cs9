from Beverage import Beverage
from Coffee import Coffee
from FruitJuice import FruitJuice
from DrinkOrder import DrinkOrder


def test_Beverage():
        a1 = Beverage(20, 15.8)
        assert (a1.getInfo()) == '20 oz, $15.80'
        a2 = Beverage(30, 17.6)
        assert (a2.getInfo()) == '30 oz, $17.60'
        

def test_Coffee():
        b1 = Coffee(10, 3.456, 'Latte')
        assert (b1.getInfo()) == 'Latte Coffee, 10 oz, $3.46'
        b2 = Coffee(15, 3.000, 'Cold Brew')
        assert (b2.getInfo()) == 'Cold Brew Coffee, 15 oz, $3.00'
        
        
def test_FruitJuice():
        c1 = FruitJuice(20, 6.789, ['Banana', 'Grape'])
        assert (c1.getInfo()) == 'Banana/Grape Juice, 20 oz, $6.79'
        c2 = FruitJuice(25, 12.1, ['Watermelon', 'Pear'])
        assert (c2.getInfo()) == 'Watermelon/Pear Juice, 25 oz, $12.10'

        
def test_getTotalOrder():
        d1 = Coffee(10, 3.456, 'Latte')
        d2 = FruitJuice(20, 6.789, ['Banana', 'Grape'])
        order = DrinkOrder()
        order.addBeverage(d1)
        order.addBeverage(d2)
        assert order.getTotalOrder() == 'Order Items:\n* Latte Coffee, 10 oz, $3.46\n* Banana/Grape Juice, 20 oz, $6.79\nTotal Price: $10.24'

        d3 = Coffee(15, 3.000, 'Cold Brew')
        d4 = FruitJuice(25, 12.1, ['Watermelon', 'Pear'])
        order = DrinkOrder()
        order.addBeverage(d3)
        order.addBeverage(d4)
        assert order.getTotalOrder() == 'Order Items:\n* Cold Brew Coffee, 15 oz, $3.00\n* Watermelon/Pear Juice, 25 oz, $12.10\nTotal Price: $15.10'


