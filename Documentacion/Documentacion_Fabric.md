# Despliegue automático - Fabric
Para el despliegue automático, he eledigo [Fabric](http://docs.fabfile.org/), ya que es una biblioteca de Python, por lo que es la herramienta adecuada a usar con nuestro proyecto en Django.


Para ésta opción, se ha elegido realizar el despliegue en el IaaS Azure.

Empezamos instalando Fabric en nuestra máquina local:
```
sudo apt-get install fabric
```

Ahora, creamos el fichero [fabfile.py](https://github.com/Samuc/Eat-with-Rango/blob/master/fabfile.py), en el que vamos a describir las tareas de administración y despliegue para realizarlo de forma remota.

**fabfile.py**
```
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

```

Para ello, he utilizado también un fichero [Makefile](https://github.com/Samuc/Eat-with-Rango/blob/master/Makefile):
** Makefile **
```
install:
	sudo apt-get update
	sudo apt-get install -y python-setuptools
	sudo apt-get install -y python-dev
	sudo apt-get install -y build-essential
	sudo apt-get install -y git
	sudo apt-get install -y pkg-config
	sudo apt-get install -y libtiff4-dev
	sudo apt-get install -y libjpeg8-dev
	sudo apt-get install -y zlib1g-dev
	sudo easy_install pip
	sudo -H pip install Pillow --upgrade
	sudo pip install django --upgrade
	sudo pip install -r requirements.txt

test:
	python manage.py test

run:
	sudo python manage.py runserver 0.0.0.0:80


azure:
	fab -H vagrant@40.78.150.231:22 downloadApp
	fab -H vagrant@40.78.150.231:22 install
	fab -H vagrant@40.78.150.231:22 test
	fab -H vagrant@40.78.150.231:22 runApp
```

La dirección de la máquina que he creado para ésta documentación es 40.78.150.231 y el usuario vagrant.
Dirección temporal: http://eatrango-service-wecdl.cloudapp.net/

En el archivo fabfile.py, hemos definido una serie de funciones, a las que podemos llamar con la siguiente orden:
`fab -H vagrant@40.78.150.231:22 <nombre_funcion>`

Insertamos nuestra contraseña, y se ejecutará esa función en la máquina azure.

![ejecución install](http://i.cubeupload.com/TV4dbm.jpg)


Entonces, el orden a seguir será:
Descargar APP:
```
	fab -H vagrant@40.78.150.231:22 downloadApp
```
Instalar dependencias:
```
	fab -H vagrant@40.78.150.231:22 install
```
Ejecutar test:
```
	fab -H vagrant@40.78.150.231:22 test
```
Ejecutar aplicación:
```
	fab -H vagrant@40.78.150.231:22 runApp
```

Al terminar las 4 órdenes, se ejecutará en la máquina la apliación, tal como vemos en la siguiente imagen:
![App corriendo utilizando fabric ](http://i.cubeupload.com/oiHhfI.jpg)


Si hacemos el test:
![test con fabric ](http://i.cubeupload.com/YH7MjR.jpg)
