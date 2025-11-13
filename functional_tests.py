from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options

# Estas son las librerías necesarias para configurar correctamente el webdriver de selenium para trabajar con firefox
# en Ubuntu. Necesitamos establecer explicitamente las rutas de firefox y el geckodriver, sino, no es posible hacer funcionar
# Estos parametros se pueden establecer en el método setUp() del fucntional test, ya sea heredando
# de LiveServerTestCase o StaticLiveServerTestCase etc.

options = Options()
options.binary_location = "/snap/firefox/current/usr/lib/firefox/firefox"

service = Service(executable_path="/snap/bin/geckodriver")
browser = webdriver.Firefox(service=service, options=options)
browser.get("http://localhost:8000")
