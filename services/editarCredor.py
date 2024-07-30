import time
import pyautogui
import os
from .localizarEClicar import localizar_e_clicar


def editarCredor(nome, numero, email):
    base_path = os.path.join(os.getcwd(), 'py', 'static', 'icons').replace('\\', '/')
    
    icon_btn_contato = os.path.join(base_path, 'bntContatos.png')
    localizar_e_clicar(icon_btn_contato, "icon_btn_contato")
    pyautogui.scroll(-900)

    icon_btn_adicionar = os.path.join(base_path, 'bntAdicionar.png')
    localizar_e_clicar(icon_btn_adicionar, "icon_btn_adicionar")
    
    pyautogui.write(nome)

    pyautogui.press("tab")
    pyautogui.press("tab")
    pyautogui.press("tab")

    icon_input_checkbox = os.path.join(base_path, 'inputCheckBoxAmarelo.png')
    localizacao = pyautogui.locateCenterOnScreen(icon_input_checkbox, confidence=0.9)
    pyautogui.click(localizacao)
    print(f"inputCheckBoxAmarelo localizado e clicado.")
    
    pyautogui.hotkey("shift", "tab")
    if numero is not None:
        pyautogui.write(numero)
 
    if email is not None:
        pyautogui.press("tab")
        pyautogui.press("tab")
        pyautogui.press("tab")
        pyautogui.write(email)

    btn_salvar = os.path.join(base_path, 'btnSalvar.png')
    localizar_e_clicar(btn_salvar, "btnSalvar")
    pyautogui.press("f5")