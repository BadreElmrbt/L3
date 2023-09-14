#Question 1
def places_lettre(ch: str, mot: str) -> list:
    """
    Recherche si le caractère `ch` est présent dans la chaîne `mot`.
    Renvoie une liste vide si le caractère n'est pas présent, sinon les indices désignant sa place dans le mot.
    Args:
        ch (str): Caractère à rechercher.
        mot (str): Chaîne de caractères à inspecter.
    Returns:
        list: Liste des indices où le caractère `ch` apparaît dans `mot`.
    """
    indices = []
    for i in range(len(mot)):
        if mot[i] == ch:
            indices.append(i)
    return indices

def test_places_lettre():
    lettre = input("Entrez une lettre : ")
    mot = input("Entrez un mot : ")

    indices = places_lettre(lettre, mot)

    if indices:
        return indices
    else:
        return []

#Question 2
def outputStr(mot: str, lpos: list) -> str:
    """
    Remplace les caractères à certaines positions de la chaîne `mot` par des caractères spécifiques.
    Args:
        mot (str): La chaîne de caractères initiale.
        lpos (list): Une liste d'indices spécifiant les positions des caractères à remplacer.  
    Returns:
        str: Une nouvelle chaîne où les caractères aux positions spécifiées par `lpos` ont été remplacés par '_'.
    """
    strtab = []
    for i in range(len(mot)):
        strtab.append("_")
        if i in lpos:
            strtab[i] = mot[i]
    string = ""
    for i in range(len(strtab)):
        string += strtab[i] + " "
    return string

print(outputStr("bonjour", [0,1,2,3,4,5,6]))

#Question 3
