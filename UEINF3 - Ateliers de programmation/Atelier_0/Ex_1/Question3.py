import random

def obtenirChoixJoueur(nomJoueur:str) -> str:
    choix = input(nomJoueur + " Faites votre choix parmi (pierre, papier, ciseaux, puit): ").strip().lower()

    while choix not in ('pierre', 'papier', 'ciseaux', 'puit'):
        print("Je n'ai pas compris votre réponse")
        choix = input(nomJoueur + " Faites votre choix parmi (pierre, papier, ciseaux, puit): ").strip().lower()

    return choix

nbrPartie = 0
scoreJoueur1 = 0
scoreJoueur2 = 0

nomJoueur1 = input("Quel est votre nom ? ")
print("Bienvenue " + nomJoueur1 + ", nous allons jouer ensemble")
choixJeu = input("Voulez-vous jouer contre l'ordinateur (Max 5 parties) O/N ? ").strip().lower()
if choixJeu == 'o':
    nomJoueur2 = "Machine"
else:
    nomJoueur2 = input("Quel est le nom du deuxième joueur ? ")
print("Bienvenue " + nomJoueur2 + ", nous allons jouer ensemble\n")

statutJeu = True

while statutJeu:
    nbrPartie += 1
    choixJoueur1 = obtenirChoixJoueur(nomJoueur1)

    if nomJoueur2 == "Machine":
        choixJoueur2 = random.choice(['pierre', 'papier', 'ciseaux', 'puit'])
    else:
        choixJoueur2 = obtenirChoixJoueur(nomJoueur2)

    print("Si on récapitule : " + nomJoueur1 + " a joué " + choixJoueur1 + " et " + nomJoueur2 + " a joué " + choixJoueur2 + "\n")

    if choixJoueur1 == choixJoueur2:
        gagnant = "Personne"
    elif (choixJoueur1 == 'pierre' and choixJoueur2 == 'ciseaux') or (choixJoueur1 == 'papier' and choixJoueur2 == 'pierre') or (choixJoueur1 == 'ciseaux' and choixJoueur2 == 'papier'):
        gagnant = nomJoueur1
        scoreJoueur1 += 1
    elif (choixJoueur1 == 'puit' and choixJoueur2 == 'feuille'):
        gagnant = nomJoueur2
        scoreJoueur2 += 1
    else:
        gagnant = nomJoueur2
        scoreJoueur2 += 1

    print("Le gagnant est " + gagnant)
    print("Les scores à l'issue de cette manche sont donc " + nomJoueur1 + " : " + str(scoreJoueur1) + " et " + nomJoueur2 + " : " + str(scoreJoueur2) + "\n")

    if nbrPartie < 5:
        go = input("Souhaitez-vous refaire une partie " + nomJoueur1 + " contre " + nomJoueur2 + " ? (O/N) ").strip().lower()
        if go != 'o':
            statutJeu = False

print("Merci d'avoir joué ! A bientôt")
