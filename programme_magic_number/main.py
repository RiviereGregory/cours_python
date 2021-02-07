import random


def demander_nombre(nb_min, nb_max):
    nombre_int = 0
    while not nb_min <= nombre_int <= nb_max:
        nombre_str = input(f"Quel est le nombre magique (entre {nb_min} et {nb_max}) ? ")
        try:
            nombre_int = int(nombre_str)
        except:
            print("ERREUR: vous devez rentrer un nombre")
        else:
            if nombre_int < nb_min or nombre_int > nb_max:
                print(f"ERREUR: vous devez rentrer un nombre entre {nb_min} et {nb_max} ")
    return nombre_int


NOMBRE_MIN = 1
NOMBRE_MAX = 10
NOMBRE_MAGIQUE = random.randint(NOMBRE_MIN, NOMBRE_MAX)
NB_VIES = 4

"""
nombre = 0
vies = NB_VIES

while not nombre == NOMBRE_MAGIQUE and vies > 0:
    print(f"il vous reste {vies} vies")
    nombre = demander_nombre(NOMBRE_MIN, NOMBRE_MAX)
    if nombre < NOMBRE_MAGIQUE:
        print(f"le nombre magique est plus grand que {nombre}")
        vies -= 1
    elif nombre > NOMBRE_MAGIQUE:
        print(f"le nombre magique est plus petit que {nombre}")
        vies -= 1
    else:
        print(f"bravo vous avez trouvez le nombre magique {nombre}")

if vies == 0:
    print(f"vous avez perdu! Le nombre magique était : {NOMBRE_MAGIQUE}")
"""

gagne = False
for i in range(0, NB_VIES):
    vies = NB_VIES - i
    print(f"il vous reste {vies} vies")
    nombre = demander_nombre(NOMBRE_MIN, NOMBRE_MAX)
    if nombre < NOMBRE_MAGIQUE:
        print(f"le nombre magique est plus grand que {nombre}")
    elif nombre > NOMBRE_MAGIQUE:
        print(f"le nombre magique est plus petit que {nombre}")
    else:
        print(f"bravo vous avez trouvez le nombre magique {nombre}")
        gagne = True
        break

if not gagne:
    print(f"vous avez perdu! Le nombre magique était : {NOMBRE_MAGIQUE}")
