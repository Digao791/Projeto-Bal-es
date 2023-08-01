from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time
import requests
from bs4 import BeautifulSoup

def login(url):


    # Configuração do WebDriver do Chrome
    chrome_options = webdriver.ChromeOptions()
    chrome_options.binary_location = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe" 
    chrome_options.add_argument('--disable-extensions')
    driver = webdriver.Chrome(options=chrome_options)
    
    response = requests.get(url)
    html_content = response.text
    soup = BeautifulSoup(html_content, 'html.parser')
    tr = soup.find_all('div', class_="score-card")

    # Acessar a página de cadastro"C:\Users\Cliente\Desktop\projeto_baloes\chrome-win64\chrome-win64\chrome.exe"
    driver.get(url)
    wait = WebDriverWait(driver, 1000)
    time.sleep(20)
    wait = WebDriverWait(driver, 100)
    nomes = driver.find_elements(By.CLASS_NAME, "user-name")

    # Obter o texto de cada div
    nomes = [element for element in nomes]
    for i in nomes:
        print(i.text)
        
    questoes = driver.find_elements(By.CLASS_NAME, "score-card")

    # Obter o texto de cada div
    questoes = [element for element in questoes]
    
    for i in questoes:
        print(i.text)

if __name__ == "__main__":

    site = "https://neps.academy/br/competition/1646"

    # Chamando a função para preencher o formulário de cadastro
    login(site)
   
    