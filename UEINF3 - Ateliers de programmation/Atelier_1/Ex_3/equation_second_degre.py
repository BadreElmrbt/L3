from math import sqrt

def discriminant(a: float, b: float, c: float)->float:
    return b**2 - 4*a*c

def racine_unique(a: float, b: float)->float:
    return -b / (2*a)

def racine_double(a: float, b: float, delta: float, num: int)->float:
    if num == 1:
        return (-b + sqrt(delta)) / (2*a)
    elif num == 2:
        return (-b - sqrt(delta)) / (2*a)
    else:
        return False

def str_equation(a: float, b: float, c: float)->str:
    return str(a) + "x² + " + str(b) + "x + " + str(c) + " = 0"

def solution_equation(a: float, b: float, c: float)->str:
    delta = discriminant(a, b, c)
    equation_litteral = str_equation(a, b, c)
    reponse_finale = "Solution de l'équation " + equation_litteral + " ; "
    if delta < 0:
        reponse_finale += "Pas de racine réelle"
    elif delta == 0:
        x = racine_unique(a, b)
        reponse_finale += "Racine unique : x = " + str(x)
    elif delta > 0:
        x1 = racine_double(a, b, delta, 1)
        x2 = racine_double(a, b, delta, 2)
        reponse_finale += "Deux racines : x1 = " + str(x1) + " ; x2 = " + str(x2)
    return reponse_finale

def equation(a: float, b: float, c: float):
    print(solution_equation(a, b, c))

def test_equation():
    print("Réponse attendue : x1=2 et x2=1 -----> " + str(solution_equation(1,-3,2)))
    print("Réponse attendue : x=-1 -----> " + str(solution_equation(2,4,2)))
    print("Réponse attendue : pas de racine réellle -----> " + str(solution_equation(1,2,5)))

test_equation() 