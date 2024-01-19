def multiply(x, y):
    if x == 0 or y == 0:
        return 0
    return x + multiply(x, y-1)


def collectMultiples(intList, n):
    if intList == []:
        return intList
    elif intList[0] % n!=0:
        return collectMultiples(intList[1:], n)
    else:
        return [intList[0]] + collectMultiples(intList[1:], n)


def countVowels(s):
    if not s:
        return 0
    elif s[0] in ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u']:
        return 1 + countVowels(s[1:])
    else:
        return countVowels(s[1:])


def reverseVowels(s):
    if not s:
        return s
    elif s[-1] in ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u']:
        return s[-1] + reverseVowels(s[:-1])
    else:
        return reverseVowels(s[:-1])

  
def removeSubString(s:str,sub:str):

    first_index =  s.find(sub)
    if first_index == -1:
        return s
    else:
        list_s = list(s)  
        for i in range(len(sub)):
            list_s.pop(first_index)  

        new_s = ''.join(list_s)  
        return removeSubString(new_s,sub)
