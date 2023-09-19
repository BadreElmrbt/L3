from random import randint,shuffle,sample
import time
import matplotlib.pyplot as plt

#---------------Exercice 1---------------
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

#---------------Exercice 2---------------
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

#---------------Exercice 3---------------
def choose_element_list(list_in_which_to_choose: list) -> int:
    """
    Choisit un élément aléatoire dans une liste.
    :param list_in_which_to_choose: La liste dans laquelle choisir.
    :return: L'élément choisi.
    """
    nbr_alea = randint(0, len(list_in_which_to_choose)-1)
    return list_in_which_to_choose[nbr_alea]

#---------------Exercice 4---------------
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

#---------------Exercice 5---------------
#Question 1
def perf_list(mix_list, shuffle, listInt, n):
    time_shuffle = []
    time_mix = []
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
        time_shuffle.append(sum(times_shuffle) / n)
        time_mix.append(sum(times_mix) / n)
    return (time_mix, time_shuffle)

#Question 2
def perf_extract(sample, extract_elements_list, listInt, n, int_nbr_of_element_to_extract):
    time_extract = []
    time_sample = []
    for i in listInt:
        times_extract = []
        times_sample = []
        liste = gen_list_random_int(i)
        for _ in range(n):
            start_pc = time.perf_counter()
            extract_elements_list(liste,int_nbr_of_element_to_extract)
            end_pc = time.perf_counter()
            times_extract.append(end_pc - start_pc)
            start_pc = time.perf_counter() 
            sample(liste,int_nbr_of_element_to_extract)
            end_pc = time.perf_counter()
            times_sample.append(end_pc - start_pc)
        time_extract.append(sum(times_extract) / n)
        time_sample.append(sum(times_sample) / n)
    return (time_extract, time_sample)


#Question 1
def sort_list(liste1):
    liste = list(liste1)
    for i in range(len(liste)):
        min_index = i
        for j in range(i+1, len(liste)):
            if liste[j] < liste[min_index]:
                min_index = j
        liste[i], liste[min_index] = liste[min_index], liste[i]
    return liste

#Question 2
def perf_list2(sorted, sort_list, listInt, n):
    time_sort_list = []
    time_mix = []
    for i in listInt:
        times_sort_list = []
        times_mix = []
        for _ in range(n):
            liste = gen_list_random_int(i)
            start_pc = time.perf_counter()
            sort_list(liste)
            end_pc = time.perf_counter()
            times_sort_list.append(end_pc - start_pc)
            start_pc = time.perf_counter() 
            sorted(liste)
            end_pc = time.perf_counter()
            times_mix.append(end_pc - start_pc)
        time_sort_list.append(sum(times_sort_list) / n)
        time_mix.append(sum(times_mix) / n)
    return (time_sort_list, time_mix)

#---------------Exercice 7---------------
#Question 1
def stupid_sort(lst_to_sort):
    i = 1
    while lst_to_sort != sort_list(lst_to_sort):
        print("TOUJOURS PAS : essai numéro : ",i)
        lst_to_sort = mix_list(lst_to_sort)
        i += 1
    return lst_to_sort

#print(stupid_sort([9,5,7,8,3,1,-5,2,23,"abc"]))

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
    print("Exercice 4 -", num_to_extract, "éléments extraits : ", extracted_list)

    #Exercice 5
    result = perf_list(mix_list, shuffle, [5,10,20], 10)
    x_axis_list = [5,10,20]
    fig, ax = plt.subplots()
    ax.plot(x_axis_list,result[0], 'bo-', label='Mix_list (ma fonction)') 
    ax.plot(x_axis_list,result[1],'r*-',label='Shuffle (fonction python)') 
    ax.set(xlabel='Taille de la liste', ylabel='Temps (s)', title="Comparaison temps fonction") 
    ax.legend(loc='upper center', shadow=True, fontsize='x-large') 

    listNbr = [10, 500, 5000, 50000, 100000]
    resultDeux = perf_extract(sample, extract_elements_list,listNbr, 100, 5)
    x_axis_list = listNbr
    fig, ax = plt.subplots()
    ax.plot(x_axis_list,resultDeux[0],'bo-',label='Extract (ma fonction)') 
    ax.plot(x_axis_list,resultDeux[1], 'r*-', label='Sample (fonction python)')
    ax.set(xlabel='Taille de la liste', ylabel='Temps (s)', title="Comparaison temps fonction") 
    ax.legend(loc='upper center', shadow=True, fontsize='x-large') 

    # Exercice 6
    sorted_list = sort_list(list1)
    print("Exercice 6 - liste triée : ", sorted_list)

    result = perf_list2(sorted, sort_list, [5,10,20], 10)
    x_axis_list = [5,10,20]
    fig, ax = plt.subplots()
    ax.plot(x_axis_list,result[0],'bo-',label='Sort_list (ma fonction)') 
    ax.plot(x_axis_list,result[1], 'r*-', label='Sorted (fonction python)') 
    ax.set(xlabel='Taille de la liste', ylabel='Temps (s)', title="Comparaison temps fonction") 
    ax.legend(loc='upper center', shadow=True, fontsize='x-large') 
    plt.show()
