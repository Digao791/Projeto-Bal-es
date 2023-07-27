from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time

def dados_basicos(url, nome, sobrenome, usuario):


    # Configuração do WebDriver do Chrome
    chrome_options = webdriver.ChromeOptions()
    chrome_options.binary_location = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe" 
    chrome_options.add_argument('--disable-extensions')
    driver = webdriver.Chrome(options=chrome_options)

    # Acessar a página de cadastro"C:\Users\Cliente\Desktop\projeto_baloes\chrome-win64\chrome-win64\chrome.exe"
    driver.get(url)
    driver.find_element(By.ID, "email").send_keys("rodrigofragacosta791@Outlook.com")
    driver.find_element(By.ID, "password").send_keys("OnePiece791!")
    entrar =  driver.find_element(By.CLASS_NAME, "submit")
    entrar.click()

    wait = WebDriverWait(driver, 10)
    wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "pn-dashboard")))

    url = "https://www.beecrowd.com.br/judge/pt/users/basic-info"
    driver.get(url)

    wait = WebDriverWait(driver, 10)
    wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "pn-basicinfo")))

    wait = WebDriverWait(driver, 100)
    time.sleep(1)
    
    #close_tour = driver.find_element(By.CLASS_NAME, "trip-close") # APAGUE ESSA LINHA SE NAO APARECER MENSAGEM DE AVISO
    #close_tour.click()#APAGUE ESSA LINHA SE NAO APARECER MENSAGEM DE AVISO

    wait = WebDriverWait(driver, 100)
    time.sleep(1)
    
    # Preencher o formulário com os dados desejados
    driver.find_element(By.ID, "first-name").clear()
    wait = WebDriverWait(driver, 100)
    driver.find_element(By.ID, "first-name").send_keys(nome)
    driver.find_element(By.ID, "last-name").clear()
    wait = WebDriverWait(driver, 100)
    driver.find_element(By.ID, "last-name").send_keys(sobrenome)
    driver.find_element(By.ID, "username").clear()
    wait = WebDriverWait(driver, 100)
    driver.find_element(By.ID, "username").send_keys(usuario)
    time.sleep(1)
    
    driver.find_element(By.ID, "timezone-selectized").send_keys("UTC/GMT -03:00 America/Sao Paulo")
    driver.find_element(By.ID, "timezone-selectized").send_keys(Keys.ENTER)
    wait = WebDriverWait(driver, 10)

    #data = driver.find_element(By.NAME, 'birthday')
    driver.find_element(By.NAME, "birthday").send_keys("20/05/2004")
    #driver.execute_script("arguments[0].click();", data)

    wait = WebDriverWait(driver, 100)
    label_procurado = 'Julho 1, 2015'  # Substitua 'Nome do Elemento' pelo valor do aria-label desejado
    xpath_query = f"//span[@aria-label='{label_procurado}']"

    elemento = WebDriverWait(driver, 100).until(EC.presence_of_element_located((By.XPATH, xpath_query)))
    driver.execute_script("arguments[0].scrollIntoView();", driver.find_element(By.ID, 'short-bio'))
    wait = WebDriverWait(driver, 100)
    time.sleep(1)

# Faça ações com o elemento encontrado, por exemplo, clicar nele
    elemento.click()

    driver.find_element(By.ID, 'genders-selectized').click()
    wait = WebDriverWait(driver, 100)
    driver.find_element(By.ID, 'genders-selectized').send_keys("Prefiro não dizer")
    driver.find_element(By.ID, 'genders-selectized').send_keys(Keys.ENTER)

    wait = WebDriverWait(driver, 100)
    
   
    check = driver.find_element(By.ID, 'objective-id-1')
    driver.execute_script("arguments[0].scrollIntoView();", driver.find_element(By.ID, 'genders-selectized'))
    wait = WebDriverWait(driver, 100)
    time.sleep(1)
    check.click()

    check = driver.find_element(By.ID, 'track-id-1')
    wait = WebDriverWait(driver, 100)
    time.sleep(1)
    check.click()

    check = driver.find_element(By.ID, 'student-or-professional-is_student')
    wait = WebDriverWait(driver, 100)
    time.sleep(1)
    check.click()

    driver.execute_script("arguments[0].scrollIntoView();", driver.find_element(By.ID, 'chkbx-recruiting'))
    wait = WebDriverWait(driver, 100)
    time.sleep(1)

    driver.find_element(By.ID, 'save-button').click()

    wait = WebDriverWait(driver, 100)
    wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "pn-basicinfo")))

    time.sleep(5)

    preferencias(driver)
    
def preferencias(driver):


    url = "https://www.beecrowd.com.br/judge/pt/users/preferences"
    driver.get(url)
    wait = WebDriverWait(driver, 100)
    wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "pn-preferences")))

    time.sleep(2)

    driver.find_element(By.ID, "language-selectized").click()
    wait = WebDriverWait(driver, 100)
    driver.find_element(By.ID, "language-selectized").send_keys("Python 3.9")
    driver.find_element(By.ID, "language-selectized").send_keys(Keys.ENTER)

    driver.find_element(By.CLASS_NAME, 'send-purple').click()

    wait = WebDriverWait(driver, 100)
    wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "pn-preferences")))

    time.sleep(5)


if __name__ == "__main__":

    site = "https://www.beecrowd.com.br/judge/pt/login"

    # Dados de exemplo
    nome = "Competidor"
    sobrenome = "Inatel"
    usuario = "CompetidorX321"

    # Chamando a função para preencher o formulário de cadastro
    dados_basicos(site, nome, sobrenome, usuario)
   
    
