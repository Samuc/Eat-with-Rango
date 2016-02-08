from fabric.api import run, local, hosts, cd
from fabric.contrib import django


#Descarga el repositorio
def downloadApp():
	run('sudo apt-get update')
	run('sudo apt-get install -y git')
    	run('sudo rm -rf Eat-with-Rango/')
   	run('sudo git clone https://github.com/Samuc/Eat-with-Rango.git')


#Instalar las dependencias necesarias
def install():
    run('sudo apt-get install -y make')
    run('cd Eat-with-Rango/ && sudo make install')

#Ejecucion de test
def test():
	run('cd Eat-with-Rango/ && sudo python manage.py test')

#Ejecucion de la aplicacion
def runApp():
	run('cd Eat-with-Rango/ && sudo python manage.py runserver 0.0.0.0:80')
