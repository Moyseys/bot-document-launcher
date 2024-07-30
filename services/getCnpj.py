import os
import time
import pyautogui
import pyperclip

def getCnpj():
    base_dir = os.path.join(os.getcwd(), 'py', 'static', 'icons').replace('\\', '/')
    icon_cnpj = os.path.join(base_dir, "iconCnpj.png")
    pyautogui.moveTo(icon_cnpj)
    time.sleep(1)
    pyautogui.moveRel(70, 0)
    pyautogui.click()
    pyautogui.hotkey('ctrl', 'a')
    pyautogui.hotkey('ctrl', 'c')
    cnpj_value = pyperclip.paste()
    return cnpj_value