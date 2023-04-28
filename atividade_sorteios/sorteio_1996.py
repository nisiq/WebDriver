from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

class Web_1996:
    def __init__(self):
        self.site = 'https://asloterias.com.br/resultados-da-mega-sena-1996?ordenacao=crescente'
        self.map = {
            'numero_do_jogo': {
                'xpath': '/html/body/main/div[2]/div/div/div[1]/strong[$primeiro$]'
            },
            'primeiro_numero': {
                'xpath': '/html/body/main/div[2]/div/div/div[1]/span[%first%]'
            }
        }
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.abrir()

    def abrir(self):
        self.driver.get(self.site)
        sleep(5)
        k = 1
        for i in range(4, 114):
            print(self.driver.find_element(By.XPATH, self.map['numero_do_jogo']['xpath'].replace('$primeiro$', f'{i}')).text, end='    ')
            for j in range(6):
                print(self.driver.find_element(By.XPATH, self.map['primeiro_numero']['xpath'].replace('%first%', f'{k}')).text, end=' ')
                k += 1
            print('')