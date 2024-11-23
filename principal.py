from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Configura las opciones para Brave
brave_path = "C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe"
chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = brave_path

# Instala automáticamente la versión correcta del driver
service = Service(ChromeDriverManager().install())

# Inicia el navegador Brave
driver = webdriver.Chrome(service=service, options=chrome_options)

# Abre una página web
driver.get("https://www.google.com")
print("Título de la página:", driver.title)

# Cierra el navegador
driver.quit()
