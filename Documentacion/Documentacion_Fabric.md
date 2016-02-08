# Despliegue automático - Fabric
Para el despliegue automático, he eledigo [Fabric](http://docs.fabfile.org/), ya que es una biblioteca de Python, por lo que es la herramienta adecuada a usar con nuestro proyecto en Django.


Para ésta opción, se ha elegido realizar el despliegue en el IaaS Azure.

Empezamos instalando Fabric en nuestra máquina local:
```
sudo apt-get install fabric
```

Ahora, creamos el fichero [fabfile.py](https://github.com/Samuc/Eat-with-Rango/blob/master/fabfile.py), en el que vamos a describir las tareas de administración y despliegue para realizarlo de forma remota.
