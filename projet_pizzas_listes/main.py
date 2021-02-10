# Exemple pour trier par la long des chaines
def tri_personnalise(element):
    return len(element)


def afficher(collection, nb_pizzas_affiche=-1):
    nb_pizzas = len(collection)
    if nb_pizzas == 0:
        print("--- AUCUNE PIZZA ---")
        return

    liste_pizzas = collection
    if not nb_pizzas_affiche == -1:
        liste_pizzas = collection[:nb_pizzas_affiche]

    # trie personnalisé
    # liste_pizzas.sort(key=tri_personnalise)
    # trie personnalisé inversé
    # liste_pizzas.sort(reverse=True, key=tri_personnalise)
    # trie par ordre alphabetique
    # liste_pizzas.sort()
    # trie par ordre alphabetique inversé
    # liste_pizzas.sort(reverse=True)
    print(f"---- LISTE DES PIZZAS ({len(liste_pizzas)}) ----")
    for pizza in liste_pizzas:
        print(pizza)

    print()
    print("Première pizza " + liste_pizzas[0])
    print("Dernière pizza " + liste_pizzas[-1])


def ajouter_pizza_utilisateur(collection):
    nouvelle_pizza = input("Pizza à ajouter : ")
    # if pizza_existe(collection, nouvelle_pizza):
    # équivalent en python
    if nouvelle_pizza.lower() in collection:
        print("ERREUR : La pizza existe déjà")
        return
    collection.append(nouvelle_pizza.lower())


def pizza_existe(collection, nouvelle_pizza):
    for pizza in collection:
        if pizza == nouvelle_pizza:
            return True
    return False


pizzas = ["4 fromages", "végétarienne", "hawai", "calzonne"]
vide = ()
afficher(pizzas)
print()
ajouter_pizza_utilisateur(pizzas)
print()
afficher(pizzas)
print()
afficher(vide)
print()
afficher(pizzas, 3)
print()
