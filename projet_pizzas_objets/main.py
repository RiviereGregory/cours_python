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


class PizzaPersonalisee(Pizza):
    PRIX_DE_BASE = 7
    PRIX_PAR_INGREDIENT = 1.2

    def __init__(self, numero):
        self.numero = numero
        super().__init__(f"Personnalisée {numero}", 0, [])
        self.demander_ingredients_utilisateur()
        self.caluler_prix()

    def demander_ingredients_utilisateur(self):
        print()
        print(f"Ingrédients pour la pizza personalisée {self.numero}")
        while True:
            ingredient = input(f"Ajoutez un ingrédient (ou ENTER pour terminer) :")
            if ingredient == "":
                return
            self.ingredients.append(ingredient)
            print(f"""vous avez {len(self.ingredients)} ingrédient(s) : {", ".join(self.ingredients)}""")

    def caluler_prix(self):
        self.prix = PizzaPersonalisee.PRIX_DE_BASE + (len(self.ingredients) * PizzaPersonalisee.PRIX_PAR_INGREDIENT)


pizzas = [Pizza("4 fromages", 8.5, ("brie", "emmental", "comté", "parmesan", "sauce tomate"), True),
          Pizza("Jambon", 9, ("jambon", "emmental", "crème")),
          Pizza("Corsica", 10.5, ("brucciu", "emmental", "figatéli", "sauce tomate")),
          Pizza("mozzarella", 8.5, ("mozarella", "crème"), True),
          PizzaPersonalisee(1),
          PizzaPersonalisee(2)]


def tri(e):
    return e.nom


pizzas.sort(key=tri)

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
