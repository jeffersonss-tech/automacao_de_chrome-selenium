import sys
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("user-data-dir=C:\\Users\\jeffe\\AppData\\Local\\Google\\Chrome\\User Data")
driver = webdriver.Chrome(chrome_options=options)
driver.get('https://www.petlove.com.br/minha-conta/pagamento')
nome = 'jeferson da silva santos'
cpf ='90908457200'

with open('lista.txt', 'r') as file:
    lines =  file.readlines()
    lines = [line.rstrip() for line in lines]

quantidade = len(lines)

contador = 0
def preeencheDadosCc(mes, ano):
    global contador
    global quantidade
    while contador != quantidade:

        cc = lines[contador]
        print('cc:', cc)
        bin = cc[0: 16]; print('bin: ', bin)
        mes = cc[17: 19]; print('mes: ', mes)
        ano = cc[22:24]; print('ano: ', ano)
        cvv = cc[25:28]; print('cvv: ', cvv)
        print('contagem:', contador + 1)

        #preenche o campo do cartao
        while True:
            try:
                driver.find_element(By.ID, 'adyen-encrypted-form-number').send_keys(bin)
                break
            except Exception as e:
                sleep(1)
                print(e)

        while True:
            try:
                driver.find_element(By.ID, 'adyen-encrypted-form-holder-name').send_keys(nome)
                break
            except Exception as e:
                sleep(1)
                print(e)
        #mes do cc
        while True:
            try:
                driver.find_element(By.ID, 'adyen-encrypted-form-expiry-month').click()
                driver.find_element(By.XPATH, '//*[@id="adyen-encrypted-form-expiry-month"]/option[3]').click()
                break
            except Exception as e:
                sleep(1)
                print(e)
        contador = contador + 1

        while True:
            try:
                driver.find_element(By.ID, 'adyen-encrypted-form-expiry-year').click()
                driver.find_element(By.XPATH, '//*[@id="adyen-encrypted-form-expiry-year"]/option[4]').click()
                break
            except Exception as e:
                sleep(1)
                print(e)

        while True:
            try:
                driver.find_element(By.ID, 'adyen-encrypted-form-cvc').send_keys(cvv)
                break
            except Exception as e:
                sleep(1)
                print(e)
        break

def salvaCartao():
    while True:
        try:
            driver.find_element(By.ID, 'payment-button').click()
            break
        except Exception as e:
            print(e)

def novoCartao():
    while True:
        try:
            print('adicionando novo cartao')
            driver.find_element(By.CLASS_NAME, 'btn--full').click()
            break
        except Exception as e:

            print(e)

while True:
    try:
        novoCartao()
        preeencheDadosCc('02', '22')
        salvaCartao()
        if contador == quantidade:
            print('fim da lista..')
            #driver.close()
            sys.exit()
    except Exception as e:
        print(e)