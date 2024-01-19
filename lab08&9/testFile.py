from Car import Car
from CarInventoryNode import CarInventoryNode
from CarInventory import CarInventory

def test_Car():
    c1 = Car("Honda", "CRV", 2007, 8000)
    c2 = Car('Honda', 'CRV', 2009, 8000)
    assert str(c2) == 'Make: HONDA, Model: CRV, Year: 2009, Price: $8000'
    assert str(c1) == 'Make: HONDA, Model: CRV, Year: 2007, Price: $8000'
    assert c1.year == 2007
    assert c2.model == 'CRV'
    assert c2 > c1

    c3 = Car('Benz', 'C300', 2020, 20000)
    c4 = Car('Benz', 'C300', 2020, 30000)
    assert str(c3) == 'Make: BENZ, Model: C300, Year: 2020, Price: $20000'
    assert c3.price == 20000
    assert c4.make == 'BENZ'
    assert c3 < c4


def test_CarInventoryNode():
    car1 = Car("BMW", "mini", 2013, 3000)
    car2 = Car("dodge", "DaRt", 2003, 5000)
    carNode = CarInventoryNode(car1)
    carNode.cars.append(car2)
    print(carNode)
    assert str(carNode) == 'Make: BMW, Model: MINI, Year: 2013, Price: $3000\nMake: DODGE, Model: DART, Year: 2003, Price: $5000\n'
    car3 = Car('Audi', 'Q5', 2000, 10000)
    carNode1 = CarInventoryNode(car3)
    assert carNode1.getModel() == 'Q5'
    carNode1.cars.append(car1)
    assert str(carNode1) == 'Make: AUDI, Model: Q5, Year: 2000, Price: $10000\nMake: BMW, Model: MINI, Year: 2013, Price: $3000\n'
    


def test_CarInventory():
    bst = CarInventory()

    car1 = Car("Nissan", "Leaf", 2018, 15000)
    car2 = Car("Tesla", "Model3", 2018, 50000)
    car3 = Car("Mercedes", "Sprinter", 2022, 45000)
    car4 = Car("Mercedes", "Sprinter", 2014, 25000)
    car5 = Car("Ford", "Ranger", 2021, 27000)
    bst.addCar(car1)
    bst.addCar(car2)
    bst.addCar(car3)
    bst.addCar(car4)
    bst.addCar(car5)

    assert CarInventoryNode(car1).getMake() == 'NISSAN'
    assert CarInventoryNode(car2).getModel() == 'MODEL3'
    assert CarInventoryNode(car3).getMake() == 'MERCEDES'
    assert CarInventoryNode(car4).getModel() == 'SPRINTER'
    assert bst.doesCarExist(car1) == True
    assert bst.doesCarExist(car3) == True
    assert bst.getBestCar("Nissan", "Leaf") == car1
    assert bst.getBestCar("Mercedes", "Sprinter") == car3
    assert bst.getBestCar("Honda", "Accord") == None
    assert bst.getBestCar('AUDI', 'Q5') == None
    assert bst.getWorstCar("Nissan", "Leaf") == car1
    assert bst.getWorstCar("Mercedes", "Sprinter") == car4
    assert bst.getBestCar("Honda", "Accord") == None
    assert bst.getBestCar('AUDI', 'Q5') == None
    assert bst.getTotalInventoryPrice() == 162000
    assert bst.inOrder() == \
"""\
Make: FORD, Model: RANGER, Year: 2021, Price: $27000
Make: MERCEDES, Model: SPRINTER, Year: 2022, Price: $45000
Make: MERCEDES, Model: SPRINTER, Year: 2014, Price: $25000
Make: NISSAN, Model: LEAF, Year: 2018, Price: $15000
Make: TESLA, Model: MODEL3, Year: 2018, Price: $50000
"""
    assert bst.preOrder() == \
"""\
Make: NISSAN, Model: LEAF, Year: 2018, Price: $15000
Make: MERCEDES, Model: SPRINTER, Year: 2022, Price: $45000
Make: MERCEDES, Model: SPRINTER, Year: 2014, Price: $25000
Make: FORD, Model: RANGER, Year: 2021, Price: $27000
Make: TESLA, Model: MODEL3, Year: 2018, Price: $50000
"""
    assert bst.postOrder() == \
