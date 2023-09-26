# Passo a passo
# Passo 1: Entrar mo sistema da empresa
    # https://dlp.hashtagtreinamentos.com/python/intensivao/login


import pyautogui
import time

pyautogui.PAUSE = 0.5

# Abrir o Google Chrome
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")

# Entrar no link
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
pyautogui.write(link)
pyautogui.press("enter")

# esperar o site carregar
pyautogui.sleep(3)

# Passo 2: Fazer login
pyautogui.click(x=789, y=595)
pyautogui.write("teste@teste.com.br")

pyautogui.press("tab")
pyautogui.write("suasenha")

pyautogui.press("tab")
pyautogui.press("enter")

time.sleep(3)

# Passo 3: Importar a base de dados
import pandas

tabela = pandas.read_csv("produtos.csv")

# Passo 4: cadastrar 1 produto

for linha in tabela.index:

    time.sleep(2)
    pyautogui.click(x=850, y=418)

    codigo = tabela.loc[linha, "codigo"]



    # preencher os campos
    pyautogui.write(str(codigo))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "marca"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "tipo"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")

    obs = tabela.loc[linha, "obs"]
    if not pandas.isna(obs):
        pyautogui.write(str(obs))

    pyautogui.press("tab")
    pyautogui.press("enter")

    pyautogui.scroll(50000)

# passo 5: Repetir para todos os produtos
