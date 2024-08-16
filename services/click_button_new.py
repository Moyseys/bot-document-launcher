from find_and_click import find_and_click
import time
import os

def click_button_new():
    time.sleep(1.5)
    base_path = os.path.join(os.getcwd(), 'static', 'icons').replace('\\', '/')
    icon_btn_new = os.path.join(base_path, 'btn_new.png').replace('\\', '/')
    find_and_click(icon_btn_new, "icon_btn_new")
    time.sleep(1)