"""\
Make: FORD, Model: RANGER, Year: 2021, Price: $27000
Make: MERCEDES, Model: SPRINTER, Year: 2022, Price: $45000
Make: MERCEDES, Model: SPRINTER, Year: 2014, Price: $25000
Make: TESLA, Model: MODEL3, Year: 2018, Price: $50000
Make: NISSAN, Model: LEAF, Year: 2018, Price: $15000
"""
    

def test_getSuccessor():
    bst = CarInventory()
    car1 = Car("Mazda", "CX-5", 2022, 25000)
    car2 = Car("Tesla", "Model3", 2018, 50000)
    car3 = Car("BMW", "X5", 2022, 60000)
    car4 = Car("BMW", "X5", 2020, 58000)
    car5 = Car("Audi", "A3", 2021, 25000)
    bst.addCar(car1)
    bst.addCar(car2)
    bst.addCar(car3)
    bst.addCar(car4)
    bst.addCar(car5)
    assert bst.getSuccessor('Mazda', 'CX-5') == 'Make: TESLA, Model: MODEL3, Year: 2018, Price: $50000'
    assert bst.getSuccessor('Tesla', 'Model3') == None
    assert bst.getSuccessor('BMW', 'X5') == None
    assert bst.getSuccessor('Audi', 'A3') == None


def test_remove():
    bst = CarInventory()
    car1 = Car("Mazda", "CX-5", 2022, 25000)
    car2 = Car("Tesla", "Model3", 2018, 50000)
    car3 = Car("BMW", "X5", 2022, 60000)
    car4 = Car("BMW", "X5", 2020, 58000)
    car5 = Car("Audi", "A3", 2021, 25000)
    bst.addCar(car1)
    bst.addCar(car2)
    bst.addCar(car3)
    bst.addCar(car4)
    bst.addCar(car5)
    bst.removeCar("BMW", "X5", 2020, 58000)
    assert bst.inOrder() == \
"""\
Make: AUDI, Model: A3, Year: 2021, Price: $25000
Make: BMW, Model: X5, Year: 2022, Price: $60000
Make: MAZDA, Model: CX-5, Year: 2022, Price: $25000
Make: TESLA, Model: MODEL3, Year: 2018, Price: $50000
"""
    assert bst.preOrder() == \
"""\
Make: MAZDA, Model: CX-5, Year: 2022, Price: $25000
Make: BMW, Model: X5, Year: 2022, Price: $60000
Make: AUDI, Model: A3, Year: 2021, Price: $25000
Make: TESLA, Model: MODEL3, Year: 2018, Price: $50000
"""
    assert bst.postOrder() == \
"""\
Make: AUDI, Model: A3, Year: 2021, Price: $25000
Make: BMW, Model: X5, Year: 2022, Price: $60000
Make: TESLA, Model: MODEL3, Year: 2018, Price: $50000
Make: MAZDA, Model: CX-5, Year: 2022, Price: $25000
"""

    
    bst.removeCar("BMW", "X5", 2022, 60000)
    assert bst.inOrder() == \
"""\
Make: AUDI, Model: A3, Year: 2021, Price: $25000
Make: MAZDA, Model: CX-5, Year: 2022, Price: $25000
Make: TESLA, Model: MODEL3, Year: 2018, Price: $50000
"""
    assert bst.preOrder() == \
"""\
Make: MAZDA, Model: CX-5, Year: 2022, Price: $25000
Make: AUDI, Model: A3, Year: 2021, Price: $25000
Make: TESLA, Model: MODEL3, Year: 2018, Price: $50000
"""
    assert bst.postOrder() == \
"""\
Make: AUDI, Model: A3, Year: 2021, Price: $25000
Make: TESLA, Model: MODEL3, Year: 2018, Price: $50000
Make: MAZDA, Model: CX-5, Year: 2022, Price: $25000
"""
    
    
