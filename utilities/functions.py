import webbrowser
import pyautogui
from time import sleep
from threading import Thread

def trocar_conta():
 # Trocar de conta
    pyautogui.click(1323,693, duration=2) # vai clicar mais abaixo para aumentar compatibilidade
    pyautogui.click(1245,627, duration=2)
    sleep(2)
