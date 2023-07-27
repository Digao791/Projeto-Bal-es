import requests
from bs4 import BeautifulSoup
import threading
import time
import baloes


url = baloes.site
response = requests.get(url)
html_content = response.text
soup = BeautifulSoup(html_content, 'html.parser')
tr = soup.find_all('td', class_="c-contestant")

baloes = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K"] #LISTA DOS BALÕES

baloes_pendentes = {} #DICIONARIO DOS BALOES PENDENTES
Baloes_adquiridos = {} #DICIONARIO DOS BALOES ADQUIRIDOS
Total_de_competidores = 0 #VARIÁVEL RESPONSAVEL POR GUARDAR A QUANTIDADE DE ALUNOS
Nome_dos_alunos = []
Quantidade_de_exercicios = len(baloes)

def check_board():
        print('checando...')
        tr = soup.find_all('tr')
        for i in tr:
            name = i.find('td', class_="c-contestant")
            if name is not None:
                r = [linha.strip() for linha in name.text.splitlines() if linha.strip()]
                if len(r) > 0:
                    print(r[0])
                    exercicios = i.find_all('td',  class_="c-box")
                    for exercicio in exercicios:
                        for letra in exercicio.find_all('p'):
                            if letra.get("class") is not None:
                                if len(letra['class']) > 1:
                                    print(letra['class'][1][-1].upper())
                                    if (not(Baloes_adquiridos[r[0]][letra['class'][1][-1].upper()])):
                                        baloes_pendentes[r[0]][letra['class'][1][-1].upper()] = True
                                       
                            
       
for i in tr:
    r = [linha.strip() for linha in i.text.splitlines() if linha.strip()]
    if len(r) > 0:
         Nome_dos_alunos.append(r[0])
         Total_de_competidores = Total_de_competidores + 1
         for j in range (0, len(baloes)):
            baloes_pendentes[str(r[0])] = {str(balao): False for balao in baloes}
            Baloes_adquiridos[str(r[0])] ={str(balao): False for balao in baloes}

def check_board_periodically():
    while not(parar):
        check_board()
        time.sleep(5)  # Pausa por 5 segundos antes de chamar a próxima iteração

# Criar a Thread para a função check_board_periodically
thread = threading.Thread(target=check_board_periodically)

# Iniciar a Thread
parar = False
thread.start()




            
    



    




