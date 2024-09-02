import os
import time
import pyautogui
import pyperclip

from .cursor_actions import move_cursor_to_center
from colorama import Fore, Style, init

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