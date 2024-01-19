from Apartment import Apartment


def mergesort(apartmentList):
    if len(apartmentList) > 1:
        mid = len(apartmentList) // 2
            
        lefthalf = apartmentList[:mid]
        righthalf = apartmentList[mid:]
        
        mergesort(lefthalf)
        mergesort(righthalf)

        i = 0
        j = 0
        k = 0

        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j] or lefthalf[i] == righthalf[j]:
                apartmentList[k] = lefthalf[i]
                i = i + 1
            else:
                apartmentList[k] = righthalf[j]
                j = j + 1
            k = k+1
        while i < len(lefthalf):
            apartmentList[k] = lefthalf[i]
            i = i + 1
            k = k + 1
        while j < len(righthalf):
            apartmentList[k] = righthalf[j]
            j = j + 1
            k = k + 1
                

def ensureSortedAscending(apartmentList):
    for n in range(len(apartmentList)-1):
        if apartmentList[n] > apartmentList[n+1]:
            return False
    return True


def getBestApartment(apartmentList):
    mergesort(apartmentList)
    n = apartmentList[0]
    return n.getApartmentDetails()


def getWorstApartment(apartmentList):
    mergesort(apartmentList)
    n = apartmentList.pop()
    return n.getApartmentDetails()


def getAffordableApartments(apartmentList, budget):
    mergesort(apartmentList)
    n = ''
    for i in range(len(apartmentList)):
        if apartmentList[i].getRent() <= budget:
            if n == '':
               n += apartmentList[i].getApartmentDetails()
            else:
               n += '\n'
               n += apartmentList[i].getApartmentDetails()
    return n


