import sys
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("user-data-dir=C:\\Users\\jeffe\\AppData\\Local\\Google\\Chrome\\User Data")
driver = webdriver.Chrome(options=options)
driver.get('https://store.avast.com/store/avastbr/pt_BR/buy/productID.5131300100/ThemeID.38737300/Currency.BRL/campaignMarker.WDS~pt-br~lp-ppc-secureline-vpn-buy~~~012_a6i/CustomID.VSOFF/clearCart.1?trackingDisabled=C0001%3A1%2CC0003%3A1%2CC0002%3A1%2CC0004%3A1%2CC0005%3A1%2CBG239%3A1&_ga=2.46154145.742075024.1662732494-1556766116.1661482574&_gac=1.184416084.1662733134.Cj0KCQjwyOuYBhCGARIsAIdGQROzAIEeiz5LIKjGb1diedo5rPdWlHxiAQFHreeTDJdwtlcrHg4m0_UaAivwEALw_wcB')
driver.delete_all_cookies()
nome = 'Alex'
sobrenome = 'Pereira Maia'
cpf ='79511333100'
cep = '57360000'
endereco = 'rua do sol'
bairro = 'centro'
cidade = 'girau do ponciano'
email = 'joelmarcvl@gmail.com'

with open('lista.txt', 'r') as file:
    lines =  file.readlines()
    lines = [line.rstrip() for line in lines]

quantidade = len(lines)




contador = 0
def preeencheDadosCc():
    print('iniciando preeenchimento')
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

        #preenche a bin
        cont = 0
        while True:
            try:
                driver.find_element(By.NAME, 'cardNumber').send_keys(bin)
                break
            except Exception as e:
                sleep(1)
                print(e)
                if cont == 3:
                    print('recarregando pagina')
                    driver.refresh()
            cont += 1
        #mes
        while True:
            try:
                driver.find_element(By.NAME, 'cardExpirationMonth').click()
                sleep(0.2)
                driver.find_element(By.XPATH, '//*[@id="ccMonth"]/option[3]').click()
                break
            except Exception as e:
                sleep(1)
                print(e)
        #ano
        while True:
            try:
                driver.find_element(By.NAME, 'cardExpirationYear').click()
                sleep(0.2)
                driver.find_element(By.XPATH, '//*[@id="ccYear"]/option[4]').click()
                break
            except Exception as e:
                sleep(1)
                print(e)

        while True:
            try:
                driver.find_element(By.NAME, 'cardSecurityCode').send_keys(cvv)
                break
            except Exception as e:
                sleep(1)
                print(e)

        while True:
            try:
                driver.find_element(By.NAME, 'BILLINGname1').send_keys(nome)
                sleep(0.1)
                driver.find_element(By.NAME, 'BILLINGname2').send_keys(sobrenome)
                sleep(0.1)
                driver.find_element(By.NAME, 'BILLINGpostalCode').send_keys(cep)
                sleep(0.2)
                driver.find_element(By.NAME, 'siteLevelBoletoBairro').send_keys(bairro)
                sleep(0.1)
                driver.find_element(By.NAME, 'EMAILemail').send_keys(email)
                sleep(0.1)
                driver.find_element(By.NAME, 'taxRegistrationNumber').send_keys(cpf)

                break
            except Exception as e:
                sleep(1)
                print(e)

        while True:
            try:
                sleep(0.9)
                driver.find_element(By.NAME, 'BILLINGline1').send_keys(endereco)
                break
            except Exception as e:
                sleep(1)
                print(e)
        break



def salvaCartao():
    while True:
        try:
            driver.find_element(By.ID, 'av_js-paymentContinueButton').click()
            break
        except Exception as e:
            print(e)

preeencheDadosCc()
salvaCartao()
'''def novoCartao():
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
            print('fim da lista..')'''