class Apartment:


    def __init__(self, rent, metersFromUCSB, condition):
        self.rent = rent
        self.metersFromUCSB = metersFromUCSB
        self.condition = condition


    def getRent(self):
        return self.rent


    def getMetersFromUCSB(self):
        return self.metersFromUCSB


    def getCondition(self):
        return self.condition


    def getApartmentDetails(self):
        return f'(Apartment) Rent: ${self.rent}, Distance From UCSB: {self.metersFromUCSB}m, Condition: {self.condition}'
    

a0 = Apartment(1204, 200, "bad")
print(a0.getApartmentDetails())
