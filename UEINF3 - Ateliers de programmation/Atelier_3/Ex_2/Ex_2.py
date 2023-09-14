# Question 1
def mots_Nlettres(lst_mot: list, n: int) -> list:
    """
    Renvoie une liste de mots de la liste `lst_mot` ayant `n` lettres.
    Args:
        lst_mot (list): Liste de mots.
        n (int): Nombre de lettres.
    Returns:
        list: Liste de mots ayant exactement `n` lettres.
    """
    listmot = []
    for i in lst_mot :
        if len(i)==n:
            listmot.append(i)
    return listmot

# Question 2
def commence_par(mot: str, prefixe: str) -> bool:
    """
    Vérifie si le mot `mot` commence par le préfixe `prefixe`.
    Args:
        mot (str): Mot à vérifier.
        prefixe (str): Préfixe à vérifier.
    Returns:
        bool: True si `mot` commence par `prefixe`, False sinon.
    """
    return mot.startswith(prefixe)

# Question 3
def finit_par(mot: str, suffixe: str) -> bool:
    """
    Vérifie si le mot `mot` se termine par le suffixe `suffixe`.
    Args:
        mot (str): Mot à vérifier.
        suffixe (str): Suffixe à vérifier.
    Returns:
        bool: True si `mot` se termine par `suffixe`, False sinon.
    """
    return mot.endswith(suffixe)

# Question 4
def finissent_par(lst_mot: list, suffixe: str) -> list:
    """
    Renvoie une liste des mots de `lst_mot` qui se terminent par `suffixe`.
    Args:
        lst_mot (list): Liste de mots.
        suffixe (str): Suffixe à vérifier.
    Returns:
        list: Liste des mots se terminant par `suffixe`.
    """
    liste = []
    for mot in lst_mot :
        if finit_par(mot, suffixe):
            liste.append(mot)
    return liste

# Question 5
def commencent_par(lst_mot: list, prefixe: str) -> list:
    """
    Renvoie une liste des mots de `lst_mot` qui commencent par `prefixe`.
    Args:
        lst_mot (list): Liste de mots.
        prefixe (str): Préfixe à vérifier.
    Returns:
        list: Liste des mots commençant par `prefixe`.
    """
    liste = []
    for mot in lst_mot :
        if commence_par(mot, prefixe):
            liste.append(mot)
    return liste

# Question 6
def liste_mots(lst_mot: list, prefixe: str, suffixe: str, n: int) -> list:
    """
    Renvoie une liste des mots de `lst_mot` qui ont `n` lettres, qui commencent
    par `prefixe` et qui se terminent par `suffixe`.
    Args:
        lst_mot (list): Liste de mots.
        prefixe (str): Préfixe à vérifier.
        suffixe (str): Suffixe à vérifier.
        n (int): Nombre de lettres.
    Returns:
        list: Liste des mots répondant aux critères.
    """
    liste_suffixe= finissent_par(mots_Nlettres(lst_mot,n),suffixe)
    return commencent_par(liste_suffixe,prefixe)

# Question 7
def dictionnaire(fichier: str) -> list:
    """
    Lit un fichier et retourne son contenu sous forme de liste de mots.
    Args:
        fichier (str): Chemin du fichier.
    Returns:
        list: Liste des mots contenus dans le fichier.
    """
    liste_dico = []
    f = open(fichier, 'r')
    c = f.readline()
    while c!="":
        c = f.readline()
        c = c.rstrip('\n')
        liste_dico.append(c)
    return liste_dico

#-------------------------Fonction de test-------------------------
def test_exercice2():
    lst_mot=["jouer","bonjour", "punir", "jour", "aurevoir", "revoir", "pouvoir", "cour", "abajour",
            "finir", "aimer"] 
    print("Test mots_Nlettres : ",mots_Nlettres(lst_mot,5)) 
    print("Test commence_par : ",commence_par("test","t"))
    print("Test finit_par : ",finit_par("test","t"))
    print("Test commencent_par : ",commencent_par(lst_mot,"j"))
    print("Test finissent_par : ",finissent_par(lst_mot,"r"))
    print("Test liste_mots et dictionnaire : ",
          liste_mots(dictionnaire('UEINF3 - Ateliers de programmation\Atelier_3\Ex_2\littre.txt'),
                     "j","r",5))

test_exercice2()
