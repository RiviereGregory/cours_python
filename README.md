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


**Ajout Audiostream**  
- pip install Cython  
- python -m pip install docutils pygments pypiwin32 kivy_deps.sdl2 kivy_deps.glew
- Téléchargez le fichier "audiostream.zip"
- Dézippez dans c:\audiostream
- Allez dans ce répertoire dans le terminal : cd \audiostream
- tapez la commande : set USE_SDL2=1
- python setup.py install

- Si vous avez l'erreur "error: Unable to find vcvarsall.bat"  
        -> Installez Visual studio 15 : https://my.visualstudio.com/Downloads?q=visual%20studio%202015&wt.mc_id=o~msft~vscom~older-downloads  
        -> Fermez et réouvrez votre terminal en mode administrateur, et retournez dans votre répertoire ("cd \audiostream"), puis refaites "python setup.py install"  
- Si erreur encore compilateur installer msgw  
	http://www.rose-hulman.edu/class/csse/binaries/MinGW/mingw-get-inst-20110530.exe  
	modifier pyhton\Lib\distutils en ajoutant le fichier :  
		distutils.cfg  
			[build]  
			compiler=mingw32  
		et modifier le fichier cygwinccompiler.py  :
		elif msc_ver == '1700':  
            return ['msvcr110']  
        elif msc_ver == '1800':  
            return ['msvcr120']  
        elif msc_ver == '1900':  
            return ['vcruntime140']  

Pour vérifier que tout fonctionne bien:  
- Allez dans le répertoire examples\sinslider  
- python main.py  
- Un programme devrait s'ouvrir et jouer un son.  


