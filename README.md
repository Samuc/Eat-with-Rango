# Eat-with-Rango-Bares-Tapas
Final proyect for IV course - University of Granada


[![Build Status](https://travis-ci.org/Samuc/Eat-with-Rango.svg)](https://travis-ci.org/Samuc/Eat-with-Rango)

[![Snap-CI](https://snap-ci.com/Samuc/Eat-with-Rango/branch/master/build_image)](https://snap-ci.com/Samuc/Eat-with-Rango/branch/master)

[![Azure](http://azuredeploy.net/deploybutton.png)](http://rango2-service-rknsl.cloudapp.net/rango/)


# Descripción - Eat with Rango
Este proyecto  está desarrollado para las asignaturas IV (Infraestructura Virtual) y DAI (Diseño de Aplicaciones de Internet) de la UGR (Universidad de Granada).

Se ha realizado conjuntamente para las dos asignaturas porque en DAI desarrollamos la aplicación web y el objetivo del proyecto de IV es proporcionar soporte, mediante una infraestructura virtual a dicha aplicación.

La idea se centra en una aplicación web que contiene información acerca de bares que visitar, la localización de éstos, las tapas que hay disponibles.

Para una descripción más extendida, ir la [descripción documentada](https://github.com/Samuc/Eat-with-Rango/blob/master/Documentacion/Descripcion.md).

# Infraestructura
Par la aplicación web necesitamos un soporte que ofrezca una infraestructura que cuente con un servidor web para desplegar la aplicación y que se ejecute en él.
Debe utilizar la base de datos alojada en el servidor, en la que se almacenará la información necesaria para la aplicación.

La infraestructura que he utilizado en este proyecto me las ha proporcionado varias opciones.
Entre ellas, una plataforma PaaS como es heroku, y  las máquinas virtuales que me proporciona la IaaS Azure.


# Herramientas usadas
- Para desarrollar la aplicación se ha usado el framework de Python Django.
- La base de datos que usa es SQLite 3.
- Bootstrap para el estilo de aplicación web
- Paquete django-registration-redux para el registro y login de usuarios
- Paquete django-easy-maps para mostrar en un mapa la localización de los bares
- Snap-CI y Travis para la integración contínua
- Como servicio PaaS he usado Heroku
- Como servicio IaaS he usado Azure


La herramienta de construcción que utiliza el proyecto de Django es **manage.py**, el cual permite realizar varias operaciones de control y ejecutar la aplicación.

## Requerimientos
Para la instalación de dependencias hace uso del archivo requirements.txt, que podemos ver [aqui](https://github.com/Samuc/Eat-with-Rango/blob/master/requirements.txt).

Para instalar las dependencias ejecutamos:
`sudo pip install -r requirements.txt`

Para ejecutar la apliación:
`python manage.py runserver`

Ésto ejecutará la apliación en el puerto 8000 por defecto.

Podemos utilizar cualquiera que queramos y que esté disponible o libre.
En el caso de tener el puerto 80 libre, podemos asignarselo con:
`sudo pytho manage.py runserver 0.0.0.0:80`


# Desarrollo basado en pruebas
Para los tests para el despliegue de la aplicación, Django ofrece su propio sistema, unittest, utilizando un archivo *test.py*,  que contendrá los tests que queramos hacerle a la aplicación.

Los tests se pueden ejecutar con:
`python manage.py test`

El archivo tests.py se encuentra [aquí](https://github.com/Samuc/Eat-with-Rango/blob/master/tests.py)

Éste tests, comproborará los casos de acceso a las diferentes páginas de la aplicación web con respuesta de OK, creación de bares y acceso a la página del mismo, y creación de tapas.

Si queremos saber más sobre el sistema de tests de Django, podemos entrar [aquí](https://docs.python.org/2/library/unittest.html).

![Tests](http://i.cubeupload.com/4mAUi8.jpg)


# Integración contínua - Travis-CI
Para la automatización del proceso de pruebas y para desarrollar el proyecto bajo el concepto de Integración Contínua, he usado [Travis-CI](https://travis-ci.org/) para la integración continua. La configuración para Travis-CI se indica en el fichero .travis.yml.

Para más información, ir [Documentación - Integración Contínua Travis](https://github.com/Samuc/Eat-with-Rango/blob/master/Documentacion/Documentacion_Travis.md).


# Integración contínua - SNAP-CI
También hemos integrado contínuamente la aplicación en SNAP-CI.

Para más información, ir [Documentación - Integración Contínua Snap](https://github.com/Samuc/Eat-with-Rango/blob/master/Documentacion/Documentacion_Snap.md).


# Despliegue en un Iaas - Azure
Para mi aplicación he elegido como servicio IaaS, usar [Azure](https://azure.microsoft.com/es-es/).

Y para realizar el despliegue en Azure, he usado las herramientas [Ansible](http://www.ansible.com/) y [Vagrant](https://www.vagrantup.com/).


Para más información sobre el despliegue, ir a [Documentación - Despliegue en Azure](https://github.com/Samuc/Eat-with-Rango/blob/master/Documentacion/Documentacion_Azure.md).


Una vez terminado el despligue, podemos ver la apliacicón en la página web de la máquina creada en Azure:
![Captura de Eat-with-Rango desplegada con Vagrant en Azure](http://i.cubeupload.com/JwiErb.jpg)
La url sobre la que está corriendo actualmente mi aplicación es: http://rango2-service-rknsl.cloudapp.net/rango/
La web estará activa temporalmente, hasta que la suscripción con Azure termine.
