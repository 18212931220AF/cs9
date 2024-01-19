
from Car import Car
from CarInventoryNode import CarInventoryNode

class CarInventory:

    def __init__(self):
        self.root = None
        

    def addCar(self, car):
        if self.root == None:
            self.root = CarInventoryNode(car)
        else:
            self._addCar(car, self.root)
            

    def _addCar(self, car, newCarInventoryNode):
        if car.make == newCarInventoryNode.getMake() and car.model == newCarInventoryNode.getModel():
            newCarInventoryNode.cars.append(car)
        elif car < newCarInventoryNode:
            if newCarInventoryNode.getLeft() != None:
                self._addCar(car, newCarInventoryNode.getLeft())
            else:
                newCarInventoryNode.setLeft(CarInventoryNode(car))
                CarInventoryNode(car).setParent(newCarInventoryNode)

        else:
            if newCarInventoryNode.getRight() != None:
                self._addCar(car, newCarInventoryNode.getRight())
            else:
                newCarInventoryNode.setRight(CarInventoryNode(car))
                CarInventoryNode(car).setParent(newCarInventoryNode)

      
         

    def doesCarExist(self, car):
        if self.root == None:
            return False
        else:
            ret = self._doesCarExist(car, self.root)
            if ret != None:
                for n in ret.cars:
                    if n == car:
                        return True

        return False


    def _doesCarExist(self, car, newCarInventoryNode):
        if newCarInventoryNode == None:
            return None
        elif car.make == newCarInventoryNode.getMake() and car.model == newCarInventoryNode.getModel():
            return newCarInventoryNode
        elif car < newCarInventoryNode:
            return self._doesCarExist(car, newCarInventoryNode.getLeft())
        else:
            return self._doesCarExist(car, newCarInventoryNode.getRight())
        
                

    def inOrder(self):
        return self._inOrder(self.root)


    def _inOrder(self, newCarInventoryNode):
        ret = ''
        if newCarInventoryNode != None:
            ret += self._inOrder(newCarInventoryNode.getLeft())
            ret += str(newCarInventoryNode)
            ret += self._inOrder(newCarInventoryNode.getRight())
        return ret
    

    def preOrder(self):
        return self._preOrder(self.root)
    

    def _preOrder(self, newCarInventoryNode):
        ret = ''
        if newCarInventoryNode != None:
            ret += str(newCarInventoryNode)
            ret += self._preOrder(newCarInventoryNode.getLeft())
            ret += self._preOrder(newCarInventoryNode.getRight())
        return ret


    def postOrder(self):
        return self._postOrder(self.root)
    

    def _postOrder(self, newCarInventoryNode):
        ret = ''
        if newCarInventoryNode != None:
            ret += self._postOrder(newCarInventoryNode.getLeft())
            ret += self._postOrder(newCarInventoryNode.getRight())
            ret += str(newCarInventoryNode)
        return ret

    
    def getBestCar(self, make, model):
        ret = self._getCar(make, model, self.root)
        if ret == None:
            return None
        else:
            bestCar = ret.cars[0]
            for n in ret.cars:
                if n > bestCar:
                    bestCar = n
        return bestCar


    def getWorstCar(self, make, model):
        ret = self._getCar(make, model, self.root)
        if ret == None:
            return None
        else:
            worstCar = ret.cars[0]
            for n in ret.cars:
                if n < worstCar:
                    worstCar = n
        return worstCar
            
        
    def _getCar(self, make, model, newCarInventoryNode):
        if not newCarInventoryNode:
            return None
        elif newCarInventoryNode.getMake() == make.upper() and newCarInventoryNode.getModel() == model.upper():
            return newCarInventoryNode
        elif newCarInventoryNode.getMake() < make.upper():
            return self._getCar(make, model, newCarInventoryNode.getRight())
        elif newCarInventoryNode.getMake() == make.upper() and newCarInventoryNode.getModel() < model.upper():
            return self._getCar(make, model, newCarInventoryNode.getRight())
        elif newCarInventoryNode.getMake() > make.upper():
            return self._getCar(make, model, newCarInventoryNode.getLeft())
        elif newCarInventoryNode.getMake() == make.upper() and newCarInventoryNode.getModel() > model.upper():
            return self._getCar(make, model, newCarInventoryNode.getLeft())


    def getTotalInventoryPrice(self):
        return self._getTotalInventoryPrice(self.root)


    def _getTotalInventoryPrice(self, newCarInventoryNode):
        pri = 0
        if newCarInventoryNode == None:
            return 0
        else:
            pri += self._getTotalInventoryPrice(newCarInventoryNode.getLeft())
            for n in newCarInventoryNode.cars:
                pri += n.price
            pri += self._getTotalInventoryPrice(newCarInventoryNode.getRight())
            return pri

        


    def getSuccessor(self, make, model):
        succ = None
        res = self._getCar(make, model, self.root)
        if res != None:
            if res.getRight():
                succ = res.findMin()
                succ = res.getRight().findMin()
            else:
                if res.getParent():
                    if res.isLeftChild():
                        succ = res.getParent()
                    else:
                        res.getParent().right = None
                        succ = self.getSuccessor(res.parent.make, res.parent.model)
                        res.getParent().setRight(res)
        return succ
    


    def remove(self,currentNode):
        if currentNode.isLeaf():
            if currentNode == currentNode.parent.left:
                currentNode.parent.left = None
            else:
                currentNode.parent.right = None
        elif currentNode.hasBothChildren():
            succ = self.getSuccessor(currentNode.make, currentNode.model)
            succ.spliceOut()
            currentNode.make = succ.make
            currentNode.model = succ.model
            currentNode.cars = succ.cars
        else:
            if currentNode.getLeft():
                if currentNode.isLeftChild():
                    currentNode.left.parent = currentNode.parent
                    currentNode.parent.left = currentNode.left
                elif currentNode.isRightChild():
                    currentNode.left.parent = currentNode.parent
                    currentNode.parent.right = currentNode.left
                else:
                    currentNode.replaceNodeData(currentNode.left.make, currentNode.left.model, currentNode.left.cars,
                                                currentNode.left.left, currentNode.left.right)         
            else:
                if currentNode.isLeftChild():
                    currentNode.right.parent = currentNode.parent
                    currentNode.parent.left = currentNode.right
                elif currentNode.isRightChild():
                    currentNode.right.parent = currentNode.parent
                    currentNode.parent.right = currentNode.right
                else:
                    currentNode.replaceNodeData(currentNode.right.make, currentNode.right.model, currentNode.right.cars,
                                                currentNode.right.left, currentNode.right.right)



    def removeCar(self, make, model, year, price):
        car = Car(make, model, year, price)
        res = self._getCar(make, model, self.root)
        if res == None:
            return False
        else:
            if car in res.cars:
                for n in res.cars:
                    if n == car:
                        res.cars.remove(n)
                if len(res.cars) != 0:
                    return True
                if len(res.cars) == 0:
                    if self.root and (self.root.getLeft() or self.root.getRight()):
                        self.remove(res)
                        return True
                    else:
                        self.root = None
                        return True
            else:
                return False

        return False

   
'''
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
print(bst.inOrder())
bst.removeCar("BMW", "X5", 2022, 60000)
print(bst.inOrder())
'''


