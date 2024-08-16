import time
import pyautogui


def move_cursor_to_center():
    screen_width, screen_height = pyautogui.size()
    center_x = screen_width / 2
    center_y = screen_height / 2
    pyautogui.moveTo(center_x, center_y)

def cursor_position():
    screen_width, screen_height = pyautogui.size()
    x, y = pyautogui.position()
    
    direita = (screen_width / 100) * 95
    esquerda = (screen_width / 100) * 5

    cursor_position = ""

    if x <= esquerda:
        cursor_position = "Esquerda" 
    elif x >= direita:
        cursor_position = "Direita" 
    else:
        cursor_position = "Meio" 

    return cursor_position

def choose_user():
    cursor_position_current = ""
    choice = ""
    while True:
        if(cursor_position_current == "Esquerda"):
            choice = "Esquerda"
            break
        elif(cursor_position_current == "Direita"):
            choice = "Direita"
            break

        cursor_position_current = cursor_position()
        time.sleep(2)

    return choice    