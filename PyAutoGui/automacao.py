from csv import writer
import pyautogui
import openpyxl
import pyperclip
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def automacao():
    try:
        self = webdriver.Firefox()
        self.get('https://cadastro-produtos-devaprender.netlify.app/index.html')
        
        #Abre a Planilha
        planilha_excel = openpyxl.load_workbook('produtos_ficticios.xlsx')
        excel_pagina = planilha_excel['Produtos']

        contador = 0 

        for linha in excel_pagina.iter_rows(min_row=2):
            nome_produto = linha[0].value
            pyperclip.copy(nome_produto)
            pyautogui.click(196,183, duration=1)
            pyautogui.hotkey('ctrl', 'v')

            descricao = linha[1].value
            pyperclip.copy(descricao)
            pyautogui.click(208,277,duration=1)
            pyautogui.hotkey('ctrl', 'v')

            categoria = linha[2].value
            pyperclip.copy(categoria)
            pyautogui.click(217,407,duration=1)
            pyautogui.hotkey('ctrl', 'v')

            codigo_produto = linha[3].value
            pyperclip.copy(codigo_produto)
            pyautogui.click(244, 491,duration=1)
            pyautogui.hotkey('ctrl', 'v')

            peso = linha[4].value
            pyperclip.copy(peso)
            pyautogui.click(214,583,duration=1)
            pyautogui.hotkey('ctrl', 'v')

            dimensoes = linha[5].value
            pyperclip.copy(dimensoes)
            pyautogui.click(195,659,duration=1)
            pyautogui.hotkey('ctrl', 'v')
            
            #Botao Proximo
            pyautogui.click(151,718,duration=1)

            WebDriverWait(self,10).until(
                EC.visibility_of_element_located((By.XPATH, '//label[contains(text(),"Data de validade:")]'))
            )

            preco = linha[6].value
            pyperclip.copy(preco)
            pyautogui.click(386,205,duration=1)
            pyautogui.hotkey('ctrl', 'v')

            quantidade_estoque = linha[7].value
            pyperclip.copy(quantidade_estoque)
            pyautogui.click(173,293,duration=1)
            pyautogui.hotkey('ctrl', 'v') 

            data_validade = linha[8].value
            pyperclip.copy(data_validade)
            pyautogui.click(172,379,duration=1)
            pyautogui.hotkey('ctrl', 'v')

            cor = linha[9].value
            pyperclip.copy(cor)
            pyautogui.click(192,465,duration=1)
            pyautogui.hotkey('ctrl', 'v')

            tamanho = linha[10].value
            pyperclip.copy(tamanho)
            pyautogui.click(559,549,duration=1)
            if tamanho == ('Pequeno'):
                pyautogui.click(187,584,duration=1)
            elif tamanho == ('Médio'):
                pyautogui.click(133,606,duration=1)
            else:
                pyautogui.click(161,636,duration=1)
                        
            material = linha[11].value
            pyperclip.copy(material)
            pyautogui.click(188,635,duration=1)
            pyautogui.hotkey('ctrl', 'v')

            #Botao Proximo
            pyautogui.click(151,718,duration=1)

            WebDriverWait(self,10).until(
                EC.visibility_of_element_located((By.XPATH, '//label[contains(text(),"País de origem:")]'))
            )

            fabricante = linha[12].value
            pyperclip.copy(fabricante)
            pyautogui.click(361,228,duration=1)
            pyautogui.hotkey('ctrl', 'v')

            pais_origem	= linha[13].value
            pyperclip.copy(pais_origem)
            pyautogui.click(176,317,duration=1)
            pyautogui.hotkey('ctrl', 'v')
            
            observacoes	= linha[14].value
            pyperclip.copy(observacoes)
            pyautogui.click(187,425,duration=1)
            pyautogui.hotkey('ctrl', 'v')

            Codigo_de_barras = linha[15].value
            pyperclip.copy(Codigo_de_barras)
            pyautogui.click(177,535,duration=1)
            pyautogui.hotkey('ctrl', 'v')

            localizacao_no_armazem =linha[16].value
            pyperclip.copy(localizacao_no_armazem)
            pyautogui.click(219,625,duration=1)
            pyautogui.hotkey('ctrl', 'v')

            #Botao Concluir
            pyautogui.click(160,674,duration=1)

            #Espera o alert aparecer na Tela
            wait = WebDriverWait(self, 10)
            wait.until(EC.alert_is_present()),

            #Botao Ok alert
            pyautogui.click(814,441,duration=1)

            WebDriverWait(self,10).until(
                EC.visibility_of_element_located((By.XPATH, '//h2[contains(text(),"Produto cadastrado com sucesso!")]'))
            )

            #Botao Adicionar Mais um 
            pyautogui.click(687,460,duration=1)
            contador += 1
        
        print(f"Cadastro finalizado com sucesso! Total de produtos cadastrados: {contador}")
    except Exception as e:
        print(f'Ocorreu um Erro na Navegação, {e}')
        self.quit()

automacao()        
