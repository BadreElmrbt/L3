#Question 1
def full_name(str_arg:str)->str:
    """Renvoie une chaîne avec le nom en majuscule et le prénom avec la 1ère lettre en maj
    Args:
        str_arg (str): chaîne de caractère séparé d'un espace
    Returns:
        str: nouvelle chaîne
    """
    nom,prenom = str_arg.split()
    nom = nom.upper()
    #Upper n'agit pas sur le objet, il renvoit juste un résultat sans rien modifier
    prenom = prenom[0].upper() + prenom[1:]
    return nom,prenom

#Question 2
def is_mail(str_arg:str)->(int,int):
    """Vérifie une adresse mail selon des conditions
    Args:
        str_arg (str): adresse mail
    Returns:
        (int,int) : validité, code d'erreur
    """
    a = 0
    b = 0
    if "@" in str_arg :
        corps,domaine = str_arg.split("@")
        if (corps == "" or corps[-1] == ".") or ".." in corps or corps[0] == ".":
            b = 1
        elif (domaine =="" or domaine[-1] == ".") or ".." in domaine or domaine[0] == "." :
            b = 3
        elif "." not in domaine:
            b = 4
        else :
            a = 1
    else :
        b = 2
    return (a,b)

#-------------------------Fonction de test-------------------------
def test_exercice1():
    print(full_name('bisgamgiglia paul'))
    print(is_mail("bisgambiglia_paul@univ-corse.fr"))
    print(is_mail("bisgambiglia_paulOuniv-corse.fr"))
    print(is_mail("bisgambiglia_paul@univ-corsePOINTfr"))
    print(is_mail("@univ-corse.fr"))

test_exercice1()

