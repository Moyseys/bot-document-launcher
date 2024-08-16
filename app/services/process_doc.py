import time
import pyautogui
from colorama import Fore, Style, init

from .get_cell_value import get_cell_value
from .attachment import attachment
from .cursor_actions import choose_user, move_cursor_to_center
from .info_payment import edit_payment, go_to_payment_guide
from .logs import add_log
from .register import click_button_new, insert_due_date, insert_n_doc, insert_prop_expenses, insert_type_document, save

def restart_page():
    pyautogui.press("f5")
    time.sleep(4)

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