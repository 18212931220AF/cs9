from Animal import Animal

class AnimalShelter:
    def __init__(self):
        self.animalShelter = {}

    def addAnimal(self,animal):
        self.animalShelter.setdefault(animal.species,[]).append(animal)
        print(self.animalShelter)
            

    def removeAnimal(self, animal):
        if animal.species in self.animalShelter:
            for i in self.animalShelter[animal.species]:
                if (i.species == animal.species) and (i.weight == animal.weight) and (i.age == animal.age) and (i.name == animal.name):
                    self.animalShelter.pop(animal.species)


    def removeSpecies(self,sepcies):
        if sepcies.upper() in self.animalShelter.keys() or sepcies in self.animalShelter.keys():
            del self.animalShelter[sepcies.upper()]
        print(self.animalShelter)


    def getAnimalsBySpecies(self, species):
        result = ""
        if species.upper() in self.animalShelter.keys():
            for temp_animal in self.animalShelter[species.upper()]:
                result += temp_animal.toString()
                if temp_animal != self.animalShelter[species.upper()][-1]:
                    result += "\n"
        return result


    def doesAnimalExist(self, animal):
        if animal.species in self.animalShelter.keys():
            if animal in self.animalShelter[animal.species]:
                return True
        else:
            return False
