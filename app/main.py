from datetime import datetime
from services.cad_titulo.get_cell_value import get_cell_value
from services.cad_titulo.logs import add_log, get_last_logged_line
from services.cad_titulo.process_doc import process_doc

import pyautogui
import os
from colorama import Fore, Style, init
init()

pyautogui.FAILSAFE = True

base_path = os.getcwd()
path_static = os.path.join(os.getcwd(), 'static').replace('\\', '/')
nfsXlsx = os.path.join(path_static, 'relatorio.xlsx').replace('\\', '/')
logs_file_path = os.path.join(base_path, "logs.json")


if not get_cell_value(nfsXlsx, "Relatório", "N", 7) == "Núm/Série":
    raise "O valor da célula na posição N7 da planilha 'Relatório' não é 'Núm/Série'."

start_line = None
end_line = None
safety_lok = None
#process_doc(59, 100, 1, nfsXlsx, logs_file_path)
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
    time_now = datetime.now().time()
    msg_time = f"\n{Fore.MAGENTA}Horário do inicio da execução: {time_now.strftime("%H:%M:%S")} {Style.RESET_ALL}"
    print(msg_time)

    process_doc(start_line, end_line, safety_lok, nfsXlsx, logs_file_path)