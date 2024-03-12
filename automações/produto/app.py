# Ler dados da planilha
# inserir cada célula de cada linha em um campo do sistema

import openpyxl
import pyautogui
import time

workbook = openpyxl.load_workbook('planilha.xlsx')
codigo_sheet = workbook['codigo']

# clicar na janela do chrome
pyautogui.click(597, 23)
for linha in codigo_sheet.iter_rows(min_row=2):

    # atalho para busca
    pyautogui.hotkey('ctrl', 'shift', 'p')
    time.sleep(1)
    pyautogui.write(str(linha[0].value))
    pyautogui.press('tab')
    # clicar na aba gerenciais
    pyautogui.click(629, 791)
    time.sleep(1)
    pyautogui.hotkey('alt', 'g')
    time.sleep(2)
    pyautogui.click(1152, 640)
    time.sleep(2)
