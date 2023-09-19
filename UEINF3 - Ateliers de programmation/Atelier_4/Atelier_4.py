from random import *
import time
import matplotlib.pyplot as plt
import numpy as np

# Exercice 1
def gen_list_random_int(len_max: int = 10, int_binf: int = 0, int_bsup: int = 10) -> list:
    """
    Génère une liste de nombres entiers aléatoires.
    :param len_max: La longueur maximale de la liste (par défaut 10).
    :param int_binf: La borne inférieure pour les entiers (par défaut 0).
    :param int_bsup: La borne supérieure pour les entiers (par défaut 10).
    :return: Une liste de nombres entiers aléatoires.
    """
    int_nbr = []
    count = 0
    while count < len_max:
        int_nbr.append(randint(int_binf, int_bsup-1))
        count += 1
    return int_nbr

# Exercice 2
def mix_list(list_to_mix: list) -> list:
    """
    Mélange une liste.
    :param list_to_mix: La liste à mélanger.
    :return: Une nouvelle liste mélangée.
    """
    nbr_alea_list = []
    mixed_list = []
    for i in range(len(list_to_mix)):
        nbr_alea = randint(0, len(list_to_mix)-1)
        if nbr_alea not in nbr_alea_list:
            mixed_list.append(list_to_mix[nbr_alea])
            nbr_alea_list.append(nbr_alea)
        else:
            while nbr_alea in nbr_alea_list:
                nbr_alea = randint(0, len(list_to_mix)-1)
            mixed_list.append(list_to_mix[nbr_alea])
            nbr_alea_list.append(nbr_alea)
    return mixed_list

# Exercice 3
def choose_element_list(list_in_which_to_choose: list) -> int:
    """
    Choisit un élément aléatoire dans une liste.
    :param list_in_which_to_choose: La liste dans laquelle choisir.
    :return: L'élément choisi.
    """
    nbr_alea = randint(0, len(list_in_which_to_choose)-1)
    return list_in_which_to_choose[nbr_alea]

# Exercice 4
def extract_elements_list(list_in_which_to_choose: list, int_nbr_of_element_to_extract: int) -> list:
    """
    Extrait un nombre donné d'éléments aléatoires d'une liste.
    :param list_in_which_to_choose: La liste à partir de laquelle extraire.
    :param int_nbr_of_element_to_extract: Le nombre d'éléments à extraire.
    :return: Une liste d'éléments extraits.
    """
    nbr_alea_list = []
    extracted_list = []
    for i in range(int_nbr_of_element_to_extract):
        nbr_alea = randint(0, len(list_in_which_to_choose)-1)
        if nbr_alea not in nbr_alea_list:
            extracted_list.append(list_in_which_to_choose[nbr_alea])
            nbr_alea_list.append(nbr_alea)
        else:
            while nbr_alea in nbr_alea_list:
                nbr_alea = randint(0, len(list_in_which_to_choose)-1)
            extracted_list.append(list_in_which_to_choose[nbr_alea])
            nbr_alea_list.append(nbr_alea)
    return extracted_list

#----------------Fonction de test----------------
def test_functions():
    #Exercice 1
    list1 = gen_list_random_int()
    print("Exercice 1 - Liste générée aléatoirement : ", list1)

    # Exercice 2
    list2 = mix_list(list1)
    print("Exercice 2 - Liste mélangée : ", list2)

    # Exercice 3
    element = choose_element_list(list1)
    print("Exercice 3 - Élément choisi : ", element)

    # Exercice 4
    num_to_extract = 3 
    extracted_list = extract_elements_list(list1, num_to_extract)
    print("Exercice 4 - ", num_to_extract, "éléments extraits : ", extracted_list)

#test_functions()

#Exercice 5
#Question 1

def perf_mix(shuffle, mix_list, listInt, n):
    tab2 = []
    tab3 = []
    for i in listInt:
        times_shuffle = []
        times_mix = []
        for _ in range(n):
            liste = gen_list_random_int(i)
            start_pc = time.perf_counter()
            shuffle(liste)
            end_pc = time.perf_counter()
            times_shuffle.append(end_pc - start_pc)
            
            start_pc = time.perf_counter() 
            mix_list(liste)
            end_pc = time.perf_counter()
            times_mix.append(end_pc - start_pc)
            
        tab2.append(sum(times_shuffle) / n)
        tab3.append(sum(times_mix) / n)

    return (tab2, tab3)

listInt = [5, 10, 15]
result = perf_mix(shuffle, mix_list, listInt, 20)

fig, ax = plt.subplots()
ax.plot(listInt, result[0], 'bo-', label='shuffle')
ax.plot(listInt, result[1], 'r*-', label='mix_list')
ax.set(xlabel='Taille de la liste', ylabel='Temps (s)',
       title='Performance de shuffle et mix_list (10 tests)')
ax.legend(loc='upper center', shadow=True, fontsize='x-large')
plt.show()

#Question 2
