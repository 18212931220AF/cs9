from Book import Book
from BookCollectionNode import BookCollectionNode

class BookCollection:

    def __init__(self):
        self.head = None


    def isEmpty(self):
        return self.head == None


    def getNumberOfBooks(self):
        temp = self.head
        count = 0
        while temp != None:
        	count = count + 1
        	temp = temp.getNext()
        return count


    def insertBook(self, book):
        current = self.head
        previous = None
        stop = False

        while current != None and not stop:
                if current.getData() > book:
                    stop = True
                else:
                    previous = current
                    current = current.getNext()

        temp = BookCollectionNode(book)

        if previous == None:
            temp.setNext(self.head)
            self.head = temp
		
        else:
            temp.setNext(current)
            previous.setNext(temp)

    

    def getBooksByAuthor(self, author):
        current = self.head
        result = ""
        while current != None:
            if current.getData().getAuthor().upper() == author.upper():
                result += str(current.getData().getBookDetails()) + '\n'
            current = current.getNext()
        return result



    def getAllBooksInCollection(self):
        current = self.head
        result = ''
        while current != None:
            result += current.getData().getBookDetails() + '\n'
            current = current.getNext()
        return result

        

    def removeAuthor(self, author):
        current = self.head
        previous = None
        found = False
        while current:
            if current.getData().getAuthor().upper() == author.upper():
                if previous != None:
                    previous.setNext(current.getNext())
                else:
                    self.head = current.getNext()
                current = current.getNext()
            else:
                previous = current
                current = current.getNext()



    def recursiveSearchTitle(self, title, bookNode):
        if bookNode == None:
            return False
        elif bookNode.getData().getTitle().upper() == title.upper():
            return True
        else:
            return self.recursiveSearchTitle(title, bookNode.getNext())
            
     
        

            
        

        
