# Colelctions : Tableaux, Listes, Tuples...
# Tuple () : immutable --> non modifiable
# Liste [] : mutable --> modifiable

a = 5
b = "toto"

# Tuple
print("##### Tuple ######")
print()
personnes = ("Mélanie", "Jean", "Martin", "Alice")
print(len(personnes))
print(personnes[0])
# -1 pour le dernier élement, -2 l'avant dernier ...
print(personnes[-1])

print()
print("personnes[i] boucle for")
for i in range(0, len(personnes)):
    print(personnes[i])

print()
print("personnes pour boucle for")
for i in personnes:
    print(i)
    print(len(i))
    print(i[-1])

# Liste
print()
print("##### Liste ######")
print()
personnesListe = ["Mélanie", "Jean", "Martin", "Alice"]
print(personnesListe)
print()

# Ajout dans liste
nouvelle_persone = "David"
personnesListe.append(nouvelle_persone)
print(personnesListe)
print()

# suppression dans la liste
del personnesListe[1]
print(personnesListe)
print()


def afficher_personnes(c):
    for i in c:
        print(i)


afficher_personnes(personnesListe)

print()
# Fonction et tuples
print("##### Fonction et tuples ######")
print()


def obtenir_information():
    return "Mélanie", 37, 1.60


def afficher_information(nom, age, taille):
    print(f"nom : {nom} , age : {age} , taille : {taille}")


infos = obtenir_information()
print("nom : " + infos[0])
print("age : " + str(infos[1]))
print("taille : " + str(infos[2]))

nom, age, taille = obtenir_information()
afficher_information(nom, age, taille)

# * devant le tuple permet de mettre les 3 valeurs
afficher_information(*infos)

print()
# Slice
print("##### Slice ######")
print()

personnesSlice = ("Mélanie", "Jean", "Martin", "Alice")

# [start:stop:step]
for i in personnesSlice[0:2]:
    print(i)

print()

for i in personnesSlice[::2]:
    print(i)

# afficher mot à l'envers
mots = "un mot"
print(mots[::-1])
