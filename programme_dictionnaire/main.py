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

# --- PARTIE 2---

# noms age,taille

personnes = [
    ("Mélanie", 25, 1.6),
    ("Paul", 29, 1.8),
    ("Jacques", 35, 1.75),
    ("Martin", 16, 1.65)
]


def obtenir_information(nom, liste):
    for i in liste:
        if i[0] == nom:
            return i
    return None


# Jacques
infos = obtenir_information("Jacques", personnes)
print(infos)

# Avec dictionnaire
personnes_dict = {
    "Mélanie": (25, 1.6),
    "Paul": (29, 1.8),
    "Jacques": (35, 1.75),
    "Martin": (16, 1.65)
}

# acces direct à l'info sans boucle
infos_dic = personnes_dict.get("Jacques")
print(infos_dic)
infos_dic = personnes_dict.get("Claire")
print(infos_dic)
