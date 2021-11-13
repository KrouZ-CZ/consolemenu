from pynput import keyboard
from os import system as cmd
def start(sel):
    global selection
    global massiv
    selection = 0
    massiv = sel
    pr()
    listener = keyboard.Listener(on_press=on_press)
    listener.start()
    listener.join()
    cmd('pause > nul')
    return selection
def pr():
    for i in range(len(massiv)):
        if selection == i:
            print(str(int(i) + 1)+'. '+massiv[i]+' <')
        else:
            print(str(int(i) + 1)+'. '+massiv[i])
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
        cmd('cls')
        pr()
    elif key == keyboard.Key.up:
        math('minus')
        cmd('cls')
        pr()
    elif key == keyboard.Key.enter:
        return False