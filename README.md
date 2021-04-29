Cours et exercice python
=============================

**Installation Django**  
Dans Pycharm --> créer un nouveau projet  
Dans Pycharm --> aller dans le terminal et faire pip install django  
Dans Pycharm --> aller dans le terminal et django-admin starproject pizzamama  


**Lancer Django**  
Dans Pycharm --> aller dans le terminal et aller où est le fichier manage.py et faire python manage.py runserver  

**Création menu Django**  
Dans Pycharm --> aller dans le terminal et aller où est le fichier manage.py et faire python manage.py startapp menu  

**Création base de données Django**  
Ajouter le chemin dans le settings.py au niveau des INSTALLED_APPS : 'menu.apps.MenuConfig',  
puis faire dans le terminal python manage.py makemigrations  
puis faire dans le terminal python manage.py migrate  

**Ajout Kivy**  
Faire un pip install kivy directement sur la version de python pas sur venv  
Attention si probleme d'opengl 1.1 non compatible :  
soit ajouter dans le fichier py :  
import os  
os.environ['KIVY_GL_BACKEND'] = 'angle_sdl2'  
  
soit : ajouter une variable system KIVY_GL_BACKEND:angle_sdl2  

liens aide kivy  
https://kivy.org/doc/stable/gettingstarted/layouts.html  

