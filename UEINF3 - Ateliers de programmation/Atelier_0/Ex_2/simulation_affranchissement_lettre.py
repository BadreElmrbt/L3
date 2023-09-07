def affranchissement(typeLettre: str, poids: float, stickerSuivi: str) -> float:
    """ Calcule le tarif d'affranchissement d'une lettre en fonction du type, du poids, et de la présence d'un sticker de suivi. """
    
    TARIF_LETTRE_VERTE = {20 : 1.16, 100 : 2.32, 250 : 4.00, 500 : 6.00, 1000 : 7.5, 3000 : 10.5}
    TARIF_LETTRE_PRIORITAIRE = {20 : 1.43, 100 : 2.86, 250 : 5.26, 500 : 7.89, 3000 : 10.5}
    TARIF_LETTRE_ECOPLI = {20 : 1.14, 100 : 2.28, 250 : 3.92}

    tarif = 0

    if typeLettre == "verte":
        if poids < 20:
            tarif = TARIF_LETTRE_VERTE[20]
        elif 20 < poids <= 100:
            tarif = TARIF_LETTRE_VERTE[100]
        elif 100 < poids <= 250:
            tarif = TARIF_LETTRE_VERTE[250]
        elif 250 < poids <= 500:
            tarif = TARIF_LETTRE_VERTE[500]
        elif 500 < poids <= 1000:
            tarif = TARIF_LETTRE_VERTE[1000]
        elif 1000 < poids <= 3000:
            tarif = TARIF_LETTRE_VERTE[3000]

    elif typeLettre == "prioritaire":
        if poids < 20:
            tarif = TARIF_LETTRE_PRIORITAIRE[20]
        elif 20 < poids <= 100:
            tarif = TARIF_LETTRE_PRIORITAIRE[100]
        elif 100 < poids <= 250:
            tarif = TARIF_LETTRE_PRIORITAIRE[250]
        elif 250 < poids <= 500:
            tarif = TARIF_LETTRE_PRIORITAIRE[500]
        elif 500 < poids <= 1000:
            tarif = TARIF_LETTRE_PRIORITAIRE[1000]
        elif 1000 < poids <= 3000:
            tarif = TARIF_LETTRE_PRIORITAIRE[3000]

    elif typeLettre == "éco-pli":
        if poids < 20:
            tarif = TARIF_LETTRE_ECOPLI[20]
        elif 20 < poids <= 100:
            tarif = TARIF_LETTRE_ECOPLI[100]
        elif 100 < poids <= 250:
            tarif = TARIF_LETTRE_ECOPLI[250]

    if stickerSuivi.lower() == "oui":
        tarif += 0.5

    return tarif

#------------------------------

typeLettre = input("Choisissez un type de lettre (verte / prioritaire / éco-pli)")
poids = int(input("Quel est le poids de la lettre ? (en grammes)"))
stickerSuivi = input("Voulez-vous un sticker suivi ? (oui / non)")

tarif = affranchissement(typeLettre, poids, stickerSuivi)
print("Le tarif d'affranchissement de votre lettre est de " + tarif + " euros.")
