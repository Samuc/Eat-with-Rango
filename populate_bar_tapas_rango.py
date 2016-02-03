import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tango_with_django_project.settings')

import django
django.setup()

from rango.models import Bar, Tapa

def populate():
    Garden_bar = add_bar('Garden Bar')

    add_tapa(bar=Garden_bar,
        name="Carne en salsa")

    add_tapa(bar=Garden_bar,
        name="Huevos revueltos")

    add_tapa(bar=Garden_bar,
        name="Bocadillo  jamon")

    Reventaero_Bar = add_bar("Reventaero")

    add_tapa(bar=Reventaero_Bar,
        name="Patatas fritas con carne")

    add_tapa(bar=Reventaero_Bar,
        name="Hamburguesa")

    add_tapa(bar=Reventaero_Bar,
        name="Lomo al jerez")

    montaditos_bar = add_bar("100 Montaditos")

    add_tapa(bar=montaditos_bar,
        name="Filete lomo")

    add_tapa(bar=montaditos_bar,
        name="Montadito carne")

    # Print out what we have added to the user.
    for c in Bar.objects.all():
        for p in Tapa.objects.filter(bar=c):
            print "- {0} - {1}".format(str(c), str(p))

def add_tapa(bar, name, votos=0):
    t = Tapa.objects.get_or_create(bar=bar, nombre=name)[0]
    t.votos=votos
    t.save()
    return t

def add_bar(name):
    b = Bar.objects.get_or_create(nombre=name)[0]
    return b

# Start execution here!
if __name__ == '__main__':
    print "Starting Rango population script..."
    populate()
