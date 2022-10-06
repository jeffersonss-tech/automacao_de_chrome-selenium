import sys
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("user-data-dir=C:\\Users\\jeffe\\AppData\\Local\\Google\\Chrome\\User Data")
driver = webdriver.Chrome(chrome_options=options)
driver.get('https://conta.olx.com.br/pagamentos')
nome = 'Alex Pereira Maia'
cpf ='79511333100'

with open('lista.txt', 'r') as file:
    lines =  file.readlines()
    lines = [line.rstrip() for line in lines]

quantidade = len(lines)



ContadorDeLinha = 0
def preeencheDadosCc():
    global ContadorDeLinha
    global quantidade
    while ContadorDeLinha != quantidade:

        cc = lines[ContadorDeLinha]
        print('cc:', cc)
        bin = cc[0: 16]; print('bin: ', bin)
        mes = cc[17: 19]; print('mes: ', mes)
        ano = cc[22:24]; print('ano: ', ano)
        cvv = cc[25:28]; print('cvv: ', cvv)
        print('contagem:', ContadorDeLinha + 1)

        #preenche a bin
        cont = 0
        while True:
            try:
                driver.find_element(By.XPATH, '/html/body/div[3]/div/div/div[2]/div/div/div[1]/div/div[3]/div[3]/input').send_keys(bin)
                break
            except Exception as e:
                sleep(1)
                print(e)
                if cont == 3:
                    break
            cont += 1
        #mes e ano
        while True:
            try:
                driver.find_element(By.XPATH, '/html/body/div[3]/div/div/div[2]/div/div/div[2]/div[1]/div/div[3]/input').send_keys(mes, ano)
                break
            except Exception as e:
                sleep(1)
                print(e)

        while True:
            try:
                driver.find_element(By.XPATH, '/html/body/div[3]/div/div/div[2]/div/div/div[2]/div[2]/div/div[1]/div[3]/input').send_keys(cvv)
                break
            except Exception as e:
                sleep(1)
                print(e)

        while True:
            try:
                driver.find_element(By.XPATH, '/html/body/div[3]/div/div/div[2]/div/div/div[3]/div/div/div[3]/input').send_keys(nome)
                break
            except Exception as e:
                sleep(1)
                print(e)

        while True:
            try:
                driver.find_element(By.XPATH, '/html/body/div[3]/div/div/div[2]/div/div/div[4]/div/div/div[3]/input').send_keys(cpf)
                break
            except Exception as e:
                sleep(1)
                print(e)

        ContadorDeLinha = ContadorDeLinha + 1
        break



def salvaCartao():
    while True:
        try:
            driver.find_element(By.XPATH, '/html/body/div[3]/div/div/div[2]/div/div/div[6]/div/div/div[2]/button').click()
            break
        except Exception as e:
            print(e)

    while True:
        try:
            driver.find_element(By.XPATH, '/html/body/div[3]/div/div/div[2]/div/div/div[4]/div/div/div[2]/button').click()
            break
        except Exception as e:
            print(e)


def novoCartao():
    cont = 0
    while True:
        try:
            print('adicionando novo cartao')
            driver.find_element(By.XPATH, '//*[@id="__next"]/div/div[2]/div/div/div[5]/div[2]/div/div[2]/div/div/div/div[2]/div[3]/div/div/div/button').click()
            break
        except Exception as e:
            if cont == 2:
                break
            print(e)
        cont = cont + 1

def abrecampoCc():

    cont = 0
    while True:
        try:
            sleep(1)
            driver.find_element(By.XPATH, '//*[@id="__next"]/div/div[2]/div/div/div[5]/div[2]/div/div[2]/div/div/div/div[2]/div[3]/div/div/div/button').click()
            return
        except Exception as e:
            sleep(1)
            print(e)
            if cont == 4:
                break
        cont = cont + 1
    cont = 0
    while True:
        try:
            sleep(1)
            driver.find_element(By.XPATH, '//*[@id="__next"]/div/div[2]/div/div/div[4]/div[2]/div/div[2]/div/div/div/div[2]/div[3]/div/div/div/button').click()
            return
        except Exception as e:
            sleep(1)
            print(e)
            if cont == 4:
                break
        cont = cont + 1

    cont = 0
    while True:
        try:
            sleep(1)
            driver.find_element(By.XPATH,
                                '//*[@id="__next"]/div/div[2]/div/div/div[4]/div[2]/div/div/div/div[2]/div/div/a/span').click()
            return
        except Exception as e:
            sleep(1)
            print(e)
            if cont == 4:
                break
        cont = cont + 1

    cont = 0
    while True:
        try:
            sleep(1)
            driver.find_element(By.XPATH,
                                '//*[@id="__next"]/div/div[2]/div/div/div[5]/div[2]/div/div/div/div[2]/div/div/a/span').click()
            return
        except Exception as e:
            sleep(1)
            print(e)
            if cont == 4:
                break
        cont = cont + 1


def inicia():
    abrecampoCc()
    preeencheDadosCc()
    salvaCartao()

while True:
        inicia()
        if contador == quantidade:
            print('fim da lista..')