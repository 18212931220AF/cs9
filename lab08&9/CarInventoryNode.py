from Car import Car

class CarInventoryNode:

    def __init__(self, car):
        self.cars = [car]
        self.make = car.make.upper()
        self.model = car.model.upper()
        self.parent = None
        self.left = None
        self.right = None


    def getMake(self):
        return self.make

    def getModel(self):
        return self.model

    def getParent(self):
        return self.parent

    def setParent(self, parent):
        self.parent = parent

    def getLeft(self):
        return self.left

    def setLeft(self, left):
        self.left = left

    def getRight(self):
        return self.right

    def setRight(self, right):
        self.right = right

    def __str__(self):
        s = ''
        for n in self.cars:
            s += str(n) + '\n'
        return s

#car1 = Car("Dodge", "dart", 2015, 6000)
#car2 = Car("dodge", "DaRt", 2003, 5000)
#carNode = CarInventoryNode(car1)
#carNode.cars.append(car2)
#print(carNode)


    def isLeftChild(self):
        return self.parent and self.parent.left == self

    def isRightChild(self):
        return self.parent and self.parent.right == self

    def isLeaf(self):
        return not (self.right or self.left)

    def hasAnyChildren(self):
        return self.right or self.left

    def hasBothChildren(self):
        return self.right and self.left

    def replaceNodeData(self, make, model, cars, lc, rc):
        self.make = make
        self.model = model
        self.cars = cars
        self.left = lc
        self.right = rc
        if self.getLeft():
            self.left.parent = self
        if self.getRight():
            self.right.parent = self

    def findMin(self):
        current = self
        while current.getLeft():
            current = current.left
        return current


    def spliceOut(self):
        if self.isLeaf():
            if self.isLeftChild():
                self.parent.left = None
            else:
                self.parent.right = None
        elif self.hasAnyChildren():
            if self.getLeft():
                if self.isLeftChild():
                    self.parent.left = self.left
                else:
                    self.parent.right = self.left
                self.right.parent = self.parent
            else:
                if self.isLeftChild():
                    self.parent.left = self.right
                else:
                    self.parent.right = self.right



                    
