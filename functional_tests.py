from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options

options = Options()
options.binary_location = "/snap/firefox/current/usr/lib/firefox/firefox"

service = Service(executable_path="/snap/bin/geckodriver")
browser = webdriver.Firefox(service=service, options=options)
browser.get("http://localhost:8000")

assert "Congratulations!" in browser.title
print("OK")