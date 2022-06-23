from selenium import webdriver
from selenium.webdriver.edge.options import Options

#Nastavení Driveru
options = Options()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--ignore-sll-errors')
options.add_argument('log-level=3') #Ignorovat výpis erorů

#DISABLE: Edge is being controlled by automated test software
options.add_argument("--disable-infobars")
options.add_experimental_option("useAutomationExtension", False)
options.add_experimental_option("excludeSwitches", ["enable-automation"])

#options.add_argument('headless') #Bez Hlavičky
#options.add_argument('--blink-settings=imagesEnabled=false') #Bez Obrázků
#options.add_argument("--no-first-run") 
#options.add_argument("--disable-default-apps") 
options.add_argument("--disable-extensions")

#options.add_argument("--disable-javascript") #Vypnout JS 2
#options.add_experimental_option( "prefs",{'profile.managed_default_content_settings.javascript': 2}) #Vypnout JS 1

options.add_argument("InPrivate") 

driver = webdriver.Edge(options = options)

driver.get('https://www.mojeip.cz/test')
