from pynput import keyboard
from os import system as cmd
from colorama import init
init()
from colorama import Fore, Back, Style
def start(sel, mode=0, title=None):
    global selection, massiv, titlep, modep
    titlep, modep = title, mode
    selection = 0
    massiv = sel
    pr()
    listener = keyboard.Listener(on_press=on_press)
    listener.start()
    listener.join()
    input()
    return selection
def pr():
    cmd('cls')
    if titlep != None:
        print(titlep+':\n')
    for i in range(len(massiv)):
        if modep == 0:
            if selection == i:
                print('> ' + str(int(i) + 1)+'. '+massiv[i])
            else:
                print(' '+str(int(i) + 1)+'. '+massiv[i])
        elif modep == 1:
            if selection == i:
                print(Fore.BLACK + Back.WHITE + str(int(i) + 1)+'. '+massiv[i] + Fore.WHITE + Back.BLACK)
            else:
                print(Fore.WHITE + Back.BLACK + str(int(i) + 1)+'. '+massiv[i] + Fore.WHITE + Back.BLACK)
def math(wh):
    global selection
    if wh == 'plus':
        selection += 1
        if selection == len(massiv):
            selection = 0
    elif wh == 'minus':
        selection -= 1
        if selection == -1:
            selection = len(massiv) - 1
def on_press(key):
    if key == keyboard.Key.down:
        math('plus')
        pr()
    elif key == keyboard.Key.up:
        math('minus')
        pr()
    elif key == keyboard.Key.enter:
        return False
