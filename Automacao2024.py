import pyautogui
import time

pyautogui.PAUSE = 0.5

pyautogui.press('win')
pyautogui.write('opera')
pyautogui.press('enter')

pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press('enter')  
time.sleep(1)

pyautogui.press('tab')
pyautogui.write('pythonimpressionador@gmail.com')
time.sleep(0.3)

pyautogui.press('tab')
pyautogui.write('12345')
time.sleep(0.2) 
pyautogui.press('tab')
pyautogui.press('enter')

import pandas as pd

tabela = pd.read_csv("produtos.csv")

print(tabela)

for linha in tabela.index:
    pyautogui.click(x=739, y=298)
    codigo = tabela.loc [linha, 'codigo']
    pyautogui.write(str(codigo))
    pyautogui.press('tab')
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
    if not pd.isna(obs):
        pyautogui.write(str(tabela.loc[linha, "obs"]))
    pyautogui.press("tab")
    pyautogui.press("enter")
    pyautogui.scroll(5000)
    
