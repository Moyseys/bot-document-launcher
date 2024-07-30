import time
import pyautogui
import os
from .localizarEClicar import localizar_e_clicar



def buscarCredor(razaoSocial):
    base_path = os.path.join(os.getcwd(), 'py', 'static', 'icons').replace('\\', '/')
    
    icon_input_razao_social = os.path.join(base_path, 'inputRazaoSocial.png')
    icon_btn_consultar = os.path.join(base_path, 'btnConsultar.png')
    icon_btn_pensil = os.path.join(base_path, 'btnPensil.png')

    localizar_e_clicar(icon_input_razao_social, 'inputRazaoSocial')
    time.sleep(1.5)
    pyautogui.write(razaoSocial)
    
    localizar_e_clicar(icon_btn_consultar, 'btnConsultar')
    time.sleep(1.5)
    localizar_e_clicar(icon_btn_pensil, 'btnPensil')
