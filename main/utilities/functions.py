import pyautogui
import webbrowser
from time import sleep


def clique_fora():
    # Clique fora - eviar inf pra guardar nome de usuario pelo browser
    pyautogui.click(1391,314, duration=2)
    pyautogui.click(1388,371, duration=2)
    sleep(2)

def start(usuario):
    webbrowser.open_new_tab('https://www.instagram.com')
    sleep(5)
    # login
    trocar_conta = pyautogui.locateCenterOnScreen('trocar_conta.png')
    if trocar_conta is not None:
        pyautogui.click(trocar_conta)
    else:
        print('Campo não localizado')     
    sleep(2)
    email = pyautogui.locateCenterOnScreen('email.png')
    if email is not None:
        pyautogui.click(email)
        sleep(1)
        pyautogui.typewrite(usuario)
        sleep(2)
    else:
        print('Campo não encontrado')    

def password(senha):
      # Senha
        pyautogui.click(1066,414, duration=2)
        pyautogui.typewrite(senha)
        sleep(2)        
        
def enter():
    pyautogui.click(1114,446, duration=2)
    sleep(5)            
    

# Evitar inf salvar login
def evitar():        
    pyautogui.click(1051,593, duration=2)
    sleep(3)    


def confirmando_login():
    pesq = pyautogui.locateCenterOnScreen('pesquisa.png')
    if pesq is None:
        print('Usuário ou senha incorretos.')
    else:    
        print('Automação Iniciada')
        # Não salvar
        pyautogui.click(1044,613, duration=1)


def postagem(pesquisa):
    # 2 - clicar em pesquisar
    pyautogui.click(185,319, duration=1)
    sleep(1)
    pyautogui.click(293,226, duration=1) # segunda tela de pesquisa
    sleep(2)

    # Escrevendo o que pesquisar
    pyautogui.typewrite(pesquisa)

    # Clicando no resultado da pesquisa
    pyautogui.click(279,339, duration=1)
    sleep(1)


    # Mover até a publicação
    pyautogui.moveTo(682,761,duration=2)
    sleep(5)
    # Clicar na publicação
    pyautogui.click(683,768,duration=1)
    sleep(3)
    # Clicar em curtir
    pyautogui.click(1115,869,duration=1)
    sleep(2)
    pyautogui.click(947,881, duration=2)
    sleep(2)          

def like(comentario):
    # 10 - Verificar se já curtiu ou não aquela postagem
    coracao = pyautogui.locateCenterOnScreen('coracao.png')
    sleep(1)
    # 11 - Se já tiver curtido, fazer nada, e pausar o bot por 24 horas
    if coracao is not None:
        sleep(86400)
    # 12 - Se não tiver curtido, curtir a foto
    elif coracao == None:
        pyautogui.click(1140,866,duration=1)
        sleep(5)
        # 13 - Se não tiver curtido, comentar na foto
        pyautogui.click(1205,980,duration=2)
        sleep(3)
        
        # 14 - Escrevendo o comentário
        pyautogui.typewrite(comentario)
        sleep(2)
        
        # 15 - Clicando em publicar
        pyautogui.click(1571,979, duration=2)
        sleep(2)   
        
def sair():
    # Para sair do site
    pyautogui.click(33,984, duration=1)
    sleep(2)
    pyautogui.click(33,984, duration=1)
    sleep(2)
    # Deslogar
    pyautogui.click(46,922, duration=2)
    sleep(1)
               
            