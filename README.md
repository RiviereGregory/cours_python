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

Pour linux avec conda  
  Création env  
    conda create --prefix /media/greg/EXTGREG/telechargement/conda/.conda/envs/kivy_env python=3.9 anaconda  
  Activation env  
    conda activate kivy_env  

    sudo apt install ffmpeg libavcodec-dev libavdevice-dev libavfilter-dev libavformat-dev libavutil-dev libswscale-dev libswresample-dev libpostproc-dev libsdl2-dev libsdl2-2.0-0 libsdl2-mixer-2.0-0 libsdl2-mixer-dev python3-dev  
    pip install --no-binary kivy kivy  

    conda update --all && conda clean -p  

Pour lancer pycharm sous linux  
  cd /media/greg/DISQUE2/pycharm-community-2021.1.1/bin  
  source ./pycharm.sh  

  Pour l'interpreteur python il faut mettre /media/greg/EXTGREG/telechargement/conda/.conda/envs/kivy_env/bin/python3  

  il faut mettre dan pycharm.sh le path pour PYCHARM_JDK=/usr/lib/jvm/default-java/  
