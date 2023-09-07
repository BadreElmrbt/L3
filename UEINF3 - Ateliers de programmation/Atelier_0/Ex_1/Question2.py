import random

choixJeu = input("Voulez-vous jouer contre l'ordinateur (Max 5 parties) O/N ? ")
if choixJeu !=('0' or 'N'):
    print("Je n'ai pas compris votre réponse")
    statutJeu = False
if choixJeu == 'O':
    nomJoueur1 = input("Quel est votre nom ?")
    print("Bienvenue ", nomJoueur1, " nous allons jouer ensemble")
    nomJoueur2 = "Machine"
    statutJeu = True
elif choixJeu == 'N':
    nomJoueur1 = input("Quel est votre nom ? ")
    print("Bienvenue ",nomJoueur1, " nous allons jouer ensemble")
    nomJoueur2 = input("Quel est le nom du deuxième joueur ?")
    print("Bienvenu ",nomJoueur2, " nous allons jouer ensemble \n")
    statutJeu = True

scoreJoueur1 = 0
scoreJoueur2 = 0
nbrPartie = 0


while statutJeu == True :
    nbrPartie += 1 
    choixJoueur1 = input("{nom} Faites votre choix parmi (pierre, papier, ciseaux): ".format(nom=nomJoueur1))
    
    while choixJoueur1 not in ('pierre', 'papier', 'ciseaux'):
        print("Je n'ai pas compris votre réponse")
        choixJoueur1 = input("{} Faites votre choix parmi (pierre, papier, ciseaux): ".format(nomJoueur1))

    if choixJeu == 'O': 
        choixJoueur2 = ['papier','pierre','ciseaux'][random.randint(0, 2)]
    else :
        choixJoueur2 = input("{nom} Faites votre choix parmi (pierre, papier, ciseaux): ".format(nom=nomJoueur2))
        while choixJoueur2 not in ('pierre', 'papier', 'ciseaux'):
            print("Je n'ai pas compris votre réponse")
            choixJoueur2 = input("{} Faites votre choix parmi (pierre, papier, ciseaux): ".format(nomJoueur2))

    #On affiche les choix de chacun
    print("Si on récapitule : ",nomJoueur1, " a joué ", choixJoueur1, " et ", nomJoueur2, " a joué " ,choixJoueur2,"\n")


    #On regarde qui a gagné cette manche on calcule les points et on affiche le résultat
    if choixJoueur1 == 'papier' and choixJoueur2 == 'papier' :
        gagnant = "aucun de vous, vous êtes ex æquo"
        scoreJoueur1 = scoreJoueur1 + 0
        scoreJoueur2 = scoreJoueur2 + 0
        print("le gagnant est",gagnant)
        print("Les scores à l'issue de cette manche sont donc",nomJoueur1, scoreJoueur1, "et", nomJoueur2, scoreJoueur2, "\n")

    if choixJoueur1 == 'pierre' and choixJoueur2 == 'papier' :
        gagnant = nomJoueur2
        scoreJoueur1 = scoreJoueur1 + 0
        scoreJoueur2 = scoreJoueur2 + 1
        print("le gagnant est",gagnant)
        print("Les scores à l'issue de cette manche sont donc",nomJoueur1, scoreJoueur1, "et", nomJoueur2, scoreJoueur2, "\n")

    if choixJoueur1 == 'pierre' and choixJoueur2 == 'pierre' :
        gagnant = "aucun de vous, vous êtes ex æquo"
        scoreJoueur1 = scoreJoueur1 + 0
        scoreJoueur2 = scoreJoueur2 + 0
        print("le gagnant est",gagnant)
        print("Les scores à l'issue de cette manche sont donc",nomJoueur1, scoreJoueur1, "et", nomJoueur2, scoreJoueur2, "\n")

    if choixJoueur1 == 'pierre' and choixJoueur2 == 'ciseaux' :
        gagnant = nomJoueur1
        scoreJoueur1 = scoreJoueur1 + 1
        scoreJoueur2 = scoreJoueur2 + 0
        print("le gagnant est",gagnant)
        print("Les scores à l'issue de cette manche sont donc",nomJoueur1, scoreJoueur1, "et", nomJoueur2, scoreJoueur2, "\n")

    if choixJoueur1 == 'papier' and choixJoueur2 == 'ciseaux' :
        gagnant = nomJoueur2
        scoreJoueur1 = scoreJoueur1 + 0
        scoreJoueur2 = scoreJoueur2 + 1
        print("le gagnant est",gagnant)
        print("Les scores à l'issue de cette manche sont donc",nomJoueur1, scoreJoueur1, "et", nomJoueur2, scoreJoueur2, "\n")

    if choixJoueur1 == 'papier' and choixJoueur2 == 'pierre' :
        gagnant = nomJoueur1
        scoreJoueur1 = scoreJoueur1 + 1
        scoreJoueur2 = scoreJoueur2 + 0
        print("le gagnant est",gagnant)
        print("Les scores à l'issue de cette manche sont donc",nomJoueur1, scoreJoueur1, "et", nomJoueur2, scoreJoueur2, "\n")

    if choixJoueur1 == 'ciseaux' and choixJoueur2 == 'pierre' :
        gagnant = nomJoueur2
        scoreJoueur1 = scoreJoueur1 + 0
        scoreJoueur2 = scoreJoueur2 + 1
        print("le gagnant est",gagnant)
        print("Les scores à l'issue de cette manche sont donc",nomJoueur1, scoreJoueur1, "et", nomJoueur2, scoreJoueur2, "\n")

    if choixJoueur1 == 'ciseaux' and choixJoueur2 == 'ciseaux' :
        gagnant = "aucun de vous, vous être ex æquo"
        scoreJoueur1 = scoreJoueur1 + 0
        scoreJoueur2 = scoreJoueur2 + 0
        print("le gagnant est",gagnant)
        print("Les scores à l'issue de cette manche sont donc",nomJoueur1, scoreJoueur1, "et", nomJoueur2, scoreJoueur2, "\n")

    if choixJoueur1 == 'ciseaux' and choixJoueur2 == 'papier' :
        gagnant = nomJoueur1
        scoreJoueur1 = scoreJoueur1 + 1
        scoreJoueur2 = scoreJoueur2 + 0
        print("le gagnant est",gagnant)
        print("Les scores à l'issue de cette manche sont donc",nomJoueur1, scoreJoueur1, "et", nomJoueur2, scoreJoueur2, "\n")

    if nbrPartie ==1 or nbrPartie ==2 or nbrPartie==3 or nbrPartie==4:
        statutJeu = True
    if nbrPartie ==5:
        statutJeu = False
        
    if nbrPartie ==1 or nbrPartie ==2 or nbrPartie==3 or nbrPartie==4:
        #On propose de statutJeu ou de s'arrêter 
        go = input("Souhaitez vous refaire une partie {} contre {} ? (O/N) ".format(nomJoueur1,nomJoueur2))
        if go == 'O':
            statutJeu = True
        if go == 'N':
            statutJeu = False
        if go != 'O' and go != 'N':
            statutJeu = True
            print("Vous ne répondez pas à la question, on continue ")
  
        
if statutJeu == False :
    print("Merci d'avoir joué ! A bientôt")