import random

NOMBRE_MIN = 1
NOMBRE_MAX = 10


def poser_question():
    nombre_int = 0
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
            if (nombre1 + nombre2) == nombre_int:
                gagne = True
                print("Réponse correcte")
            else:
                print("Réponse incorrecte")


for i in range(0, 10):
    poser_question()
    i += 1
