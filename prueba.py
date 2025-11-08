from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options

options = Options()
options.binary_location = "/snap/firefox/current/usr/lib/firefox/firefox"

service = Service(executable_path="/snap/bin/geckodriver")
driver = webdriver.Firefox(service=service, options=options)

#Esta es la única forma en ubuntu que podemos ejecutar el firefox con selenium, por el problema de
#que el gekodriver se encuentra en /snap/bin/gecodriver y el firefox en otro sitio.