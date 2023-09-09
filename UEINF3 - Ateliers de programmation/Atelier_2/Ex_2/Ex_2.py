#Question 1
def position1(lst:list,elt:int)->int:
    """Retourne l'indice de l'entier elt dans la liste lst avec une boucle for
    Args:
        lst (list): liste d'entiers
        elt (int): entier à rechercher dans la liste
    Returns:
        int: indice
    """
    if elt in lst :
        for i in range (len(lst)):
            if lst[i]==elt :
                indice = i
    else :
        indice = -1
    return indice

def position2(lst:list,elt:int)->int:
    """Retourne l'indice de l'entier elt dans la liste lst avec une boucle while
    Args:
        lst (list): liste d'entiers
        elt (int): entier à rechercher dans la liste
    Returns:
        int: indice
    """
    compteur = 0
    indice = -1
    while compteur < len(lst):
        if lst[compteur] == elt :
            indice = compteur
            compteur = len(lst)
        else :
            compteur += 1
    return indice

#Question 2
def nb_occurrences(lst:int,e:int)->int:
    """Retourne le nombre d'occurences de l'entier e dans liste lst
    Args:
        lst (list): liste d'entiers
        e (int): entier dont on cherche le nombre d'occurrences
    Returns:
        int: occurrence(s) de e dans lst
    """
    compteur = 0
    for i in lst:
        if i ==e :
            compteur += 1
    return compteur

#Question 3

def est_triee1(lst:list)->bool:
    """Test si la liste lst est triée par ordre croissant en utilisant une boucle for
    Args:
        lst (list): liste à tester
    Returns:
        bool: renvoie true si la liste est triée, false si elle ne l'est pas
    """
    for i in range (len(lst)-1):
        if lst[i] >= lst[i+1]:
            return False
    return True

def est_triee2(lst: list) -> bool:
    """Test si la liste lst est triée par ordre croissant en utilisant une boucle while
    Args:
        lst (list): liste à tester
    Returns:
        bool: renvoie true si la liste est triée, false si elle ne l'est pas
    """
    i = 0
    while (i < len(lst) - 1) and (lst[i] <= lst[i + 1]):
        i += 1
    return i == len(lst) - 1

#À mon avis la meilleure version est la première car elle est plus lisble.

#Question 4

def position_tri(lst: list, e:int) -> int:
    """Trouve la position de l'élément e dans la liste TRIÉE lst en utilisant la recherche dichotomique.
    Args:
        lst (list): Liste triée.
        e: L'élément à chercher.
    Returns:
        int: La position de l'élément (ou -1 si non trouvé).
    """
    debut = 0
    fin = len(lst) - 1
    while debut <= fin:  # Tant que la plage de recherche est valide
        milieu = (debut + fin) // 2  # Calcule l'indice du milieu
        if lst[milieu] == e:  # Si on a trouvé l'élément
            return milieu  # On retourne sa position
        elif lst[milieu] < e:  # Si l'élément est dans la moitié droite
            debut = milieu + 1  # On met à jour le début de la plage de recherche
        else:  # Sinon (l'élément est dans la moitié gauche)
            fin = milieu - 1  # On met à jour la fin de la plage de recherche
    return -1 

#Question 5

def a_repetitions(lst:list)->bool:
    """Renvoie true si la liste lst comporte des répétitions de valeurs 
    Args:
        lst (list): Liste d'entiers
    Returns:
        bool: True ou false
    """
    T = []
    i = 0  # Indice pour parcourir la liste
    while i < len(lst):
        if lst[i] not in T:  # Si l'élément n'est pas présent dans la liste T
            T.append(lst[i])  # On l'ajoute à la liste T
        else:  # Sinon, on a trouvé une répétition
            return True
        i += 1  # Passer à l'élément suivant
    return False 

#----------------------TEST----------------------#

LISTE = [1,2,3,4,5,6,7,8,9,10]

def test_exercice2():  
    print("Test position1 (réponse attendue : 3) : ", position1(LISTE,4))
    print("Test position2 (réponse attendue : -1) : ", position2(LISTE,0))
    print("Test nb_occurrences (réponse attendue : 1) : ", nb_occurrences(LISTE,5))
    print("Test est_triee (réponse attendue : True) : ", est_triee1(LISTE))
    print("Test est_triee (réponse attendue : False) : ", est_triee2(list(reversed(LISTE))))
    print("Test position_tri (réponse attendue : 3) : ", position_tri(LISTE, 4))
    print("Test a_repetitions (réponse attendue : True) : ", a_repetitions([1,1,2,3,4,5,6,7,8,9,10]))
   
test_exercice2()