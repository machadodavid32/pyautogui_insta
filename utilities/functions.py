import webbrowser
import pyautogui
from time import sleep
from threading import Thread

def trocar_conta():
 # Trocar de conta
    pyautogui.click(1323,693, duration=2) # vai clicar mais abaixo para aumentar compatibilidade
    pyautogui.click(1245,627, duration=2)
    sleep(2)

def clique_fora():
    # Clique fora - eviar inf pra guardar nome de usuario pelo browser
    pyautogui.click(1391,314, duration=2)
    pyautogui.click(1388,371, duration=2)
    sleep(2)