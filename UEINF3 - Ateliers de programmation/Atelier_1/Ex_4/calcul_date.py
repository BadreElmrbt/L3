from datetime import date

def est_bissextile(annee:int)->bool:
    """Renvoie true si l'annee est bissextile

    Paramètres : 
    annne (int) : annee

    Renvoie :
    bool : true si l'année est bissextile
    """
    return ((annee % 4 == 0) and (annee % 100 != 0)) or (annee % 400 == 0)

#Question 1
# Liste des mois avec 30 jours
MOIS_30_JOURS = [4, 6, 9, 11]
# Liste des mois avec 31 jours
MOIS_31_JOURS = [1, 3, 5, 7, 8, 10, 12]
# Liste du mois de février
FEVRIER = [2]

def date_est_valide(annee:int, mois:int, jour:int)->bool:
    """Renvoie un booléen qui indique si la date est valide
    Args:
        jour (int): jour
        mois (int): mois
        annee (int): annee
    Returns:
        bool: renvoie true si la date est valide
    """
    MOIS_30_JOURS = [4, 6, 9, 11]
    MOIS_31_JOURS = [1, 3, 5, 7, 8, 10, 12]
    FEVRIER = [2]

    if annee <= 0 or mois < 1 or mois > 12:
        print("Condition 1 échouée")
        return False

    if mois in MOIS_30_JOURS and (jour < 1 or jour > 30):
        print("Condition 2 échouée")
        return False

    if mois in MOIS_31_JOURS and (jour < 1 or jour > 31):
        print("Condition 3 échouée")
        return False

    if mois in FEVRIER:
        if est_bissextile(annee):
            if jour < 1 or jour > 29:
                print("Condition 4 échouée")
                return False
        elif jour < 1 or jour > 28:
            print("Condition 5 échouée")
            return False

    return True

#Question 2
def saisie_date_naissance()->date:
    """Assure la saisie au clavier d'une date de naissance et renvoie une valeur de type date.

    Returns:
        date or None: Un objet de type date si la date est valide et dans le passé, sinon None.
    """
    annee = int(input("Entrez l'année de naissance : "))
    mois = int(input("Entrez le mois de naissance : "))
    jour = int(input("Entrez le jour de naissance : "))

    if date_est_valide(annee, mois, jour) and date(annee, mois, jour) <= date.today():
        return date(annee, mois, jour)
    else:
        print("Erreur : La date de naissance n'est pas valide")
        return None

#Question 3
def age(date_naissance : date) -> int:
    """Calcule l'âge en années à partir de la date de naissance.
    Args:
        date_naissance : date
    Returns:
        int : L'âge de la personne en années.
    """
    difference = date.today() - date_naissance
    return int(difference.days // 365.25)

#Question 4
def est_majeur(date_naissance:date)->bool:
    return age(date_naissance) > 18

#Question 5
def test_acces():
    """
    Assure la saisie de la date de naissance et affiche un message en fonction de l'âge.

    Returns:
        None
    """
    date_naissance = saisie_date_naissance()
    if date_naissance is not None:
        age_personne = age(date_naissance)

        if est_majeur(date_naissance):
            print(f"Bonjour, vous avez {age_personne} ans. Accès autorisé.")
        else:
            print(f"Désolé, vous avez {age_personne} ans. Accès interdit.")

#Question 6
test_acces()