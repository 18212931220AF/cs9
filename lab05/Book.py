class Book:

    def __init__(self, title = '', author = '', year = None):
        self.title = title
        self.author = author
        self.year = year


    def getTitle(self):
        return self.title


    def getAuthor(self):
        return self.author


    def getYear(self):
        return self.year


    def getBookDetails(self):
        return f'Title: {self.title}, Author: {self.author}, Year: {self.year}'


    def __gt__(self, other):
        if self.author > other.author:
            return True
        elif self.author < other.author:
            return False
        else:
            if self.year > other.year:
                return True
            elif self.year < other.year:
                return False
            else:
                if self.title > other.title:
                    return True
                else:
                    return False
#b = Book("Ready Player One", "Cline, Ernest", 2011)
#print(b.getBookDetails())
