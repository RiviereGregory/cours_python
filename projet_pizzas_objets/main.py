# nom, prix, ingredients, végétarienne

class Pizza:
    def __init__(self, nom, prix, ingredients):
        self.nom = nom
        self.prix = prix
        self.ingredients = ingredients

    def afficher(self):
        print(f"PIZZA {self.nom} : {self.prix}€")
        print(", ".join(self.ingredients))
        print()


pizzas = (Pizza("4 fromages", 8.5, ("brie", "emmental", "comté", "parmesan")),
          Pizza("Jambon", 9, ("jambon", "emmental", "crème")),
          Pizza("Corsica", 10.5, ("brucciu", "emmental", "figatéli", "sauce tomate")),
          Pizza("mozzarella", 8.5, ("mozarella", "crème")))

for pizza in pizzas:
    pizza.afficher()
