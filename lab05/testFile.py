from Book import Book
from BookCollectionNode import BookCollectionNode
from BookCollection import BookCollection


def test_Book():
    b0 = Book("Cujo", "King, Stephen", 1981)
    b1 = Book("The Shining", "King, Stephen", 1977)
    b2 = Book("Ready Player One", "Cline, Ernest", 2011)
    b3 = Book("Rage", "King, Stephen", 1977)
    assert b0.getTitle() == 'Cujo'
    assert b0.getAuthor() == 'King, Stephen'
    assert b0.getYear() == 1981
    assert b0.getBookDetails() == 'Title: Cujo, Author: King, Stephen, Year: 1981'
    assert (b0 > b1) == True

    assert b2.getTitle() == 'Ready Player One'
    assert b2.getAuthor() == 'Cline, Ernest'
    assert b2.getYear() == 2011
    assert b2.getBookDetails() == 'Title: Ready Player One, Author: Cline, Ernest, Year: 2011'
    assert (b2 > b1) == False


def test_BookCollectionNode():
    b0 = Book("Cujo", "King, Stephen", 1981)
    b1 = Book("The Shining", "King, Stephen", 1977)
    b2 = Book("Ready Player One", "Cline, Ernest", 2011)
    b3 = Book("Rage", "King, Stephen", 1977)
    newB0 = BookCollectionNode(b0)
    newB1 = BookCollectionNode(b1)
    newB2 = BookCollectionNode(b2)
    newB3 = BookCollectionNode(b3)

    newB1.setData(b2)
    assert newB1.getData() == b2
    newB2.setNext(b3)
    assert newB2.getNext() == b3
    newB0.setData(b1)
    assert newB0.getData() == b1
    newB3.setNext(b0)
    assert newB3.getNext() == b0
        
    
def test_BookCollection():
    b0 = Book("Cujo", "King, Stephen", 1981)
    b1 = Book("The Shining", "King, Stephen", 1977)
    b2 = Book("Ready Player One", "Cline, Ernest", 2011)
    b3 = Book("Rage", "King, Stephen", 1977)
    bc = BookCollection()
    bc.insertBook(b0)
    bc.insertBook(b1)
    bc.insertBook(b2)
    bc.insertBook(b3)

    assert bc.recursiveSearchTitle("CUJO", bc.head) == True
    assert bc.recursiveSearchTitle("Shining", bc.head) == False

    assert bc.isEmpty() == False
    assert bc.getNumberOfBooks() == 4
    assert bc.getBooksByAuthor("KING, Stephen") == 'Title: Rage, Author: King, Stephen, Year: 1977\n' \
                                    'Title: The Shining, Author: King, Stephen, Year: 1977\n' \
                                    'Title: Cujo, Author: King, Stephen, Year: 1981\n'
    bc.removeAuthor('King, Stephen')
    assert bc.getNumberOfBooks() == 1
    assert bc.getAllBooksInCollection() == 'Title: Ready Player One, Author: Cline, Ernest, Year: 2011\n'
    bc.removeAuthor('Cline, Ernest')
    assert bc.isEmpty() == True

    bc.insertBook('Cujo')
    assert bc.getNumberOfBooks() == 1
    bc.insertBook('Rage')
    assert bc.isEmpty() == False

    
    

    
    

