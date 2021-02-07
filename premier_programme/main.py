def demander_nom():
    nom_f = ""
    while nom_f == "":
        nom_f = input("Quel est votre nom ?")
    return nom_f


def demander_age(nom_personne):
    age_int = 0
    while age_int == 0:
        age_str = input(f"Quel est votre age de {nom_personne} ?")

        try:
            age_int = int(age_str)
        except:
            print("ERREUR: vous devez rentrer un nombre pour l'age")
    return age_int


def afficher_message(nom_f, age_int, taille=0):
    print()
    print(f"Vous vous appelez {nom_f}, vous avez  {age_int} ans")
    print(f"Vous aurez l'an prochain  {age_int + 1} ans")

    if age_int == 17:
        print("Vous êtes presque majeur")
    elif 12 <= age_int < 18:
        print("Adolescent")
    elif age_int == 1 or age_int == 2:
        print("Bebe")
    elif age_int == 18:
        print("Tout juste majeur : Félicitation")
    elif age_int < 10:
        print("Vous êtes enfant")
    elif age_int > 60:
        print("Vous êtes senior")
    elif age_int >= 18:
        print("Vous êtes majeur")
    else:
        print("Vous êtes mineur")

    # afficher taille
    if not taille == 0:
        print(f"votre taille {taille} m")


NB_PERSONNES = 1

for i in range(0, NB_PERSONNES):
    nom = demander_nom()
    age = demander_age(nom)
    afficher_message(nom, age, 1.80)

# nom1 = demander_nom()
# nom2 = demander_nom()
#
# age1 = demander_age(nom1)
# age2 = demander_age(nom2)
#
# afficher_message(nom1, age1)
# afficher_message(nom2, age2)
