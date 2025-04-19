from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import pyautogui
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def inicio():

    try:
        self = webdriver.Firefox()
        self.get('https://precos-de-produtos.netlify.app/')
        sleep(3)
        
        WebDriverWait(self, 10).until(
            EC.visibility_of_element_located((By.XPATH,"//th[contains(text(), 'Nome do Produto')]"))
        )
        
        
        self.execute_script('window.scrollTo(0, document.body.scrollHeight);')
        sleep(3)

        button = WebDriverWait(self, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//button[contains(text(), "Carregar Mais")]'))
        )
        button.click()
        
        sleep(3)
        self.execute_script('window.scrollTo(0, document.body.scrollHeight);')
        
        #volta para Topo
        self.execute_script('window.scrollTo(0, 0);')
        sleep(3)

        button = WebDriverWait(self, 10).until(
            EC.visibility_of_element_located((By.XPATH,'//button[contains(normalize-space(text()), "Subir Planilha de Preços")]'))
        )
        button.click()

    except Exception as e:
        print(f"Erro na Navegação Antes de Baixar a Nova Planilha:{e}")
        self.quit()

    try:

        sleep(5)
        pyautogui.write(r'C:\Users\Leonardo Assis\Documents\projetos de Pyautogui\Planilha\precos-produtos-atualizados')
        pyautogui.press('enter')
        input('Aperta enter no terminal para Finalizar a tarefa')
        
    except Exception as e:
       print(f"Erro na Navegação:{e}")
       self.quit()    

inicio()        

    
   





