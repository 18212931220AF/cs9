class Animal:
    
    def __init__(self, species = None, weight = None, age = None, name = None):
        
        self.species = species
        if self.species != None:
            self.species = species.upper()
        self.weight = weight
        self.age = age
        self.name = name
        if self.name != None:
            self.name = name.upper()

    def setSpecies(self, species):
        self.species = species.upper()

    def setWeight(self, weight):
        self.weight = weight

    def setAge(self, age):
        self.age = age

    def setName(self, name):
        self.name = name.upper()

    def toString(self):
        return f'Species: {self.species}, Name: {self.name}, Age: {self.age}, Weight: {self.weight}'
