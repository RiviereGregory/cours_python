from django.http import HttpResponse

from .models import Pizza


# Create your views here.

def index(request):
    pizzas = Pizza.objects.all()
    pizzas_names_and_price = [pizza.nom + " : " + str(pizza.prix) + "€" for pizza in pizzas]
    pizzas_names_str = ", ".join(pizzas_names_and_price)
    return HttpResponse("Les pizzas : " + pizzas_names_str)
