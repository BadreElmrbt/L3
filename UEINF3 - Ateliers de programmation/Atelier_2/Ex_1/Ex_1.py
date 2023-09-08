#Question 1

def somme1(L:list)->float:
    """Calcule la somme d'une liste
    Args:
        L (list): liste
    Returns:
        float: somme de la liste
    """
    somme = 0
    for i in range (len(L)):
        somme += L[i]
    return somme

def somme2(L:list):
    """Calcule la somme d'une liste
    Args:
        L (list): liste
    Returns:
        float: somme de la liste
    """
    somme = 0
    for i in L :
        somme += i
    return somme

def somme3(L:list)->float:
    """Calcule la somme d'une liste
    Args:
        L (list): liste
    Returns:
        float: somme de la liste
    """
    somme = 0
    i = 0
    while i < len(L):
        somme += L[i]
        i += 1
    return somme

#La seconde fonction semble plus accessible et compréhensible que les autres

#Question 3 :

def moyenne(L:list)->float:
    """Calcule la moyenne d'une liste
    Args:
        L (list): liste d'entiers
    Returns:
        float: moyenne
    """
    moyenne = 0
    if len(L)==0:
        None
    else:
        moyenne = somme1(L)/len(L)
    return moyenne

#Question 4 :

def nb_sup1(L:list,e:int)->int:
    """Retourne le nombre de valeurs supérieurs à e dans L
    Args:
        L (list): liste d'entiers
        e (int): entiers
    Returns:
        int: nombres de valeurs
    """
    nbrValeursSup = 0
    for i in range(len(L)):
        if e<L[i]:
            nbrValeursSup += 1
    return nbrValeursSup

def nb_sup2(L:list,e:int)->int:
    """Retourne le nombre de valeurs supérieurs à e dans L
    Args:
        L (list): liste d'entiers
        e (int): entiers
    Returns:
        int: nombres de valeurs
    """
    nbrValeursSup = 0
    for i in L:
        if e<i:
            nbrValeursSup += 1
    return nbrValeursSup

#Question 5 :

def moy_sup(L:list,e:int)->float:
    """Calcule la moyenne des valeurs supérieurs à e dans L

    Args:
        L (list): liste
        e (int): entier

    Returns:
        float: moyenne finale
    """
    somme = 0
    moyenne = 0
    nbrValeursSup = nb_sup2(L,e)
    if nbrValeursSup>0 :
        for i in range(len(L)):
            if e<L[i]:
                somme += L[i]
        moyenne = somme/nbrValeursSup
    else :
        None
    return moyenne

#Question 6

def val_max(L:list)->int:
    """Retourne le max d'une liste

    Args:
        L (list): liste d'entiers

    Returns:
        int: le maximum
    """
    maximum = L[0]
    for i in range (len(L)):
        if L[i]>maximum:
            maximum = L[i]
    return maximum

#Question 7

def ind_max(L:list)->int:
    """Retourne l'indice de l'élément maximal de la liste L

    Args:
        L (list): liste

    Returns:
        int: indice de l'élément le plus grand de L
    """
    maximum = val_max(L)
    indice = None
    for i in range(len(L)):
        if L[i]==maximum:
            indice = i
    return indice

#Fonction de test

def test_exercice1 (): 
    print("TEST SOMME") 
    print("Test liste vide : ", somme1([])) 
    #test somme 11111 
    lst2test1=[1,10,100, 1000,10000] 
    print("Test somme 1111 : ", somme2(lst2test1))
    listeMoyenne= [1,2,3,4,5]
    print("Test moyenne  : ", moyenne(listeMoyenne))
    listeNbSup=[0,0,5,4]
    print("Test nb_sup : ", nb_sup2(listeNbSup,1))
    listeMoySup=[10,100,1000]
    print("Test moy_sup : ", moy_sup(listeMoySup,0))
    listeMax = [5,589,-96]
    print("Test test_max: ", val_max(listeMax))
    listeIndiceMax = [1,10,-5,4]
    print("Test test_ind_max: ", ind_max(listeIndiceMax))

test_exercice1()
