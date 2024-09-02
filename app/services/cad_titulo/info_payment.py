#Vai até a guia de pagamento
import os
import time
import pyautogui

from .find_and_click import find_and_click


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