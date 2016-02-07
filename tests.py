from django.test import TestCase
from rango.models import Tapa, Bar, UserProfile
from django.test import Client


class SiteTestCase(TestCase):
	# Test acceso sitio principal
	def test_index(self):
		response = self.client.get('/rango/')
		self.assertEqual(response.status_code, 200)

	# Testea acceso a about
	def test_about(self):
		response = self.client.get('/rango/about/')
		self.assertEqual(response.status_code, 200)

	# Test acceso a login
	def test_login(self):
		response = self.client.get('/rango/login/')
		self.assertEqual(response.status_code, 200)


    # Test acceso a highchart
	def test_highchart(self):
		response = self.client.get('/rango/highchart/')
		self.assertEqual(response.status_code, 200)

	# Test acceso a register
	def test_login(self):
		response = self.client.get('/rango/register/')
		self.assertEqual(response.status_code, 200)


class BarTestCase(TestCase):
	# Test para crear un bar
	def setUp(self):
		Bar.objects.create(nombre = "Bar Test", direccion = "Calle Periodista Daniel Saucedo Aranda, Granada" )

	# Testear tupla nombre-lema
	def test_Bar_direccion(self):
		bar = Bar.objects.get(nombre = "Bar Test")
		self.assertEqual(bar.direccion, "Calle Periodista Daniel Saucedo Aranda, Granada")



class BarAccessTestCase(TestCase):
    # Test para crear un bar y accedera a la pagina del mismo
	def setUp(self):
		Bar.objects.create(nombre = "Bar Test", direccion = "Calle Periodista Daniel Saucedo Aranda, Granada" )

	# Testear tupla nombre-lema
	def test_Bar_access(self):
		response = self.client.get('/rango/bar/Bar_Test/')
		self.assertEqual(response.status_code, 200)


class TapaTestCase(TestCase):
	# Test para crear un bar
    def setUp(self):
		Bar.objects.create(nombre = "Bar Test", direccion = "Calle Periodista Daniel Saucedo Aranda, Granada" )
		bar_test = Bar.objects.get(nombre = "Bar Test")


         	tapa = Tapa.objects.create(nombre = "Carne en salsa", bar= bar_test)


    # Testear tupla
    def test_Tapa_bar(self):
        tapa = Tapa.objects.get(nombre = "Carne en salsa")
        bar = Bar.objects.get(nombre = "Bar Test")

        self.assertEqual(tapa.bar, bar)
