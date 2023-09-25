#Exercice 2

import numpy as np

#Question 1
def my_add(tableA : object, tableB : object)->object:
    if tableA.shape == tableB.shape:
        return tableA + tableB

A = np.array(([3,1],[6,4])) 
B = np.array(([1,8],[4,2])) 

print(my_add(A,B))

#1 - Création de matrices
A = np.random.randint(0, 11, (4, 4))  # Crée une matrice 4x4 avec des valeurs aléatoires entre 0 et 10.
I = np.eye(4)  # Crée une matrice identité 4x4.

#2 - Fonctions à définir
def matrice_trace(matrice:object)->float:
    if len(matrice) != len(matrice[0]):
        raise ValueError("La matrice doit être carrée pour calculer la trace.")
    trace = 0
    for i in range(len(matrice)):
        trace += matrice[i][i]
    return trace

def est_symetrique(matrice:object)->bool:
    n = len(matrice)
    for i in range(n):
        for j in range(i+1, n):
            if matrice[i][j] != matrice[j][i]:
                return False
    return True

def produit_diagonal(matrice:object)->float:
    if len(matrice) != len(matrice[0]):
        raise ValueError("La matrice doit être carrée pour calculer le produit de la diagonale.")
    produit = 1
    for i in range(len(matrice)):
        produit *= matrice[i][i]
    return produit

#3 - Application des fonctions
trace_A = matrice_trace(A)
print("Matrice A :\n",A)
print(f"\nTrace de A : {trace_A}")

symetrique_A = est_symetrique((A+A.T)/2)
print(f"Est-ce que a est symétrique ? {symetrique_A}")

produitD_I = produit_diagonal(I)
print(f"Produit diagonal de A : {produitD_I}\n")

#4 - Manipulation supplémentaire
A_inverse = np.linalg.inv(A) #Calcul de l'inverse de A
resultat = np.dot(A, A_inverse) #Calcul du produit de A par son inverse

print("A*A^-1 :\n",abs(resultat.round()))