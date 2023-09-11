def separer(L):
    """Classe les nombres de la liste L dans une nouvelle liste LSEP en plaçant
    ensemble les nombres négatifs, les nombres nuls et les nombres positifs.
    Les nombres négatifs sont placés à gauche, les zéros au centre et les
    nombres positifs à droite.
    Args:
        L (list): Liste d'entiers.   
    Returns:
        list: Liste LSEP construite selon les critères décrits ci-dessus.
    """
    LSEP = [0] * len(L)  # Initialise la liste LSEP (de même dimension que L) avec des zéros
    indice_neg = 0 # Indice pour les nombres négatifs (on part de la première case)
    indice_pos = len(L) - 1 # Indice pour les nombres positifs (on part de la dernière case)

    for nombre in L:
        if nombre < 0:  # Si le nombre est négatif on le place à gauche
            LSEP[indice_neg] = nombre
            indice_neg += 1
        elif nombre != 0:  # Si le nombre est différent de zéro et positif on le place à droite
            LSEP[indice_pos] = nombre
            indice_pos -= 1
        #Les zéros sont placés au milieu par défaut 
        #Car nous avons initialisé la liste LSEP qu'avec des 0 à l'intérieur
    return LSEP

L = [-2, 4, 0, -7, 0, 5, -1, 0, 9]
LSEP = separer(L)
print(LSEP)
