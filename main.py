from services.localizarEClicar import localizar_e_clicar
import time
import pyautogui
import os
from datetime import datetime, timedelta
pyautogui.FAILSAFE = True

# nome_credor = input("Digite o nome do credor: ")
# numero_documento = input("Digite o número do documento: ")
# codigo_empresa = input("Digite o código da empresa: ")
# centro_custo = input("Digite o centro de custo: ")
# codigo_plano_financeiro = input("Digite o código do plano financeiro: ")
# codigo_forma_pagamento = input("Digite o código da forma de pagamento: ")

nome_credor = "João da Silva"
numero_documento = "131186"
codigo_centro_custo = "49"
codigo_plano_financeiro = "2010103"
codigo_forma_pagamento = "15"

#Clica no btn novo
time.sleep(1.5)
base_path = os.path.join(os.getcwd(), 'static', 'icons').replace('\\', '/')
icon_btn_novo = os.path.join(base_path, 'btn_novo.png').replace('\\', '/')
localizar_e_clicar(icon_btn_novo, "icon_btn_novo")
time.sleep(1)

#Insere o tipo de documento
pyautogui.write("NFE")
pyautogui.press("tab")

#Insere o N° do doc
time.sleep(1)
pyautogui.press("tab")
pyautogui.write(numero_documento)
pyautogui.press("tab")
time.sleep(1.5)

#Insere a data de vencimento
for _ in range(17):
    pyautogui.press("tab")

time.sleep(1)
# Calcula a data de hoje mais 10 dias
hoje = datetime.today()
data_futura = hoje + timedelta(days=10)
data_formatada = data_futura.strftime('%d/%m/%Y')
pyautogui.write(data_formatada)

#Insere o cento de custo e o plano financeiro
for _ in range(2):
    pyautogui.press("tab")

pyautogui.press("enter")
time.sleep(1)
pyautogui.write(codigo_centro_custo)

for _ in range(2):
    pyautogui.press("tab")

time.sleep(1)
pyautogui.write(codigo_plano_financeiro)
pyautogui.press("tab")
time.sleep(1)

for _ in range(3):
    pyautogui.press("tab")

pyautogui.press("enter")

#Salva
time.sleep(1)

for _ in range(10):
    pyautogui.press("tab")
pyautogui.press("enter")

time.sleep(4)

#Vai até a guia de pagamento
for _ in range(7):
    pyautogui.press("tab")
pyautogui.press("enter")

#Edita o pagamento
time.sleep(1)
btn_lapis = os.path.join(base_path, 'btn_lapis.png').replace('\\', '/')
localizar_e_clicar(btn_lapis, "btn_lapis")
time.sleep(1)

for _ in range(8):
    pyautogui.press("tab")
pyautogui.write(codigo_forma_pagamento)
pyautogui.press("tab")
time.sleep(1)

for _ in range(8):
    pyautogui.press("tab")
pyautogui.press("enter")
time.sleep(1)

#Anexo
for _ in range(8):
    pyautogui.press("tab")
pyautogui.press("enter")

time.sleep(1)
pyautogui.scroll(-900)
time.sleep(2)

btn_novo_anexo = os.path.join(base_path, 'btn_novo_anexo.png').replace('\\', '/')
localizar_e_clicar(btn_novo_anexo, "btn_novo_anexo")
time.sleep(1)

input_anexo = os.path.join(base_path, 'input_anexo.png').replace('\\', '/')
localizar_e_clicar(input_anexo, "input_anexo")
pyautogui.write("NFE")
pyautogui.press("tab")
pyautogui.press("enter")
time.sleep(1)