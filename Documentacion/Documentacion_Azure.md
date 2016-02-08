# Despliegue en un Iaas - Azure
[![Azure](http://azuredeploy.net/deploybutton.png)](http://rango2-service-rknsl.cloudapp.net/rango/)

Para mi aplicación he elegido como servicio IaaS, usar [Azure](https://azure.microsoft.com/es-es/).

Y para realizar el despliegue en Azure, he usado las herramientas [Ansible](http://www.ansible.com/) y [Vagrant](https://www.vagrantup.com/).


Vamos a configurar el Vagrantfile para crear una máquina de Azure donde desplegar la aplicación.

Antes de todo, si no tenemos instalado VirtualBox, AzureCLI y Vagrant, es el momento de instalarlo.

El primer paso es instalar "Vagrant Azure Provider" con el siguiente comando:
 `vagrant plugin install vagrant-azure`

![Install Vagrant Azure Provider](http://i.cubeupload.com/VPBqoc.jpg)

- Nos conectamos a Azure con
```azure login```
![login](http://i.cubeupload.com/qMCJLH.jpg)


A continuación tenemos que editar en el archivo ansible_host, el nombre del host a "localhost" y la dirección IP (será la IP privada de la máquina de azure que se creará con Vagrant),  y lo llamaremos así desde el el playbook aprovisionamiento.yml.:

**ansible_hosts:**
```
[localhost]
192.168.10.175

```

Exportamos la variable de entorno de Ansible para que reconozca el host:

 `export ANSIBLE_HOSTS=~/ansible_hosts`


**aprovisionamiento.yml:**

```
- hosts: localhost
  sudo: yes
  remote_user: samu
  tasks:
  - name: Actualizar cache apt
    apt: update_cache=yes
  - name: Instalar python-setuptools
    apt: name=python-setuptools state=present
  - name: Instalar python-dev
    apt: name=python-dev state=present
  - name: Instalar build-essential
    apt: name=build-essential state=present
  - name: Instalar git
    apt: name=git state=present
  - name: Instalar pkg-config
    apt: name=pkg-config state=present
  - name: Instalar libtiff4-dev
    apt: name=libtiff4-dev state=present
  - name: Instalar libjpeg8-dev
    apt: name=libjpeg8-dev state=present
  - name: Instalar zlib1g-dev
    apt: name=zlib1g-dev state=present
  - name: Instalar PIP
    shell: sudo easy_install pip
  - name: Instalar Pillow
    shell: sudo -H pip install Pillow --upgrade
  - name: Clonando repositorio desde git
    git: repo=https://github.com/Samuc/Eat-with-Rango.git  dest=~/Eat-with-Rango clone=yes force=yes
  - name: Dar permisos a apliacación
    shell: sudo chmod +x ~/Eat-with-Rango
  - name: Instalar requisitos para la app
    shell: sudo pip install -r ~/Eat-with-Rango/requirements.txt
  - name: Ejecutar aplicacion
    shell: cd ~/Eat-with-Rango && sudo python manage.py runserver 0.0.0.0:80

```

En este fichero .yml, le indicamos las ordenes necesarias a ejecutar en la máquina de azure, y los paquetes a instalar necesarios para la app.
Después de ello, también se le indica que se descargue el repo de la app, instale los paquetes necesarios del mismo, y que ejecute la apliacción por el puerto 80.


Ahora, debemos generar los certificados de Azure, con los siguientes comandos:
```
openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout azurevagrant.key -out azurevagrant.key
chmod 600 azurevagrant.key
openssl x509 -inform pem -in azurevagrant.key -outform der -out azurevagrant.cer
```

El archivo azurevagrant.cer generado, deberemos subirlo al apartado "certificados del panel de configuración de Azure, [aquí](https://manage.windowsazure.com/). Uso la versión antigua del panel de Azure porque es más fácil, hay que ir a configuración->Certificados de Administración->Agregar, y ahí subimos nuestro certificado generado.


Ahora debemos generar el fichero .pem, para que vagrant lo pueda leer.
Ejecutamos los siguientes comandos:
```
openssl req -x509 -key ~/.ssh/id_rsa -nodes -days 365 -newkey rsa:2048 -out azurevagrant.pem

cat azurevagrant.key > azurevagrant.pem
```



A continuación crearemos el Vagrantfile crearemos la máquina de Azure y usaremos el archivo **aprovisionamiento.yml** que ya hemos creado,  para realizar el despliegue de nuestra App.

**Vagrantfile:**
```
# -*- mode: ruby -*-
# vi: set ft=ruby :

# Vagrantfile API/syntax version. Don't touch unless you know what you're doing!
VAGRANTFILE_API_VERSION = "2"

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
  # All Vagrant configuration is done here. The most common configuration
  # options are documented and commented below. For a complete reference,
  # please see the online documentation at vagrantup.com.
  config.vm.box = 'azure'
  config.vm.network "public_network"
  config.vm.network "private_network",ip: "192.168.10.175", virtualbox__intnet: "eth0"
  config.vm.network "forwarded_port", guest: 80, host: 80
  config.vm.define "localhost" do |l|
          l.vm.hostname = "localhost"
  end

  config.vm.provider :azure do |azure, override|
      azure.mgmt_certificate = File.expand_path('/home/samu/azurevagrant.pem')
      azure.mgmt_endpoint = 'https://management.core.windows.net'
      azure.subscription_id = 'd6c58002-4537-471f-ab27-888d8170aca4'
      azure.vm_image = 'b39f27a8b8c64d52b05eac6a62ebad85__Ubuntu-14_04_2-LTS-amd64-server-20150506-en-us-30GB'
      azure.vm_name = 'Rango2'
      azure.vm_password = 'Mi_contraseña1'
      azure.vm_location = 'Central US'
      azure.ssh_port = '22'
      azure.tcp_endpoints = '80:80'
  end

  config.vm.provision "ansible" do |ansible|
      ansible.sudo = true
        ansible.playbook = "aprovisionamiento.yml"
        ansible.verbose = "v"
        ansible.host_key_checking = false
  end

end
```
En la primera parte de éste fichero, el nombre de la máquina a usar es azure, la IP privada es la misma ip que la que es encuentra en el fichero ansible_hosts (que previamente hemos modificado). Y el nombre de la interfaz de red que estamos usando.

Luego tenemos que indicar donde se encuentra nuestro certicifado .pem, colocar nuestro ID de azure.
Éste ID lo podemos encontrar desde el panel de Azure, [aquí](https://manage.windowsazure.com/).

Tabmbién, indicamos la imagen a usar, en mi caso, un Ubuntu Server 14-02 amd64.

A continuación, en el siguiente bloque rellenamos con los de la máquina, como su nombre, contraseña, localización, puerto de ssh y endpoints.

Y por último, en el último bloque, añadimos el nombre de nuestro fichero de aprivisionamiento.


Una vez terminada toda la configuración procedemos a su uso, ejecutamos el siguiente comando:
```
vagrant box add azure https://github.com/msopentech/vagrant-azure/raw/master/dummy.box
```

En caso de que ya esté creado previamente, y queramos crearlo de nuevo desde 0, añadimos la opción --force:
```
vagrant box add azure https://github.com/msopentech/vagrant-azure/raw/master/dummy.box --force
```

Ahora, ya podemos proceder a levantar la  máquina, con:

 `sudo vagrant up --provider=azure`

Éste comando, creará la máquina virtual en Azure y posteriormente despliega la app.

Si ocurriese algún error en el aprovisionamiento, ahora debemos ejecutar otra orden, porque si intentamos la anterior de nuevo, nos dirá que la máquina ya está creada. Por lo que nos gustaría solo probar la parte del aprovisionamiento. Por lo tanto, ejecutaríamos el siguiente comando:
 `sudo vagrant provision`

![Ejecucion Vagrant up](http://i.imgbox.com/WU5EucG6.jpg)
![Ejecucion Vagrant up](http://i.imgbox.com/IWYVAeju.jpg)
![Ejecucion Vagrant up](http://i.imgbox.com/oFlY3Cm2.jpg)


Por último, entramos a la dirección de la máquina de azure en el navegador web. La dirección podemos verla también desde el panel de Azure.
Entramos en la dirección, y podremos ya usar nuestra aplicación:
![Captura de Eat-with-Rango desplegada con Vagrant en Azure](http://i.cubeupload.com/HPA0Fh.jpg)


Si queremos conectarnos a nuestra máquina por ssh, ejecutamos:
`vagrant ssh`
![Conexión SSH con "vagrant ssh"](http://i.imgbox.com/PAjUWhxA.jpg)


La url sobre la que está corriendo actualmente mi aplicación es: http://rango2-service-rknsl.cloudapp.net/rango/
La web estará activa temporalmente, hasta que la suscripción con Azure termine.
