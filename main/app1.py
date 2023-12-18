import PySimpleGUI as sg

from time import sleep
from threading import Thread
from utilities.functions import *

sg.theme('LightBrown')



layout = [
    [sg.Text("Digite seu usuario: ")],
    [sg.Input(key='usuario')],
    [sg.Text('Digite sua senha: ')],
    [sg.Input(password_char='*', key='senha')],
    [sg.Text('O que pesquisar?')],
    [sg.Input(key='pesquisa')],
    [sg.Text('Digite seu comentário')],
    [sg.Input(key='comentario')],
    [sg.Button('Start')],
    [sg.Output(size=(60,10))]    
]

window = sg.Window('InstaAuto', layout=layout)



while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    elif event == 'Start':
        thread_inicio = Thread(target='Start', daemon=True)
        thread_inicio.start()
        usuario = values['usuario']
        senha = values['senha']
        pesquisa = values['pesquisa']
        comentario = values['comentario']
        
        start(usuario)
        sleep(3)  
        #trocar_conta() 
        sleep(2)
        clique_fora()
        sleep(2)
        password(senha)
        sleep(3)
        enter()
        sleep(2)
        evitar()
        sleep(3)
        confirmando_login()
        sleep(2)
        postagem(pesquisa)
        sleep(2)
        like(comentario)
        sair()
        
        
            
    