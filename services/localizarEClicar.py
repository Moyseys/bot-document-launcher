import pyautogui
import time
import os
from PIL import Image

def localizar_e_clicar(imagem, descricao):
    base_path = os.path.join(os.getcwd(), 'static', 'icons').replace('\\', '/')
    try:
        print(f"Tentativa 1: Procurando {descricao} com confiança 0.8...")
        try:
            localizacao = pyautogui.locateCenterOnScreen(imagem, confidence=0.8)
            if localizacao is not None:
                pyautogui.click(localizacao)
                print(f"{descricao} localizado e clicado com confiança 0.8.")
                time.sleep(1)
                return
            else:
                print(f"{descricao} não localizado com confiança 0.8.")
        except Exception as e:
            print(f"Erro na tentativa 1 com confiança 0.8: {e}")
        
        print(f"Tentativa 2: Procurando {descricao} com confiança 0.7...")
        try:
            localizacao = pyautogui.locateCenterOnScreen(imagem, confidence=0.7)
            if localizacao is not None:
                pyautogui.click(localizacao)
                print(f"{descricao} localizado e clicado com confiança 0.7.")
                time.sleep(1)
                return
            else:
                print(f"{descricao} não localizado com confiança 0.7.")
        except Exception as e:
            print(f"Erro na tentativa 2 com confiança 0.7: {e}")

        print(f"Tentativa 3: Redimensionando a imagem para procurar {descricao} com confiança 0.7...")
        # Terceira tentativa: redimensionar a imagem e tentar novamente
        try:
            with Image.open(imagem) as img:
                img = img.resize((img.width // 2, img.height // 2))
                resized_image_path = os.path.join(base_path, 'resized_image.png')
                img.save(resized_image_path)
        
            localizacao = pyautogui.locateCenterOnScreen(resized_image_path, confidence=0.7)
            if localizacao is not None:
                pyautogui.click(localizacao)
                print(f"{descricao} localizado e clicado após redimensionamento com confiança 0.7.")
                time.sleep(1)
                return
            else:
                print(f"{descricao} não localizado após redimensionamento com confiança 0.7.")
        except Exception as e:
            print(f"Erro na tentativa 3 com redimensionamento: {e}")

        # Se todas as tentativas falharem, levanta a exceção personalizada
        raise TentativasExcedidasException(f"{descricao} não localizado na tela após todas as tentativas.")
    
    except TentativasExcedidasException as e:
        print(e)
        raise  # Relevanta a exceção para parar o programa
    except Exception as e:
        print(f"Erro inesperado ao localizar e clicar em {descricao}: {e}")