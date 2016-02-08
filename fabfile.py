from fabric.api import run, local, hosts, cd
from fabric.contrib import django


#Descargar la app
def getApp():
	run('sudo apt-get update')
	run('sudo apt-get install -y git')
   	run('sudo git clone https://github.com/Samuc/Eat-with-Rango.git')

def onlygetRepo():
    run('sudo git clone https://github.com/Samuc/Eat-with-Rango.git')

#Instalar la app
def install():
    run('sudo apt-get install make')
    run('cd Eat-with-Rango/ && sudo make install')

#Ejecucion de test
def test():
	run('cd Eat-with-Rango/ && sudo python manage.py test')

#Ejecucion de la aplicacion
def runApp():
	run('cd Eat-with-Rango/ && sudo python manage.py runserver 0.0.0.0:80')


#Crea la maquina en azure
def crearMaquina():
	run('cd Eat-with-Rango/ && make crearAzure')

#Provisiona la maquina en azure
def provisionarMaquina():
	run('cd Eat-with-Rango/ && make provisionAzure')
