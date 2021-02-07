import random

NOMBRE_MIN = 1
NOMBRE_MAX = 10
NB_QUESTION = 5


def poser_question(ope):
    global nombre_de_reponse
    nombre_int = 0
    nb_faux = 0
    gagne = False
    nombre1 = random.randint(NOMBRE_MIN, NOMBRE_MAX)
    nombre2 = random.randint(NOMBRE_MIN, NOMBRE_MAX)
    while nombre_int == 0 or not gagne:
        nombre_str = input(f"Calculez: {nombre1} {ope} {nombre2} = ")
        try:
            nombre_int = int(nombre_str)
        except:
            print("ERREUR: vous devez rentrer un nombre")
        else:
            nombre_de_reponse += 1
            calcul = nombre1 * nombre2
            if ope == "+":
                calcul = nombre1 + nombre2

            if calcul == nombre_int:
                gagne = True
                print("Réponse correcte")
            else:
                print("Réponse incorrecte")
                nb_faux += 1
    return 0 if not nb_faux == 0 else 1


def choix_operateur():
    operateur_int = -1
    while operateur_int == -1 or not 0 <= operateur_int <= 2:
        operateur_str = input(f"Quel opérateur pour les questions : + (0) ,* (1) ou hasard (2) : ")
        try:
            operateur_int = int(operateur_str)
        except:
            print("ERREUR: vous devez rentrer un nombre")
    return operateur_int


def appreciation():
    moyenne = int(NB_QUESTION / 2)
    if nb_de_point == NB_QUESTION:
        print("Excellent!")
    elif nb_de_point == 0:
        print("Révisez vos maths!")
    elif nb_de_point > moyenne:
        print("Pas mal")
    else:
        print("Peut mieux faire")


nombre_de_reponse = 0
nb_de_point = 0

operateur_utilisateur = choix_operateur()
choix_operateur = operateur_utilisateur

for i in range(0, NB_QUESTION):
    if operateur_utilisateur == 2:
        choix_operateur = random.randint(0, 1)

    operateur = "+" if choix_operateur == 0 else "*"
    i += 1
    print(f"Question {i}/{NB_QUESTION} :")
    nb_de_point += poser_question(operateur)
    print()

print(f"{nombre_de_reponse} propositions pour {NB_QUESTION} questions")
print(f"Scores: {nb_de_point} / {NB_QUESTION} ")

appreciation()
