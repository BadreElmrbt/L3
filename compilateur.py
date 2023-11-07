class Pile:
    def __init__(self):
        self.elements = []
        self.SP = -1  # Initialisation du pointeur de pile

    def empiler(self, element):
        self.elements.append(element)
        self.SP += 1

    def depiler(self):
        if not self.est_vide():
            self.SP -= 1
            return self.elements.pop()

    def sommet(self):
        if not self.est_vide():
            return self.elements[-1]

    def est_vide(self):
        return len(self.elements) == 0


def executer_instruction(pile, instruction):
    global PC
    global breaker
    op = instruction[0]
    match op:
        case "ADD":
            a = pile.depiler()
            b = pile.depiler()
            pile.empiler(a + b)
        case "SUB":
            a = pile.depiler()
            b = pile.depiler()
            pile.empiler(b - a)
        case "MUL":
            a = pile.depiler()
            b = pile.depiler()
            pile.empiler(a * b)
        case "DIV":
            a = pile.depiler()
            b = pile.depiler()
            pile.empiler(b // a)
        case "EQL":
            a = pile.depiler()
            b = pile.depiler()
            pile.empiler(1 if a == b else 0)
        case "NEQ":
            a = pile.depiler()
            b = pile.depiler()
            pile.empiler(1 if a != b else 0)
        case "GTR":
            a = pile.depiler()
            b = pile.depiler()
            pile.empiler(1 if b > a else 0)
        case "LSS":
            a = pile.depiler()
            b = pile.depiler()
            pile.empiler(1 if b < a else 0)
        case "GEQ":
            a = pile.depiler()
            b = pile.depiler()
            pile.empiler(1 if b >= a else 0)
        case "LEQ":
            a = pile.depiler()
            b = pile.depiler()
            pile.empiler(1 if b <= a else 0)
        case "PRN":
            print(pile.depiler())
        case "INN":
            adresse = pile.depiler()
            valeur = int(input("Entrez une valeur : "))
            pile.empiler(valeur)
        case "INT":
            c = instruction[1]
            pile.SP += c
        case "LDI":
            v = instruction[1]
            pile.empiler(v)
        case "LDA":
            a = instruction[1]
            pile.empiler(a)
        case "LDV":
            adresse = pile.depiler()
            valeur = MEM[adresse]
            pile.empiler(valeur)
        case "STO":
            valeur = pile.depiler()
            adresse = pile.depiler()
            MEM[adresse] = valeur
        case "BRN":
            i = instruction[1]
            PC = i - 1
        case "BZE":
            i = instruction[1]
            condition = pile.depiler()
            if condition == 0:
                PC = i - 1
        case "HLT":
            breaker = True
    


def executer_code(pile, P_CODE):
    global PC
    global breaker
    while PC < len(P_CODE) and breaker != True:
        INST = P_CODE[PC]
        executer_instruction(pile, INST)
        print(PC)
        PC += 1


# Initialisation de la pile
MEM = Pile()
PC = 0
breaker = False

# Initialisation du tableau d'instructions P_CODE
P_CODE = [
    ("LDI", 10),  #Empile la valeur 10 sur la pile
    ("LDI", 20),  #Empile la valeur 20 sur la pile
    ("ADD",), #Additionne les deux valeurs au sommet de la pile (20 + 10) et empile le résultat (30)
    #("BRN",1), 
    ("PRN",),  #Affiche le sommet de la pile (30) et le dépile
    ("HLT",),  #Arrête l'exécution
]

# Exécute le code avec la pile, les instructions et la mémoire
executer_code(MEM, P_CODE)
