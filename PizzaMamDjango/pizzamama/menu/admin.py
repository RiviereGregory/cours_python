from django.contrib import admin
from .models import Pizza


# permet d'afficher les colonnes dans l'interface
class PizzaAdmin(admin.ModelAdmin):
    list_display = ('nom', 'ingredients', 'vegetarienne', 'prix')
    search_fields = ['nom']


# Register your models here.
admin.site.register(Pizza, PizzaAdmin)
