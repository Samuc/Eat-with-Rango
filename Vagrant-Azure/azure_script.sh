#!/bin/bash

git clone https://github.com/Samuc/Eat-with-Rango.git
cd Eat-with-Rango/Vagrant-Azure/
chmod 777 *
vagrant box add azure https://github.com/msopentech/vagrant-azure/raw/master/dummy.box
vagrant up --provider=azure
vagrant provision
