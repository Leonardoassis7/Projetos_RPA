import datetime
from typing import Dict, List
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoAlertPresentException, NoSuchElementException, ElementNotInteractableException
from selenium.webdriver.support.select import Select
from selenium import webdriver


class AutomacaoPadrao:
    def __init__(self, driver=None):
        # Se o driver não for passado, cria um novo
        self.driver = driver or webdriver.Firefox()

    def clica_elemento(self, **kwargs) -> Dict[str, any]:
        sleep(1)
        xpath_elemento = kwargs["xpath_elemento"]
        aparicao = kwargs.get("aparicao", 0)
        aguardar = kwargs.get("aguardar", 0)
        if self.aguarda_campo(xpath_elemento, aparicao):
            elemento = self.get_elemento(xpath_elemento)
            elemento.click()
            sleep(aguardar)
            return
        raise Exception(f"Não foi possível clicar no campo {xpath_elemento}")

    def preenche_campo(self, xpath_elemento: str = "", valor: str = "", tecla_por_tecla: bool = False, limpar_campo: bool = True) -> Dict[str, any]:
        sleep(1)
        if self.aguarda_campo(xpath_elemento):
            elemento = self.get_elemento(xpath_elemento)
            if limpar_campo:
                elemento.clear()
            if tecla_por_tecla:
                for i in valor:
                    sleep(0.5)
                    elemento.send_keys(i)
                return
            elemento.send_keys(valor)
            return
        raise Exception(f"Não foi possível preencher o campo {xpath_elemento}")

    def backspace(self, xpath_elemento: str = ""):
        sleep(1)
        if self.aguarda_campo(xpath_elemento):
            elemento = self.get_elemento(xpath_elemento)
            elemento.send_keys(Keys.BACKSPACE)

    def aguarda_campo(self, xpath_elemento: str, aparicao: int = 0) -> bool:
        cont = 0
        while not self.existe_elemento(xpath_elemento, aparicao) or self.loading_ativo():
            if cont > 15:
                return False
            cont += 1
            sleep(2)
        return True

    def existe_elemento(self, xpath_elemento: str, aparicao: int = 0) -> bool:
        try:
            self.get_elemento(xpath_elemento, aparicao)
            return True
        except NoSuchElementException:
            return False

    def tabkeys(self, xpath_elemento: str):
        sleep(1)
        if self.aguarda_campo(xpath_elemento):
            elemento = self.get_elemento(xpath_elemento)
            elemento.send_keys(Keys.TAB)

    def fechar_navegador(self):
        try:
            self.driver.quit()
        except Exception as e:
            print(f"Erro ao fechar navegador: {e}")

    def get_elemento(self, xpath_elemento: str, aparicao: int = 0) -> WebElement:
        """Método para obter o elemento pelo XPath"""
        return WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, xpath_elemento))
        )

    def loading_ativo(self) -> bool:
        """Método para verificar se o carregamento está ativo"""
        try:
            return bool(self.driver.find_element(By.XPATH, "//*[contains(@class, 'loading')]"))
        except NoSuchElementException:
            return False


# Exemplo de uso da classe
if __name__ == "__main__":
    automacao = AutomacaoPadrao()
    automacao.driver.get('https://example.com')
    automacao.clica_elemento(xpath_elemento='//*[@id="some_element"]')
    automacao.preenche_campo(xpath_elemento='//*[@id="input_field"]', valor="Teste")
    automacao.fechar_navegador()
