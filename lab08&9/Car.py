class Car:

    def __init__(self, make, model, year, price):
        self.make = make.upper()
        self.model = model.upper()
        self.year = year
        self.price = price


    def __gt__(self, other):
        if self.make > other.make:
            return True
        elif self.make < other.make:
            return False
        else:
            if self.model > other.model:
                return True
            elif self.model < other.model:
                return False
            else:
                if self.year > other.year:
                    return True
                elif self.year < other.year:
                    return False
                else:
                    if self.price > other.price:
                        return True
                    else:
                        return False


    def __lt__(self, other):
        if self.make < other.make:
            return True
        elif self.make > other.make:
            return False
        else:
            if self.model < other.model:
                return True
            elif self.model > other.model:
                return False
            else:
                if self.year < other.year:
                    return True
                elif self.year > other.year:
                    return False
                else:
                    if self.price < other.price:
                        return True
                    else:
                        return False


    def __eq__(self, other):
        if self.make == other.make and self.model == other.model and self.year == other.year and self.price == other.price:
            return True
        else:
            return False


    def __str__(self):
        return f'Make: {self.make}, Model: {self.model}, Year: {self.year}, Price: ${self.price}'


#c = Car("Honda", "CRV", 2007, 8000)
#print(c)


