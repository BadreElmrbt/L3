#Partie 1 - Listes en compréhension

#Question 1
def listeMultiples(binf:int,bsup:int,nb:int)->list:
    lst = list(range(binf,bsup+1))
    return [x for x in lst if x%nb==0]

lstMulti = listeMultiples(10,50,5)
print("Test listeMultiples : ", lstMulti)

#Question 2
def ajouter(lst:list,nb:int)->list:
    return [x+nb for x in lst]

lstAjout = ajouter([1,2,3,4,5,6,7,8,9,10],10)
print("Test listeAjout : ", lstAjout)

#Question 3
def ajouterSiSup(lst:list,val:int,nb:int)->list:
    lst2 = list(lst)
    return [x+nb if x >= val else x for x in lst2 ]

ajoutSiSup = ajouterSiSup([1,2,3,4,5,6,7,8,9,10],8,10)
print("Test ajoutSiSup : ", ajoutSiSup)

#Question 4
def bissextiles(adeb:int,afin:int)->list:
    lst = list(range(adeb,afin+1))
    return [annee for annee in lst if ((annee % 4 == 0) and (annee % 100 != 0)) or (annee % 400 == 0)]

anneeBissextiles = bissextiles(2010,2020)
print("Test bissextiles : ", anneeBissextiles)

#Question 5
def premiers(binf:int, bsup:int)->list:
    lst = list(range(binf+1,bsup))
    for n in range(2,10):
        lst = [x for x in lst if x <= n or x%n!=0] 
    return lst

nbrPremiers = premiers(10,50)
print("Test premiers : ",nbrPremiers)