from services.find_and_click import find_and_click
from services.get_cell_value import get_cell_value
import time
import pyautogui
import pyperclip
import json
import os
from datetime import datetime, timedelta
from colorama import Fore, Style, init

init()

pyautogui.FAILSAFE = True

#Clica no btn novo
def click_button_new():
    time.sleep(1.5)
    base_path = os.path.join(os.getcwd(), 'static', 'icons').replace('\\', '/')
    icon_btn_new = os.path.join(base_path, 'btn_new.png').replace('\\', '/')
    find_and_click(icon_btn_new, "icon_btn_new")
    time.sleep(1)

#Insere o tipo de documento
def insert_type_document():
    pyautogui.write("NFE")
    pyautogui.press("tab")
    time.sleep(1.5)

#Insere o N° do doc
def insert_n_doc(document_number):
    pyautogui.press("tab")
    pyautogui.write(document_number)
    pyautogui.press("tab")
    time.sleep(1.5)

#Insere a data de vencimento]
def insert_due_date():
    for _ in range(17):
        pyautogui.press("tab")

    time.sleep(1)

    today = datetime.today()
    future_date = today + timedelta(days=10)
    formatted_date = future_date.strftime('%d/%m/%Y')
    pyautogui.write(formatted_date)

    time.sleep(1)

#Insere o cento de custo e o plano financeiro
def insert_prop_expenses(cost_center_code, financial_plan_code):
    for _ in range(2):
        pyautogui.press("tab")

    pyautogui.press("enter")
    time.sleep(1)
    pyautogui.write(cost_center_code)

    for _ in range(2):
        pyautogui.press("tab")

    time.sleep(1)
    pyautogui.write(financial_plan_code)
    pyautogui.press("tab")
    time.sleep(1)

    for _ in range(3):
        pyautogui.press("tab")

    pyautogui.press("enter")

#Salva
def save():
    time.sleep(1)

    pyautogui.press("tab")
    pyautogui.press("enter")

    time.sleep(6)

#Vai até a guia de pagamento
def go_to_payment_guide():
    for _ in range(7):
        pyautogui.press("tab")
    pyautogui.press("enter")

#Edita o pagamento
def edit_payment(payment_form_code):
    time.sleep(1)
    base_path = os.path.join(os.getcwd(), 'static', 'icons').replace('\\', '/')
    btn_pencil = os.path.join(base_path, 'btn_pencil.png').replace('\\', '/')
    find_and_click(btn_pencil, "btn_pencil")
    time.sleep(1)

    for _ in range(8):
        pyautogui.press("tab")
    pyautogui.write(payment_form_code)
    pyautogui.press("tab")
    time.sleep(1)

    pyautogui.press("enter")
    time.sleep(1)


def move_cursor_to_center():
    screen_width, screen_height = pyautogui.size()
    center_x = screen_width / 2
    center_y = screen_height / 2
    pyautogui.moveTo(center_x, center_y)

def go_to_nfe_folder():
    for _ in range(6):
        pyautogui.press("tab")
    pyautogui.press("enter")
    path_nfse_s = "C:\\Users\\MoyseysFerreiraVeron\\Desktop\\lancador_de_nfe\\static\\NFSES"
    pyautogui.write(path_nfse_s)
    pyautogui.press("enter")
    for _ in range(6):
        pyautogui.press("tab")
    
    return

#attachment
def attachment(document_identifier, is_first): 
    base_path = os.path.join(os.getcwd(), 'static', 'icons').replace('\\', '/')
    for _ in range(8):
        pyautogui.press("tab")
    pyautogui.press("enter")

    time.sleep(1)

    move_cursor_to_center()
    pyautogui.click()

    for _ in range(3):
        pyautogui.press("tab")

    pyautogui.hotkey('ctrl', 'c')
    copied_text = pyperclip.paste()
    title = copied_text.strip()
    time.sleep(1)
    print(f"{Fore.RED}{Style.BRIGHT}Título: {title}{Style.RESET_ALL}")

    for _ in range(2):
        pyautogui.press("tab")
    pyautogui.press("enter")
    
    for _ in range(2):
        pyautogui.hotkey('shift', 'tab')

    pyautogui.write("NFE")
    pyautogui.press("tab")
    pyautogui.press("enter")
    time.sleep(1)
    if is_first: 
        go_to_nfe_folder()
    pyautogui.write(document_identifier)
    pyautogui.press("enter")

    pyautogui.press("tab")
    pyautogui.press("tab")
    pyautogui.press("enter")

    return title

def restart_page():
    pyautogui.press("f5")
    time.sleep(4)

def add_log(logs_file_path, log_entry):
    # Carregar logs existentes do arquivo JSON, se existir
    if os.path.exists(logs_file_path):
        with open(logs_file_path, 'r') as log_file:
            logs = json.load(log_file)
    else:
        logs = []

    # Adicionar o novo log
    logs.append(log_entry)

    # save os logs atualizados no arquivo JSON
    with open(logs_file_path, 'w') as log_file:
        json.dump(logs, log_file, indent=4)

