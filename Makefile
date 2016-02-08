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
