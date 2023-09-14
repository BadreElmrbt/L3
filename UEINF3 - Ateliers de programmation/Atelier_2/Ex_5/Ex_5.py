def agencement_objets(nbEmplacement:int, lObjets:list):
    if nbEmplacement * 2 >= len(lObjets) :
        lObjets.sort()

        uniques = []
        doublons = []

        vitrine1 = []
        vitrine2 = []

        # Repérer les objets uniques et les doublons
        for objet in lObjets:
            if lObjets.count(objet) == 1:
                uniques.append(objet)
            elif lObjets.count(objet) == 2:
                doublons.append(objet)
            else :
                return None

        # Répartir les doublons entre les deux vitrines
        doublon_count = 0
        for doublon in doublons:
            if doublon_count % 2 == 0:
                vitrine1.append(doublon)
            else:
                vitrine2.append(doublon)
            doublon_count += 1

        # Remplir les vitrines avec les objets restants
        for objet in uniques:
            if len(vitrine1) < nbEmplacement:
                vitrine1.append(objet)
            else:
                vitrine2.append(objet)

        vitrine1.sort()
        vitrine2.sort()

        return (vitrine1, vitrine2)
    else:
        return None

nbEmplacement = 5
lObjets = [1, 2, 2, 3, 4, 5, 5, 6, 6]

print(agencement_objets(nbEmplacement, lObjets))