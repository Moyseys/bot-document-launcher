import pyautogui
import time
import os

def find_and_click(imagem, descricao):
    try:
        try:
            localizacao = pyautogui.locateCenterOnScreen(imagem, confidence=0.8)
            if localizacao is not None:
                pyautogui.click(localizacao)
                time.sleep(1)
                return
            else:
                print(f"{descricao} não localizado com confiança 0.8.")
        except Exception as e:
            print(f"Erro na tentativa 1 com confiança 0.8: {e}")
    
        try:
            localizacao = pyautogui.locateCenterOnScreen(imagem, confidence=0.7)
            if localizacao is not None:
                pyautogui.click(localizacao)
                time.sleep(1)
                return
            else:
                print(f"{descricao} não localizado com confiança 0.7.")
        except Exception as e:
            print(f"Erro na tentativa 2 com confiança 0.7: {e}")

            print(f"Tentando novamente localizar {descricao} após 1 segundo.")
            time.sleep(1)
            find_and_click(imagem, descricao)
    except Exception as e:
        print(f"Erro inesperado ao localizar e clicar em {descricao}: {e}")