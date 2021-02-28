personne = {'nom': 'Mélanie', "age": 25, "taille": 1.60}
print(personne)

print(personne["nom"])
print(personne["age"])

personne["nom"] = "Claire"
personne["poste"] = "Développeur"

achats = ("Chocolat", "beurre", "fromage")
personne["achat"] = achats
print(personne)

for i in personne:
    print("clef : " + i)
