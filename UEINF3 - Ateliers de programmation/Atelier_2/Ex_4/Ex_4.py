#------------------------------Question 1------------------------------

def histo(F:list)->list:
    """comptage de fréquence
    Args:
        F (list): liste d'entiers
    Returns:
        list: _fréquence des entiers de la liste F
    """
    H = [0] * (max(F) + 1)
    for val in F:
        H[val] += 1
    return H

F = [6,5,6,8,4,2,1,5]
print(histo(F))

def est_injective(F:list)->bool:
    """Teste si une fonction est injective ou pas

    Args:
        F (list): liste à tester
    Returns:
        bool: True ou false si F est injective
    """
    H = histo(F)
    for i in H :
        if i > 1 :
            return False
    return True

print(est_injective(F))

def est_surjective(F:list)->bool:
    """Teste si une fonction est surjective ou pas
    Args:
        F (list): liste à tester
    Returns:
        bool: True ou false si F est surjective
    """
    H = histo(F)
    for i in H :
        if i < 1 :
            return False
    return True

print(est_surjective(F))

def est_bijective(F:list)->bool:
    """Teste si une fonction est bijective ou pas
    Args:
        F (list): liste à tester
    Returns:
        bool: True ou false si F est bijective
    """
    return est_injective(F) and est_surjective(F)

print(est_bijective(F))

#------------------------------Question 2------------------------------

def afficheHisto1(F:list)->str:
    """Affiche une réprésentaiton graphique de l'histogramme associé à la liste d'entiers F
    Args:
        F (list): liste d'entiers
    Returns:
        str: réprésentation graphique en str
    """
    #---OBTENU GRÂCE À ChatGPT--
    H = histo(F)
    MAXOCC = max(H)
    
    for i in range(MAXOCC, 0, -1):
        for j in range(len(H)):
            if H[j] >= i:
                print('#', end=' ')
            else:
                print(' ', end=' ')
        print() #permet de passer à une autre ligne
   
    var = ""
    nbr = ""
    for i in range (len(H)):
        var += "|- "
        nbr += str(i) + "  "
    print(var)
    print(nbr)

F = [1,5,5,5,9,11,11,15,15,15]
afficheHisto1(F)

#------------------------------Question 3------------------------------

import matplotlib.pyplot as plt

def afficheHisto2(F:list):
    """Affiche une réprésentaiton graphique de l'histogramme associé à la liste d'entiers F
    Args:
        F (list): liste d'entiers
    Returns:
        plt: réprésentation graphique
    """
    plt.hist(F)
    plt.title("Histogramme avec MatPlotLib")
    plt.show()

afficheHisto2(F)
