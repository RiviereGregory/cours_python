import random

NOMBRE_MIN = 1
NOMBRE_MAX = 10
NB_QUESTION = 10


def poser_question():
    global nombre_de_reponse
    nombre_int = 0
    nb_faux = 0
    gagne = False
    nombre1 = random.randint(NOMBRE_MIN, NOMBRE_MAX)
    nombre2 = random.randint(NOMBRE_MIN, NOMBRE_MAX)
    while nombre_int == 0 or not gagne:
        nombre_str = input(f"Calculez: {nombre1} + {nombre2} = ")
        try:
            nombre_int = int(nombre_str)
        except:
            print("ERREUR: vous devez rentrer un nombre")
        else:
            nombre_de_reponse += 1
            if (nombre1 + nombre2) == nombre_int:
                gagne = True
                print("Réponse correcte")
            else:
                print("Réponse incorrecte")
                nb_faux += 1
    return 0 if not nb_faux == 0 else 1


nombre_de_reponse = 0
nb_de_point = 0
for i in range(0, NB_QUESTION):
    i += 1
    print(f"Question {i}/{NB_QUESTION} :")
    nb_de_point += poser_question()
    print()

print(f"{nombre_de_reponse} propositions pour {NB_QUESTION} questions")
print(f"Scores: {nb_de_point} / {NB_QUESTION} ")
