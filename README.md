# Eat-with-Rango-Bares-Tapas
Final proyect for IV course - University of Granada

# Descripción

Este proyecto  está desarrollado para las asignaturas IV (Infraestructura Virtual) y DAI (Diseño de Aplicaciones de Internet) de la UGR (Universidad de Granada).

Se ha realizado conjuntamente para las dos asignaturas porque en DAI desarrollamos la aplicación web y el objetivo del proyecto de IV es proporcionar soporte, mediante una infraestructura virtual a dicha aplicación.


 La idea se centra en una aplicación web que contiene información acerca de bares que visitar, la localización de éstos, las tapas que hay disponibles.

En cada bar mostrará las visitas que ha generado, cada vez que se visite la sección de ese bar en la aplicación, subirán sus visitas.

Cada bar, tendrá su lista de tapas, a las que se podrá votar (con un like), para ver cuáles gusta más a los usuarios.

La aplicación contiene un formulario de Login y de Registro.

El registro de usuarios permite añadir una imagen de avatar para el perfil del usuario.

Los usuarios logeados, podrán hacer "logout", añadir Bares, y añadir tapas a esos bares.

Cada bar, se podrá crear añadiendo su nombre y una dirección.
Gracias a ésta dirección, si está bien escrita, una vez se visualice el bar y la lista de tapas, debajo mostrará un mapa (con easy_maps) localizando el bar en su dirección correcta.

Al añadir tapa, se insertará el nombre de la tapa y el bar al que pertenece.

Una vez insertada, a ésta tapa podremos darle a "like" y su contador irá subiendo al refrescar la página. Igual que las visitas de cada bar.

Toda ésta información se guardará permanentemente en la base de datos.

Contiene diferentes botones botones para cambiar el tamaño de la letra.

También, contiene una sección Hightchart, donde se monitoriza las visitas de los bares, mostrando una gráfica con relación nombre del bar y número de visitas.



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

Para la instalación de dependencias hace uso de un archivo requirements.txt.
Para instalar las dependencias ejecutamos:
`sudo pip install -r requirements.txt`

Para ejecutar la apliación:
`python manage.py runserver`

Ésto ejecutará la apliación en el puerto 8000 por defecto.

Podemos utilizar cualquiera que queramos y que esté disponible o libre.
En el caso de tener el puerto 80 libre, podemos asignarselo con:
`sudo pytho manage.py runserver 0.0.0.0:80`


# Desarrollo basado en pruebas
Para los tests para el despliegue de la aplicación, Django ofrece su propio sistema, utilizando un archivo *test.py*,  que contendrá los tests que queramos hacerle a la aplicación.

Los tests se pueden ejecutar con:
`python manage.py test`
