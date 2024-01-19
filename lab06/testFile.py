from Apartment import Apartment
from lab06 import mergesort
from lab06 import ensureSortedAscending
from lab06 import getBestApartment
from lab06 import getWorstApartment
from lab06 import getAffordableApartments


def test_getRent():
    a0 = Apartment(1115, 215, "bad")
    assert a0.getRent() == 1115
    a1 = Apartment(950, 215, "average")
    assert a1.getRent() == 950


def test_getMetersFromUCSB():
    a2 = Apartment(950, 215, "excellent")
    assert a2.getMetersFromUCSB() == 215
    a3 = Apartment(950, 190, "excellent")
    assert a3.getMetersFromUCSB() == 190


def test_getCondition():
    a4 = Apartment(900, 190, "excellent")
    assert a4.getCondition() == 'excellent'
    a5 = Apartment(500, 250, "bad")
    assert a5,getCondition() == 'bad'


def test_getApartmentDetails():
    a0 = Apartment(1115, 215, "bad")
    a1 = Apartment(950, 215, "average")
    a2 = Apartment(950, 215, "excellent")
    a3 = Apartment(950, 190, "excellent")
    a4 = Apartment(900, 190, "excellent")
    a5 = Apartment(500, 250, "bad")
    assert a0.getApartmentDetails() == '(Apartment) Rent: $1115, Distance From UCSB: 215m, Condition: bad'
    assert a2.getApartmentDetails() == '(Apartment) Rent: $950, Distance From UCSB: 215m, Condition: excellent'
    assert a5.getApartmentDetails() == '(Apartment) Rent: $500, Distance From UCSB: 250m, Condition: bad'


def test_ensureSortedAscending():
    a0 = Apartment(1115, 215, "bad")
    a1 = Apartment(950, 215, "average")
    a2 = Apartment(950, 215, "excellent")
    a3 = Apartment(950, 190, "excellent")
    a4 = Apartment(900, 190, "excellent")
    a5 = Apartment(500, 250, "bad")
    apartmentList = [a0, a1, a2, a3, a4, a5]
    assert ensureSortedAscending(apartmentList) == False
    mergesort(apartmentList)
    assert ensureSortedAscending(apartmentList) == True


def test_getBestApartment():
    a0 = Apartment(1115, 215, "bad")
    a1 = Apartment(950, 215, "average")
    a2 = Apartment(950, 215, "excellent")
    a3 = Apartment(950, 190, "excellent")
    a4 = Apartment(900, 190, "excellent")
    a5 = Apartment(500, 250, "bad")
    apartmentList1 = [a0, a1, a2, a3, a4, a5]
    assert getBestApartment(apartmentList1) == '(Apartment) Rent: $500, Distance From UCSB: 250m, Condition: bad'
    b0 = Apartment(1000, 500, 'bad')
    b1 = Apartment(600, 300, 'average')
    b2 = Apartment(900, 200, 'excellent')
    apartmentList2 = [b0, b1, b2]
    assert getBestApartment(apartmentList2) == '(Apartment) Rent: $600, Distance From UCSB: 300m, Condition: average'
    c0 = Apartment(1200, 300, 'excellent')
    c1 = Apartment(2000, 100, 'average')
    c2 = Apartment(1500, 200, 'bad')
    apartmentList3 = [c0, c1, c2]
    assert getBestApartment(apartmentList3) == '(Apartment) Rent: $1200, Distance From UCSB: 300m, Condition: excellent'


def test_getWorstApartment():
    a0 = Apartment(1115, 215, "bad")
    a1 = Apartment(950, 215, "average")
    a2 = Apartment(950, 215, "excellent")
    a3 = Apartment(950, 190, "excellent")
    a4 = Apartment(900, 190, "excellent")
    a5 = Apartment(500, 250, "bad")
    apartmentList1 = [a0, a1, a2, a3, a4, a5]
    assert getWorstApartment(apartmentList1) == '(Apartment) Rent: $1115, Distance From UCSB: 215m, Condition: bad'
    b0 = Apartment(1000, 500, 'bad')
    b1 = Apartment(600, 300, 'average')
    b2 = Apartment(900, 200, 'excellent')
    apartmentList2 = [b0, b1, b2]
    assert getWorstApartment(apartmentList2) == '(Apartment) Rent: $1000, Distance From UCSB: 500m, Condition: bad'
    c0 = Apartment(1200, 300, 'excellent')
    c1 = Apartment(2000, 100, 'average')
    c2 = Apartment(1500, 200, 'bad')
    apartmentList3 = [c0, c1, c2]
    assert getWorstApartment(apartmentList3) == '(Apartment) Rent: $2000, Distance From UCSB: 100m, Condition: average'

    

def test_getAffordableApartments():
    a0 = Apartment(1115, 215, "bad")
    a1 = Apartment(950, 215, "average")
    a2 = Apartment(950, 215, "excellent")
    a3 = Apartment(950, 190, "excellent")
    a4 = Apartment(900, 190, "excellent")
    a5 = Apartment(500, 250, "bad")
    apartmentList1 = [a0, a1, a2, a3, a4, a5]
    assert getAffordableApartments(apartmentList1, 500) == '(Apartment) Rent: $500, Distance From UCSB: 250m, Condition: bad'

    c0 = Apartment(1200, 300, 'excellent')
    c1 = Apartment(2000, 100, 'average')
    c2 = Apartment(1500, 200, 'bad')
    apartmentList3 = [c0, c1, c2]
    assert getAffordableApartments(apartmentList3, 1300) == '(Apartment) Rent: $1200, Distance From UCSB: 300m, Condition: excellent'



    

