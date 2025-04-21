# Automação de Cadastro de Produtos no Navegador

Este projeto tem como objetivo automatizar o preenchimento de um formulário web com dados de produtos retirados de uma planilha Excel.


## Site
- [https://cadastro-produtos-devaprender.netlify.app/]


## Explicação

Funcionamento da leitura o Excel: O que eu faço. Pego as informações do Excel e atribuo ela a uma variavel (nome_produto = linha[0].value) desse jeito, com as variaveis consigo preencher os campos no navegador.

### Observação :
A planilha tem **caracteres especiais**. O copia e cola do pyautogui não funciona. Para isso uso ( pyperclip ) para pegar as informações da variavel e preenchê-las no site !!


## Ferramentas Utilizadas

- **pyautogui**: Usado para clicar e colar informações no navegador
- **selenium**: Utilizado para aguardar mudanças de tela (com `WebDriverWait`)
- **openpyxl**: Lê os dados do arquivo Excel `.xlsx`
- **pyperclip**: Resolve o problema de copiar/colar com caracteres especiais
- **mouseinfo**:
1) python -m pip install mouseinfo "Exibe as coordenadas X e Y do Cursor do mouse" 
    - python
    - from mouseinfo import mouseInfo
    - mouseInfo()  " No app Desmarca Delay de 3 Segundos, canto superior Esquerto "

## Observação sobre o Excel
- Use uma extensão como **Excel Viewer** no VS Code para visualizar a planilha direto no editor
