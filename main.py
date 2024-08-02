from services.localizarEClicar import localizar_e_clicar
from services.getCellValue import get_cell_value
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

#Clica no btn novo
def clica_btn_novo():
    time.sleep(1.5)
    base_path = os.path.join(os.getcwd(), 'static', 'icons').replace('\\', '/')
    icon_btn_novo = os.path.join(base_path, 'btn_novo.png').replace('\\', '/')
    localizar_e_clicar(icon_btn_novo, "icon_btn_novo")
    time.sleep(1)

#Insere o tipo de documento
def insere_tipo_documento():
    pyautogui.write("NFE")
    pyautogui.press("tab")

#Insere o N° do doc
def insere_n_doc(numero_documento):
    time.sleep(1)
    pyautogui.press("tab")
    pyautogui.write(numero_documento)
    pyautogui.press("tab")
    time.sleep(1.5)

#Insere a data de vencimento
def insere_data_vencimento():
    for _ in range(17):
        pyautogui.press("tab")
    time.sleep(1)

# Calcula a data de hoje mais 10 dias
def calcula_data_vencimento():
    hoje = datetime.today()
    data_futura = hoje + timedelta(days=10)
    data_formatada = data_futura.strftime('%d/%m/%Y')
    pyautogui.write(data_formatada)

#Insere o cento de custo e o plano financeiro
def insere_prop_despesas(codigo_centro_custo, codigo_plano_financeiro):
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
def salvar():
    time.sleep(1)

    for _ in range(10):
        pyautogui.press("tab")
    pyautogui.press("enter")

    time.sleep(4)

#Vai até a guia de pagamento
def ate_guia_pagamento():
    for _ in range(7):
        pyautogui.press("tab")
    pyautogui.press("enter")

#Edita o pagamento
def edita_pagamento(codigo_forma_pagamento):
    time.sleep(1)
    base_path = os.path.join(os.getcwd(), 'static', 'icons').replace('\\', '/')
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
def anexo(): 
    base_path = os.path.join(os.getcwd(), 'static', 'icons').replace('\\', '/')
    for _ in range(8):
        pyautogui.press("tab")
    pyautogui.press("enter")

    time.sleep(1.5)
    pyautogui.scroll(-900)
    time.sleep(2.5)

    btn_novo_anexo = os.path.join(base_path, 'btn_novo_anexo.png').replace('\\', '/')
    localizar_e_clicar(btn_novo_anexo, "btn_novo_anexo")
    time.sleep(1)

    input_anexo = os.path.join(base_path, 'input_anexo.png').replace('\\', '/')
    localizar_e_clicar(input_anexo, "input_anexo")
    pyautogui.write("NFE")
    pyautogui.press("tab")
    pyautogui.press("enter")
    time.sleep(1)

def reinicia_pagina():
    pyautogui.press("f5")
    time.sleep(4)


# numero_documento = 
# codigo_centro_custo = "49"
# codigo_plano_financeiro = "2010103"
# codigo_forma_pagamento = "15"

base_path = os.path.join(os.getcwd(), 'static').replace('\\', '/')
nfsXlsx = os.path.join(base_path, 'relatorio.xlsx').replace('\\', '/')

if not get_cell_value(nfsXlsx, "Relatório", "N", 7) == "Núm/Série":
    raise CellValueError("O valor da célula na posição N7 da planilha 'Relatório' não é 'Núm/Série'.")

for i in range(8, 18):
    # Extart N° do documento da celula
    cell_value = get_cell_value(nfsXlsx, "Relatório", "N", i)
    if cell_value is not None:
        numero_documento = cell_value.split('/')[0]
        print(numero_documento)
    else:
        print(f"A célula N{i} está vazia ou não existe.")

    # Faz o lançamento do documento
    clica_btn_novo()

    # Perguntar ao usuário se deseja continuar
    continuar = input("Deseja continuar a execução? (s/n): ")
    if continuar.lower() != 's':
        print("Execução interrompida pelo usuário.")
        break

    reinicia_pagina()