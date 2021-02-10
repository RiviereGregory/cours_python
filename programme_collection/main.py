# Colelctions : Tableaux, Listes, Tuples...
# Tuple () : immutable --> non modifiable
# Liste [] : mutable --> modifiable

a = 5
b = "toto"

# Tuple
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



