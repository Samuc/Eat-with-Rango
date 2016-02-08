install:
	sudo apt-get update
	sudo apt-get install python-setuptools
	sudo apt-get install python-dev
	sudo apt-get install build-essential
	sudo apt-get install git
	sudo apt-get install pkg-config
	sudo apt-get install libtiff4-dev
	sudo apt-get install libjpeg8-dev
	sudo apt-get install zlib1g-dev
	sudo easy_install pip
	sudo -H pip install Pillow --upgrade
	sudo pip install django --upgrade
	sudo pip install -r requirements.txt

test:
	python manage.py test

run:
	sudo python manage.py runserver 0.0.0.0:80

crearAzure:
	cd Vagrant-Azure
	vagrant box add azure https://github.com/msopentech/vagrant-azure/raw/master/dummy.box
	vagrant up --provider=azure
	vagrant provision
	sudo vagrant up --provider=azure

provisionAzure:
	cd Vagrant-Azure  && vagrant provision

azure:
	sudo vagrant provision
	fab -H samu@rango2-service-rknsl.cloudapp.net runApp
