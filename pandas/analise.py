import pandas as pd
from csv import writer
import openpyxl
import pyperclip
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from comando_padrao import AutomacaoPadrao
from selenium.webdriver.support.ui import Select

from time import sleep

class AnaliseDados(AutomacaoPadrao):
    def __init__(self):
        self.driver = webdriver.Firefox()

    def analise_dados(self):
        try:
            
            self.driver.get('https://cadastro-produtos-devaprender.netlify.app/index.html')

            sleep(2)
            planilha = pd.read_excel('produtos_ficticios.xlsx')
            print(planilha.head()) 

            #Para Percorre linha por linha 
            for index, linha in planilha.iterrows():

                WebDriverWait(self.driver,30).until(
                    EC.visibility_of_element_located((By.XPATH,'//h2[contains(text(),"Cadastro de Produto - Etapa 1: Informações Básicas")]'))

                )
            
                nome_produto = linha['Nome do produto']
                self.preenche_campo(xpath_elemento='//*[@id="product_name"]', valor=nome_produto)

                descricao = linha['Descrição']
                self.preenche_campo(xpath_elemento='//textarea[@id="description"]', valor=descricao)

                categoria = linha['Categoria']
                self.preenche_campo(xpath_elemento='//input[@id="category"]', valor=categoria)

                codigo_produto = linha['Código do produto']
                self.preenche_campo(xpath_elemento='//input[@id="product_code"]', valor=codigo_produto)

                peso = linha['Peso (em kg)']
                self.preenche_campo(xpath_elemento='//input[@id="weight"]', valor=peso)

                dimensoes = linha['Dimensões (L x A x P)']
                self.preenche_campo(xpath_elemento='//input[@id="dimensions"]', valor=dimensoes)


                #Botão Proximo
                self.clica_elemento(xpath_elemento='//button[contains(text(),"Próximo")]')
                

                WebDriverWait(self.driver, 30).until(
                    EC.visibility_of_element_located((By.XPATH, '//h2[contains(text(),"Cadastro de Produto - Etapa 2: Detalhes do Produto")]'))
                )

                preco = linha['Preço']
                self.preenche_campo(xpath_elemento='//input[@id="price"]', valor=preco)

                quantidade_estoque = linha['Quantidade em estoque']
                self.preenche_campo(xpath_elemento='//input[@id="stock"]', valor=quantidade_estoque)

                data_validade = linha['Data de validade']
                self.preenche_campo(xpath_elemento='//input[@id="expiry_date"]', valor=data_validade)

                cor = linha['Cor']
                self.preenche_campo(xpath_elemento='//input[@id="color"]', valor=cor)

                tamanho = linha['Tamanho'].strip().capitalize()
                select_element = self.driver.find_element(By.ID, "size")
                Select(select_element).select_by_value(tamanho)                
                
                material = linha['Material']
                self.preenche_campo(xpath_elemento='//*[@id="material"]', valor=material)

                #Botão Proximo
                self.clica_elemento(xpath_elemento='//button[contains(text(),"Próximo")]')

                WebDriverWait(self.driver, 30).until(
                    EC.visibility_of_element_located((By.XPATH, '//*[@id="manufacturer"]'))
                )

                fabricante = linha['Fabricante']
                self.preenche_campo(xpath_elemento='//*[@id="manufacturer"]', valor=fabricante)

                pais_origem = linha['País de origem']
                self.preenche_campo(xpath_elemento='//*[@id="country"]', valor=pais_origem)

                observacoes = linha['Observações']
                self.preenche_campo(xpath_elemento='//*[@id="remarks"]', valor=observacoes)

                codigo_de_barras = linha['Código de barras']
                self.preenche_campo(xpath_elemento='//*[@id="barcode"]', valor=codigo_de_barras)

                localizacao_no_armazem = linha['Localização no armazém']
                self.preenche_campo(xpath_elemento='//*[@id="warehouse_location"]', valor=localizacao_no_armazem)

                #Botão Proximo
                self.clica_elemento(xpath_elemento='//button[contains(text(),"Concluir")]')

                WebDriverWait(self.driver, 10).until(EC.alert_is_present())
                alert = self.driver.switch_to.alert
                alert.accept()

                WebDriverWait(self.driver, 30).until(
                    EC.presence_of_element_located((By.XPATH, '//h2[contains(text(),"Produto cadastrado com sucesso!")]'))
                )

                #Botão 
                self.clica_elemento(xpath_elemento='//button[contains(text(),"Adicionar Mais")]')

        except Exception as e:
            print("Ocorreu um Erro na navegação")
            self.fechar_navegador()
            
if __name__ == "__main__":
    analise = AnaliseDados()
    analise.analise_dados()


 
