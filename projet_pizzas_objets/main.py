# nom, prix, ingredients, végétarienne

class Pizza:
    def __init__(self, nom, prix, ingredients, vegetarienne=False):
        self.nom = nom
        self.prix = prix
        self.ingredients = ingredients
        self.vegetarienne = vegetarienne

    def afficher(self):
        veg_str = ""
        if self.vegetarienne:
            veg_str = " - VEGETARIENNE"

        print(f"PIZZA {self.nom} : {self.prix}€" + veg_str)
        print(", ".join(self.ingredients))
        print()


pizzas = (Pizza("4 fromages", 8.5, ("brie", "emmental", "comté", "parmesan", "sauce tomate"), True),
          Pizza("Jambon", 9, ("jambon", "emmental", "crème")),
          Pizza("Corsica", 10.5, ("brucciu", "emmental", "figatéli", "sauce tomate")),
          Pizza("mozzarella", 8.5, ("mozarella", "crème"), True))

print("--- Pizza végétarienne ---")
for pizza in pizzas:
    if pizza.vegetarienne:
        pizza.afficher()
print("--- Pizza non végétarienne ---")
for pizza in pizzas:
    if not pizza.vegetarienne:
        pizza.afficher()
print("--- Pizza sauce tomate ---")
for pizza in pizzas:
    if "sauce tomate" in pizza.ingredients:
        pizza.afficher()
print("--- Pizza moins de 10€ ---")
for pizza in pizzas:
    if pizza.prix < 10:
        pizza.afficher()
