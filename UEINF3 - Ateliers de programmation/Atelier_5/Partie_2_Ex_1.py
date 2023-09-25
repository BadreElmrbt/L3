#Exercice 1

import numpy as np

#Question 1
def my_searchsorted(table:np, indice:int)->int:
    for i in range(len(table)):
        if indice == table[i] :
            return i

arr = np.array([1, 2, 3, 4, 5, 4, 4])
x = np.searchsorted(arr, 4) 
print(x)
y = my_searchsorted(arr,4)
print(y)

#Question 2
def my_where(table:object, indice:int)->list:
    tab = []
    for i in range(len(table)):
        if indice == table[i] :
            tab.append(i)
    return tab

arr = np.array([1, 2, 3, 4, 5, 4, 4])
x = np.where(arr == 4) 
print(x)
y = my_where(arr,4)
print(y)