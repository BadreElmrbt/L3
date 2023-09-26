import numpy as np

#Question 1
def matriceAdjacence(S:list, A:list)->list:
    n = len(S)
    matrice = np.zeros((n, n), dtype=int)
    for arc in A:
        i, j = arc
        matrice[i, j] = 1  # -1 car les indices commencent à 0 dans les tableaux
    return matrice

#Question 2
def matriceAdjacencePond(S:list, A:list)->list:
    n = len(S)
    matrice = np.zeros((n, n), dtype=int)
    for arc in A:
        i, j, p = arc
        matrice[i-1, j-1] = p 
    return matrice

#Question 3
def lireMatriceFichier(nomfichier):
    with open(nomfichier, 'r') as fichier:
        lignes = fichier.readlines()
    matrice = []
    for ligne in lignes:
        valeurs = ligne.strip().split()
        matrice.append([float(val) for val in valeurs])
    return np.array(matrice)

#Question 4
def tousLesSommets(mat:list)->list:
    n = mat.shape[0] #Récupère la taille de la matrice (nombre de lignes/colonnes)
    sommets = []
    for i in range(n):
        sommets.append(i)
    return sommets

#Question 5
def listeArcs(mat):
    n = mat.shape[0]
    arcs = []  
    for i in range(n):
        for j in range(n):
            if mat[i][j] == 1:
                arcs.append((i, j))
    return arcs

# Question 6
def matriceIncidence(mat:list)->list:
    S = tousLesSommets(mat)
    A = listeArcs(mat)
    n = len(S)
    m = len(A)
    mat_incidence = np.zeros((n, m), dtype=int)
    arc_index = 0
    for i in range(n):
        for j in range(n):
            if (i, j) in A:
                mat_incidence[i][arc_index] = 1
                mat_incidence[j][arc_index] = -1
                arc_index += 1
    return mat_incidence

#Question 7
def est_voisin(matAdj:list,S:int,V:int)->bool:
    return matAdj[S][V]!=0

def test_functions():
    S = [0, 1, 2, 3, 4]
    A = [(0,1),(0,2),(1,2),(1,4),(2,3),(3,4),(4,2)]
    matrice0 = matriceAdjacence(S, A)
    print("Matrice d'adjacence:")
    print(matrice0)

    A = [(1, 2, 5), (2, 3, 6), (3, 4, 7), (4, 1, 2)]
    matrice = matriceAdjacencePond(S, A)
    print("\nMatrice d'adjacence pondérée:")
    print(matrice)

    nom_fichier = "UEINF3 - Ateliers de programmation\Atelier_5\graph0.txt"
    matrice = lireMatriceFichier(nom_fichier)
    print("\nMatrice à partir d'un fichier:")
    print(matrice)

    print("\nListe de tous les sommets:")
    print(tousLesSommets(matrice0))

    print("\nListe de tous les arcs:")
    print(listeArcs(matrice0))

    print("\nMatrice d'incidence:")
    mat_incidence = matriceIncidence(matrice0)
    print(mat_incidence)

    print("\nTest de est_voisin : ")
    print(est_voisin(matrice0, 0, 1))

test_functions()