def get_last_logged_line(logs_file_path):
    """Retrieves the last logged line number from the logs file."""
    if not os.path.exists(logs_file_path):
        print("Log file does not exist.")
        return None

    with open(logs_file_path, 'r') as log_file:
        logs = json.load(log_file)
    
    if not logs:
        print("No logs found.")
        return None
    
    # A última entrada no log
    last_entry = logs[-1]
    
    # Retorna o valor da chave 'linha' se ela existir
    return last_entry.get("linha", None)

def cursor_position():
    screen_width, screen_height = pyautogui.size()
    x, y = pyautogui.position()
    
    direita = (screen_width / 100) * 95
    esquerda = (screen_width / 100) * 5

    cursor_position = ""

    if x <= esquerda:
        cursor_position = "Esquerda" 
    elif x >= direita:
        cursor_position = "Direita" 
    else:
        cursor_position = "Meio" 

    return cursor_position

def choose_user():
    cursor_position_current = ""
    choice = ""
    while True:
        if(cursor_position_current == "Esquerda"):
            choice = "Esquerda"
            break
        elif(cursor_position_current == "Direita"):
            choice = "Direita"
            break

        cursor_position_current = cursor_position()
        time.sleep(2)

    return choice

def process_doc(start_line, end_line, safety_lok, nfsXlsx, logs_file_path):
    is_first = True
    cont = 0

    for i in range(start_line, end_line):
        print(f"{Fore.GREEN}{Style.BRIGHT}Linha atual: {i}{Style.RESET_ALL}")

        # Extart N° do documento da celula
        cell_value = get_cell_value(nfsXlsx, "Relatório", "N", i)
        document_number = ""
        if cell_value is not None:
            document_number = cell_value.split('/')[0]
            print(f"{Fore.CYAN}{Style.BRIGHT}N° Documento: {document_number}{Style.RESET_ALL}")
            titulo = get_cell_value(nfsXlsx, "Relatório", "Q", i)
            if titulo:
                print(f"{Fore.CYAN}{Style.BRIGHT}Documento já lançado\nTítulo: {titulo} {document_number}{Style.RESET_ALL}") 
                continue
        else:
            print(f"A célula N{i} está vazia ou não existe.")
            return

        # Faz o lançamento do documento
        click_button_new()
        insert_type_document()
        insert_n_doc(document_number)
        insert_due_date()
        insert_prop_expenses("49", "2010103")
        save()
        go_to_payment_guide()
        edit_payment("15")

        title = attachment(document_number, is_first)
        is_first = False

        log_entry = {
                "título": title,
                "document_number": document_number,
                "status": "Lançado com sucesso",
                "linha": i
            }
        add_log(logs_file_path, log_entry)

        move_cursor_to_center()
        
        cont = cont + 1
        print(cont)

        if cont == safety_lok:
            cont = 0
            message = (f"{Fore.CYAN}{Style.BRIGHT}Deseja continuar a execução?{Style.RESET_ALL}\n"
            f"{Fore.YELLOW}Caso deseje, posicione seu cursor no canto direito da tela,"
            f" caso contrário, posicione no canto esquerdo da tela.{Style.RESET_ALL}")

            print(message)

            choice = choose_user()
            if (choice == "Direita"):
                print("Execução confirmada")
            else:
                print("Execução finalizada!")
                break

        restart_page()



base_path = os.path.join(os.getcwd(), 'static').replace('\\', '/')
nfsXlsx = os.path.join(base_path, 'relatorio.xlsx').replace('\\', '/')
logs_file_path = 'logs.json'

if not get_cell_value(nfsXlsx, "Relatório", "N", 7) == "Núm/Série":
    raise CellValueError("O valor da célula na posição N7 da planilha 'Relatório' não é 'Núm/Série'.")

start_line = None
end_line = None
safety_lok = None

while(True):
    try:
        choice = int(input(f"\n{Fore.YELLOW}Deseja realizar o lançamento a partir de qual linha do relatório?\n"
            "1 - Última linha executada.\n"
            "2 - Digitar uma linha para inicialização.\n\n"
            f"Digite uma opção aqui: {Style.RESET_ALL}"))

        if choice not in  [1 ,2]: 
            print(f"{Fore.RED}Opção inválida. Por favor, escolha 1 ou 2.{Style.RESET_ALL}")
            continue
        
        if choice == 1: 
            last_line = get_last_logged_line(logs_file_path)
            if last_line is None:
                print(f"{Fore.RED}Não foi possível determinar a última linha executada. Por favor, escolha a linha manualmente.{Style.RESET_ALL}")
                continue
            start_line = last_line + 1
        else: 
            start_line = int(input(f"\n{Fore.YELLOW}Digite a linha que deseja começar o lançamento: {Style.RESET_ALL}"))

        end_line = int(input(f"\n{Fore.YELLOW}Digite a linha até qual será lançado: {Style.RESET_ALL}"))
        safety_lok = int(input(f"\n{Fore.YELLOW}Digite quantos seram lançados antes da trava de segurança aparecer: {Style.RESET_ALL}"))
        break
    except ValueError:
        print(f"{Fore.RED}Entrada inválida. Por favor, insira um número inteiro.{Style.RESET_ALL}")

if(start_line and end_line):
    process_doc(start_line, end_line, safety_lok, nfsXlsx, logs_file_path)