class Pizza:
    def __init__(self, nom, prix):
        self.nom = nom
        self.prix = prix


pizzas = [
    Pizza("Calzonne", 8),
    Pizza("4 fromages", 9.5),
    Pizza("Hawai", 12)
]

# Récupérer le nom des pizzas dans une liste
nom_pizzas = [pizza.nom for pizza in pizzas]

print(nom_pizzas)

# 2 - ANY
pizza_chere_existe = any([pizza.prix > 10 for pizza in pizzas])
print(pizza_chere_existe)

# 3 - SUM
nb_pizza_chere_existe = sum([1 for pizza in pizzas if pizza.prix > 10])
print(nb_pizza_chere_existe)

# 4 - ZIP (fusion de liste)

pizzas_nom = ("4 fromages", "Calzonne", "Hawai")
pizzas_prix = (10.5, 11, 8)

noms_et_prix = list(zip(pizzas_nom, pizzas_prix))

print(noms_et_prix)

for (nom, prix) in zip(pizzas_nom, pizzas_prix):
    print(f"{nom} - {prix}€")

# séparration des listes
unzipped = list(zip(*noms_et_prix))
print(unzipped)
pn, pp = list(zip(*noms_et_prix))
print(pn)
print(pp)
