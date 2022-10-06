import sys
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.chrome.options import Options
from time import sleep

options = Options()
options.add_argument("user-data-dir=C:\\Users\\jeffe\\AppData\\Local\\Google\\Chrome\\User Data")
driver = webdriver.Chrome(chrome_options=options)
driver.get('https://condutor.timob.com.br/')

nome = 'Alex Pereira Maia'
cpf ='79511333100'
dataNacimento = '25/09/1978'

with open('lista.txt', 'r') as file:
    lines =  file.readlines()
    lines = [line.rstrip() for line in lines]

quantidade = len(lines)

def login():
    while True:
        try:
            driver.find_element(By.NAME, 'doc').send_keys('219.366.518-40')
            driver.find_element(By.NAME, 'password').send_keys('885416729xX')
            driver.find_element(By.CLASS_NAME, 'btn-green').click()
            break
        except Exception as e:
            sleep(2)
            print(e)
resultado = ''
ContadorDeLinha = 0
def preeencheDadosCc():
    global  resultado
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

        while True:
            try:
                driver.find_element(By.NAME, 'number').send_keys(bin)
                break
            except Exception as e:
                print(e)

        while True:
            try:
                driver.find_element(By.NAME, 'name').send_keys(nome)
                break
            except Exception as e:
                print(e)

        while True:
            try:
                driver.find_element(By.NAME, 'cvc').send_keys(cvv)
                break
            except Exception as e:
                print(e)

        while True:
            try:
                driver.find_element(By.NAME, 'expirationDate').send_keys(mes, ano)
                break
            except Exception as e:
                print(e)
        while True:
            try:
                driver.find_element(By.NAME, 'cpf').send_keys(cpf)
                break
            except Exception as e:
                print(e)

        while True:
            try:
                driver.find_element(By.NAME, 'birthDate').send_keys(dataNacimento)
                break
            except Exception as e:
                print(e)

        while True:
            try:
                driver.find_element(By.XPATH, '//*[@id="root"]/main/div/div[1]/div/div[2]/div/div/div/form/button').click()
                driver.find_element(By.XPATH,
                                    '//*[@id="root"]/main/div/div[1]/div/div[2]/div/div/div/div/div/div/button[1]').click()
                break
            except Exception as e:
                print(e)

        while True:
            try:
                resultado = (driver.find_element(By.XPATH, '//*[@id="root"]/main/div/div[1]/div/div/div[2]/div/div/div/div/div[1]/div[2]/p[2]').text)
                break

            except Exception as e:
                sleep(10)
                driver.refresh()
                print(e)



        ContadorDeLinha = ContadorDeLinha + 1
        break


def abrirCampo():
    while True:
        try:
            driver.find_element(By.XPATH, '//*[@id="root"]/main/div/div[1]/div/div/div[4]/div/div[2]/div[2]/div[1]').click()
            driver.find_element(By.XPATH,
                                '//*[@id="root"]/main/div/div[1]/div/div[2]/div/form/div/div/label').click()
            break
        except Exception as e:
            print('')

    cont = 0
    while True:
        try:
            driver.find_element(By.XPATH, '//*[@id="root"]/main/div/div[1]/div/div/div[4]/div/div[2]/div[2]/div[1]').click()
            driver.find_element(By.XPATH,
                                '//*[@id="root"]/main/div/div[1]/div/div[2]/div/form/div/div/label').click()
            driver.find_element(By.XPATH,
                                '//*[@id="root"]/main/div/div[1]/div/div[2]/div/form/button[2]').click()
            break
        except Exception as e:
            print('')
            if cont == 5:
                break
            cont = cont + 1

    while True:
        try:
            driver.find_element(By.XPATH, '//*[@id="root"]/main/div/div[1]/div/div[2]/div/form/button[2]').click()
            break
        except Exception as e:
            print(e)
            if cont == 5:
                break
            cont = cont + 1

    preeencheDadosCc()






login()

while True:
    abrirCampo()
    if ContadorDeLinha ==  quantidade:
        break

