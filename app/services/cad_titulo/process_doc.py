import time
import pyautogui
from colorama import Fore, Style, init

from .get_cell_value import get_cell_value
from .attachment import attachment
from .cursor_actions import choose_user, move_cursor_to_center
from .info_payment import edit_payment, go_to_payment_guide
from .logs import add_log
from .register import click_button_new, click_input_n_doc, popup_find_nfe, insert_due_date, insert_n_doc, insert_prop_expenses, insert_type_document, save

def restart_page():
    pyautogui.press("f5")
    time.sleep(4)

def process_doc(start_line, end_line, safety_lok, nfsXlsx, logs_file_path):
    is_first = True
    cont = 0

    for i in range(start_line, end_line):
        print(f"{Fore.GREEN}{Style.BRIGHT}Linha atual: {i}{Style.RESET_ALL}")

        # Extart N° do documento da celula
        document_number = get_cell_value(nfsXlsx, "Relatório", "N", i)
        date_of_issue = get_cell_value(nfsXlsx, "Relatório", "K", i)
        total_value = get_cell_value(nfsXlsx, "Relatório", "O", i)
        acess_key = get_cell_value(nfsXlsx, "Relatório", "L", i)

        if document_number is None or date_of_issue is None or total_value is None:
            print(f"{Fore.RED}{Style.BRIGHT}Planilha relatório inválida!{Style.RESET_ALL}")
            break

        if document_number is not None:
            document_number = document_number.split('/')[0]
            print(f"{Fore.CYAN}{Style.BRIGHT}N° Documento: {document_number}{Style.RESET_ALL}")
            titulo = get_cell_value(nfsXlsx, "Relatório", "Q", i)
            if titulo:
                print(f"{Fore.CYAN}{Style.BRIGHT}Documento já lançado\nTítulo: {titulo} {document_number}{Style.RESET_ALL}") 
                continue
        else:
            print(f"A célula N{i} está vazia ou não existe.")
            return

        #Faz o lançamento do documento
        tabs_to_input_date = 17

        click_button_new()
        insert_type_document()
        insert_n_doc(document_number)
        
        is_auto_complet = not popup_find_nfe()
        if not is_auto_complet:  
            print(f"{Fore.RED}{Style.BRIGHT}Essa NFE não esta sendo puxada automaticamente, será necessário realizar o lançamento manualmente...{Style.RESET_ALL}")
            for _ in range(11):
                pyautogui.press("tab")
            pyautogui.press("enter")

            time.sleep(1)
            #Doc
            click_input_n_doc()
            pyautogui.write(document_number)
            pyautogui.press("tab")

            #Empresa
            pyautogui.write("1")
            pyautogui.press("tab")
            time.sleep(0.5)
            pyautogui.press("tab")

            #Credor
            pyautogui.write("5030")
            pyautogui.press("tab")
            pyautogui.press("tab")
            pyautogui.press("tab")

            #Data de emissão
            pyautogui.write(str(date_of_issue))
            pyautogui.press("tab")
            pyautogui.press("tab")

            #Valor total
            pyautogui.write(str(total_value))
            pyautogui.press("tab")
            pyautogui.press("tab")

            tabs_to_input_date = 7


        
        insert_due_date(tabs_to_input_date)
        insert_prop_expenses("49", "2010103")
        save()

        if not is_auto_complet:
            # vai até a guia informações fiscais
            for _ in range(6):
                pyautogui.press("tab")
        
            pyautogui.press("enter")
            time.sleep(1.5)
            
            #Adiciona um serviço
            pyautogui.press("enter")
            time.sleep(1.5)

            #Vai até campo 
            for _ in range(10):
                pyautogui.press("tab")

            pyautogui.press("right")
            time.sleep(0.5)
            for _ in range(4):
                pyautogui.press("tab")

            # codigo fiscal
            time.sleep(1.5)
            pyautogui.write("2653")
            pyautogui.press("tab")
            time.sleep(1.5)

            
            pyautogui.press("tab")
            
            #Outros Dados
            #Apuração do PIS/COFINS*
            pyautogui.press("enter")
            time.sleep(0.5)
            pyautogui.press("up")
            time.sleep(0.5)
            pyautogui.press("enter")
            time.sleep(0.5)
            
            #Modalidade do frete*
            pyautogui.press("tab")
            pyautogui.press("enter")
            time.sleep(0.5)
            pyautogui.write("s")
            pyautogui.press("enter")
            pyautogui.press("tab")

            #Chave de acesso
            pyautogui.write(acess_key)
            pyautogui.press("tab")
            #Salva
            pyautogui.press("enter")

            #Volta guia       
            pyautogui.press("tab")
            pyautogui.press("enter")

            time.sleep(1.5)

        go_to_payment_guide()
        edit_payment("15")
        title = attachment(document_number, is_first)
        for _ in range(2):
            pyautogui.press("tab")
        pyautogui.press("enter")
        time.sleep(1)
        
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