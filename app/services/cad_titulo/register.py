from datetime import datetime, timedelta
import os
import time
import pyautogui

from .find_and_click import find_and_click

#Verefica se o pop de pesquisa de NFE  aparece na tela
def popup_find_nfe():
    try:
        base_path = os.path.join(os.getcwd(), 'static', 'icons').replace('\\', '/')
        popup_not_find_nfe = os.path.join(base_path, 'popup_not_find_nfe.png').replace('\\', '/')
        localizacao = pyautogui.locateCenterOnScreen(popup_not_find_nfe, confidence=0.8)

        if localizacao is not None:
            return True
        else:
            return False
    except Exception:
        return False

#Clica no btn novo
def click_input_n_doc():
    base_path = os.path.join(os.getcwd(), 'static', 'icons').replace('\\', '/')
    input_n_doc = os.path.join(base_path, 'input_n_doc.png').replace('\\', '/')
    find_and_click(input_n_doc, "input_n_doc")
    time.sleep(1)

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

#Insere a data de vencimento
def insert_due_date(tabs_to_input):
    for _ in range(tabs_to_input):
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