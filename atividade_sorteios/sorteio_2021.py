from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

class Web_2021:
    def __init__(self):
        self.site = 'https://asloterias.com.br/resultados-da-mega-sena-2021'
        self.map = {
            'numero_do_jogo2021': {
                'xpath': '/html/body/main/div[2]/div/div/div[1]/strong[$terceiro$]'
            },
            'ano2021': {
                'xpath': '/html/body/main/div[2]/div/div/div[1]/span[%third%]'
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
            print(self.driver.find_element(By.XPATH, self.map['numero_do_jogo2021']['xpath'].replace('$terceiro$', f'{i}')).text, end='    ')
            for j in range(6):
                print(self.driver.find_element(By.XPATH, self.map['ano2021']['xpath'].replace('%third%', f'{k}')).text, end=' ')
                k += 1
            print('')