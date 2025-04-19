# RPA: Automação de Upload de Planilha de Preços

Este projeto é um RPA em Python que acessa o site (https://precos-de-produtos.netlify.app/) e Baixa uma Atualização da Planilha utilizando Selenium e PyAutoGUI.

## Funcionalidades

- Acessa automaticamente o site de produtos
- Espera os elementos carregarem antes de interagir
- Rola a página até o fim
- Clica no botão **"Carregar Mais"**
- Volta ao topo da página
- Clica no botão **"Subir Planilha de Preços"**
- Digita o caminho da planilha no pop-up do sistema usando [pyautogui]

## Tecnologias utilizadas

- [Python 3]
- [Selenium]
- [PyAutoGUI]
- [Geckodriver (para Firefox)]

##  Requisitos

- Python 3 instalado
- Geckodriver no PATH ou no mesmo diretório do script
- Firefox instalado
- Instalar dependências com:

## bash

pip install selenium 
pip install selenium pyautogui

## Recomendo que Cria um amabiente para insalar as Bibliotecas

- bash

python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
