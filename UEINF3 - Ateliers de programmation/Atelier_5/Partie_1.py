def somme_recursive(liste:list)->int:
    if len(liste)==1:
        return liste[0]
    else :
        return liste[0] + somme_recursive(liste[1:])
    
def factorielle(x):
    if x == 0 :
        return 1
    else :
        return factorielle(x-1)*x
    
def longueur(lst:list)->int:
    if len(lst)==0:
        return 0
    else :
        return 1 + longueur(lst[1:])

def findMin(lst:list)->int:
    mini = None
    if len(lst)==0:
        mini = None
    elif len(lst)==1:
        mini = lst[0]
    else :
        mini = findMin(lst[1:])
        if lst[0] < mini :
            mini = lst[0]
    return mini

def listPairs(lst: list) -> list:
    if len(lst) == 0:
        return []
    elif len(lst) == 1:
        if lst[0] % 2 == 0:
            return lst
        else:
            return []
    else:
        if lst[0] % 2 == 0:
            return [lst[0]] + listPairs(lst[1:])
        else:
            return listPairs(lst[1:])

def concat_list(lst:list)->list:
    if lst==[]:
        return []
    else :
        return lst[0] + concat_list(lst[1:])

def separe(lst:list)->list:
    if len(lst)==0:
        return [],[]
    pairs,impairs = separe(lst[1:])
    if lst[0] %2  == 0 :
        return [lst[0]] + pairs, impairs
    else :
        return pairs, [lst[0]] + impairs

print(somme_recursive([1,2,3,4,5]))
print(factorielle(5)) 
print(longueur([1,2,3,4,5,6]))
print(findMin([5,1,3,-5]))
print(listPairs([1,2,3,45,6]))
print(concat_list([[1,2,3,45,6],["a","b"]]))
print(separe([1,2,3,4,5,6]))

