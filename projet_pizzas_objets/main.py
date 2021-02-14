# nom, prix, ingredients, végétarienne

class Pizza:
    def __init__(self, nom, prix):
        self.nom = nom
        self.prix = prix

    def afficher(self):
        print(f"PIZZA {self.nom} : {self.prix}€")


pizza1 = Pizza("4 fromages", 8.5)
pizza1.afficher()
