import json

import requests

url = "https://jrpizzamamadjangogri.herokuapp.com/api/GetPizzas"

data = requests.get(url)

# print(data.text)

pizzas = json.loads(data.text)
# print(pizzas)
# print(len(pizzas))

print("Liste des pizzas :")
for pizzaModel in pizzas:
    pizza = pizzaModel['fields']
    print(pizza['nom'] + " : " + str(pizza['prix'])+"€")
