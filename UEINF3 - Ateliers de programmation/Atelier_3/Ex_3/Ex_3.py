import random

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

def build_dict(lst: list) -> dict:
    dictionnaire_mots = {}
    for mot in lst:
        taille = len(mot)
        if taille in dictionnaire_mots:
            dictionnaire_mots[taille].append(mot)
        else:
            dictionnaire_mots[taille] = [mot]
    return dictionnaire_mots

def select_word(sorted_words: dict, word_len: int) -> str:
    mots_disponibles = sorted_words.get(word_len, [])
    if mots_disponibles:
        return random.choice(mots_disponibles)
    else:
        return ""
    
#Question 3
def runGame():
    """Code générale du jeu"""
    with open("UEINF3 - Ateliers de programmation\Atelier_3\Ex_3\listePays.txt", 'r') as fichier:
        pays = fichier.readlines()
    pays = [p.strip() for p in pays]
    dicoPays = build_dict(pays)
    niveau = str(input("Choisssisez le niveau de difficulté (easy, normal, hard) : "))
    match niveau :
        case "easy" :
            mot = select_word(dicoPays, random.randint(1,7))
        case "normal" :
            mot = select_word(dicoPays, random.randint(6,9))
        case "hard" :
            mot = select_word(dicoPays, random.randint(8,len(max(pays))))
        case _ :
            return None
    mot = (random.choice(pays)).lower()
    print("Devinez le mot : ", mot)
    print(outputStr(mot,[]))
    essais = 0
    erreur = ["|______","|/ \ ","| T ","| O ","|---]"]
    indices_mot = []
    while essais < 5 :
        lettre = str(input("\nDonnez une lettre : ")).lower()
        if lettre in mot :
            indices_lettre = places_lettre(lettre, mot)
            indices_mot += indices_lettre
            print(outputStr(mot,indices_mot))
        else :
            print("La lettre", lettre, "n'est pas dans le mot")
            for i in reversed(range(essais+1)):
                print(erreur[i])
            essais += 1
            print("Il vous reste ", 5-essais, " essais.")
    if essais == 5 :
        print("\nPerdu, le mot était :", mot)

runGame()
