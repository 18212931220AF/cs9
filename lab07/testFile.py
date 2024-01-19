from Pizza import Pizza
from CustomPizza import CustomPizza
from SpecialtyPizza import SpecialtyPizza
from PizzaOrder import PizzaOrder
from OrderQueue import OrderQueue

def test_Pizza():
    pizza1 = Pizza('S')
    pizza1.setPrice(10.00)
    assert pizza1.getSize() == 'S'
    assert pizza1.getPrice() == 10.00

    pizza2 = Pizza('L')
    pizza2.setPrice(30.00)
    assert pizza2.getPrice() == 30.00
    assert pizza2.getSize() == 'L'


def test_CustomPizza():
    cp1 = CustomPizza("S")
    assert cp1.getPizzaDetails() == "CUSTOM PIZZA\nSize: S\nToppings:\nPrice: $8.00\n"
    
    cp2 = CustomPizza('M')
    assert cp2.getPizzaDetails() == 'CUSTOM PIZZA\nSize: M\nToppings:\nPrice: $10.00\n'
    

    cp3 = CustomPizza("L")
    cp3.addTopping("extra cheese")
    cp3.addTopping("sausage")
    assert cp3.getPizzaDetails() == "CUSTOM PIZZA\nSize: L\nToppings:\n\t+ extra cheese\n\t+ sausage\nPrice: $14.00\n"

    cp4 = CustomPizza('M')
    cp4.addTopping('beans')
    cp4.addTopping('potato')
    assert cp4.getPizzaDetails() == 'CUSTOM PIZZA\nSize: M\nToppings:\n\t+ beans\n\t+ potato\nPrice: $11.50\n'



def test_PizzaOrder():
    sp1 = SpecialtyPizza('S', 'Carne-more')
    assert sp1.getPizzaDetails() == 'SPECIALTY PIZZA\nSize: S\nName: Carne-more\nPrice: $12.00\n'

    sp2 = SpecialtyPizza('M', 'bbq-chicken')
    assert sp2.getPizzaDetails() == 'SPECIALTY PIZZA\nSize: M\nName: bbq-chicken\nPrice: $14.00\n'

    sp3 = SpecialtyPizza('L', 'Buffalo')
    assert sp3.getPizzaDetails() == 'SPECIALTY PIZZA\nSize: L\nName: Buffalo\nPrice: $16.00\n'


def test_PizzaOrder():
    cp1 = CustomPizza("S")
    cp1.addTopping("extra cheese")
    cp1.addTopping("sausage")
    sp1 = SpecialtyPizza("S", "Carne-more")
    order = PizzaOrder(123000) #12:30:00PM
    order.addPizza(cp1)
    order.addPizza(sp1)
    assert order.getOrderDescription() == "******\nOrder Time: 123000\nCUSTOM PIZZA\nSize: S\nToppings:\n\t+ extra cheese\n\t+ sausage\nPrice: $9.00\n\n----\nSPECIALTY PIZZA\nSize: S\nName: Carne-more\nPrice: $12.00\n\n----\nTOTAL ORDER PRICE: $21.00\n******\n"

    cp2 = CustomPizza('M')
    cp2.addTopping('beans')
    cp2.addTopping('potato')
    sp2 = SpecialtyPizza('M', 'Buffalo')
    order = PizzaOrder(143000)
    order.addPizza(cp2)
    order.addPizza(sp2)
    assert order.getOrderDescription() == "******\nOrder Time: 143000\nCUSTOM PIZZA\nSize: M\nToppings:\n\t+ beans\n\t+ potato\nPrice: $11.50\n\n----\nSPECIALTY PIZZA\nSize: M\nName: Buffalo\nPrice: $14.00\n\n----\nTOTAL ORDER PRICE: $25.50\n******\n"


    
