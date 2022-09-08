import  os
from selenium import webdriver
from selenium.webdriver.common.by import By

from time import sleep
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("user-data-dir=C:\\Users\\jeffe\\AppData\\Local\\Google\\Chrome\\User Data")
driver = webdriver.Chrome(chrome_options=options)
driver.get('https://shopee.com.br/user/account/payment')

email = 'marcosnetflixgratisfree@gmail.com'
password = '885416729xX'

def login():
    contador = 0
    while True:
        try:
            driver.find_element(By.CLASS_NAME, "_1a550J").click()

            os.system('cls')
            break
        except Exception as e:
            sleep(1)
            print(e)
            contador = contador + 1
            if contador == 4:
                break

login()
while True:
        try:
            if driver.find_element(By.CLASS_NAME, "my-account-section__header-button"):
                driver.find_element(By.CLASS_NAME, "my-account-section__header-button").click()
           # driver.find_element(By.ID, "pass").send_keys('@Jefferson(123)')
                break
        except Exception as e:
            print(e)
            sleep(2)

nome = 'jeferson da silva santos'
sobrenome = ''
cpf ='90908457200'
cep = '57360000'
rua = '13 de maio'
numero = '01'
validade = '02/2024'

with open('lista.txt', 'r') as file:
    lines =  file.readlines()
    lines = [line.rstrip() for line in lines]

quantidade = len(lines)

contador = 0
def preeencheDadosCc():
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
                driver.find_element(By.XPATH, '//*[@id="modal"]/div[2]/div[1]/div/div/div/div/div/div[3]/div[2]/div[2]/div[1]/div[1]/div/div/input').send_keys(bin)
                sleep(1)
                break
            except Exception as e:
                sleep(1)
                print(e)
        #preenche o campo cvv
        while True:
            try:
                sleep(0.5)
                driver.find_element(By.XPATH, '//*[@id="modal"]/div[2]/div[1]/div/div/div/div/div/div[3]/div[2]/div[2]/div[2]/div[1]/div/div[1]/div/div/input').send_keys(mes,'/', ano)

                break
            except Exception as e:
                sleep(1)
                print(e)
        while True:
            try:
                sleep(0.5)
                driver.find_element(By.XPATH, '//*[@id="modal"]/div[2]/div[1]/div/div/div/div/div/div[3]/div[2]/div[2]/div[2]/div[2]/div/div[1]/div/div[1]/input').send_keys(cvv)
                break
            except Exception as e:
                sleep(1)
                print(e)
        contador = contador + 1
        break

def preeencheDados():

    while True:
        try:
            sleep(0.5)
            driver.find_element(By.XPATH, '//*[@id="modal"]/div[2]/div[1]/div/div/div/div/div/div[3]/div[2]/div[2]/div[3]/div[1]/div/div/input').send_keys(nome)
            break
        except Exception as e:
            print(e)
            sleep(1)
    while True:
        try:
            sleep(0.5)
            driver.find_element(By.XPATH, '//*[@id="modal"]/div[2]/div[1]/div/div/div/div/div/div[3]/div[3]/div[2]/div[1]/div[1]/div/div/input').send_keys(cep)
            break
        except Exception as e:
            print(e)
            sleep(1)

    while True:
        try:
            sleep(0.5)
            driver.find_element(By.XPATH,'//*[@id="modal"]/div[2]/div[1]/div/div/div/div/div/div[3]/div[3]/div[2]/div[5]/div[1]/div/div/input').send_keys(numero)
            break
        except Exception as e:
            print(e)
            sleep(1)

    while True:
        try:
            sleep(0.5)
            driver.find_element(By.XPATH,'//*[@id="modal"]/div[2]/div[1]/div/div/div/div/div/div[3]/div[3]/div[2]/div[4]/div[1]/div/div/input').send_keys(rua)
            break
        except Exception as e:
            print(e)
            sleep(1)

    while True:
        try:
            sleep(0.5)
            driver.find_element(By.XPATH,'//*[@id="modal"]/div[2]/div[1]/div/div/div/div/div/div[3]/div[3]/div[2]/div[5]/div[1]/div/div/input').send_keys(numero)
            break
        except Exception as e:
            print(e)
            sleep(1)
    while True:
        try:
            sleep(0.5)
            driver.find_element(By.XPATH,'//*[@id="modal"]/div[2]/div[1]/div/div/div/div/div/div[3]/div[3]/div[2]/div[4]/div[1]/div/div/input').send_keys(rua)
            break
        except Exception as e:
            print(e)
            sleep(1)

preeencheDadosCc()
preeencheDados()

def enviar():
    while True:
        try:
            driver.find_element(By.XPATH,'//*[@id="modal"]/div[2]/div[1]/div/div/div/div/div/div[3]/div[4]/button[2]').click()
            break
        except Exception as e:
            print(e)
            sleep(1)
enviar()

while True:
    try:
        driver.find_element(By.XPATH,'//*[@id="modal"]/div[2]/div[1]/div/div[2]/span').click()
        driver.find_element(By.CLASS_NAME, "my-account-section__header-button").click()
        sleep(2)
        preeencheDadosCc()
        preeencheDados()
        enviar()
        os.system('cls')
    except Exception as e:
        print(e)
        sleep(1)
