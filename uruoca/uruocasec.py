from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

nav = webdriver.Chrome()
arq = "infosec.txt"


def salvardados(arq, dados):
    lista = dados[:]
    try:
        with open(arq, 'w', encoding='utf-8') as arquivo:
            for dado in lista:
                arquivo.write('\n')
                arquivo.write(dado)
                arquivo.write('\n')
                arquivo.write('')
    except:
        print("erro ao inserir dados")


setores = '/html/body/nav[2]/div/div/ul/li[3]/a'
primeiro_item = '/html/body/nav[2]/div/div/ul/li[3]/ul/li[1]/a'


link = "https://www.uruoca.ce.gov.br/"
nav.get(link)
nav.maximize_window()
sleep(4)
dados = list()
botao = nav.find_element(By.XPATH, f'{setores}')
botao.click()
for c in range(1, 2):
    try:

        nav.find_element(By.XPATH, f'/html/body/nav[2]/div/div/ul/li[3]/ul/li[{c}]/a').click()
        sleep(2)
        foto = nav.find_element(By.XPATH, '/html/body/div/div/div[1]/div[2]/div/img')
        foto.screenshot_as_png



    except:
        print(f'Erro na linha {c}')


#salvardados(arq, dados)
