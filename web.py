from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from banco import inserir_jogos


class Web:
    def __init__(self):
        self.site = 'https://asloterias.com.br/resultados-da-mega-sena-xxxx'
        self.map = {
            'sorteio': {
                'xpath': '/html/body/main/div[2]/div/div/div[1]/strong[&&]'
            },
            'numero': {
                'xpath': '/html/body/main/div[2]/div/div/div[1]/span[$$]'
            }
        }
        self.driver = webdriver.Chrome()
        for i in range(1996, 2023):
            self.ano = i
            self.cont = 0
            site_ano = self.site.replace('xxxx', f"{i}") #define o ano
            self.driver.get(site_ano) #abrir o site
            self.abrir()
            sleep(2)

    def abrir(self):
        n = []
        cont = 0
        for i in range(4, 160):
            try:
                id = self.driver.find_element(By.XPATH, self.map['sorteio']['xpath'].replace('&&', f"{i}")).text
                print()
                print(id, end=": ")
                for j in range(6):
                    cont = cont + 1
                    x = self.driver.find_element(By.XPATH, self.map['numero']['xpath'].replace('$$', f"{cont}")).text
                    n.append(x[:])
                    if x == "Mega da Virada":
                        cont = cont + 1
                        x = self.driver.find_element(By.XPATH, self.map['numero']['xpath'].replace('$$', f"{cont}")).text
                        n.append(x[:])
                    print(n[cont-1], end=" ")
                inserir_jogos(self.ano, n[cont-6], n[cont-5], n[cont-4], n[cont-3], n[cont-2], n[cont-1])
                print()
            except:
                break
        n.clear()


if __name__ == "__main__":
    w = Web()
