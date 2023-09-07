def est_bissextile(annee:int)->bool:
    return ((annee % 4 == 0) and (annee % 100 != 0)) or (annee % 400 == 0)

def test_est_bissextile():
    print("Réponse attendue : true -----> " + str(est_bissextile(2020)))
    print("Réponse attendue : false -----> " + str(est_bissextile(999)))
    print("Réponse attendue : false -----> " + str(est_bissextile(1.05)))
    print("Réponse attendue : false -----> " + str(est_bissextile(-85)))

test_est_bissextile() 