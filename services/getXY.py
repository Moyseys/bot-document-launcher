import pyautogui
import time

print("Pressione Ctrl+C para parar o programa.")

try:
    while True:
        x, y = pyautogui.position()
        
        print(f"A posição atual do cursor é: ({x}, {y})", end="\r")
        
        time.sleep(0.1)
except KeyboardInterrupt:
    print("\nPrograma interrompido pelo usuário.")
