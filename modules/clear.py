import os
import platform

def clear():
    system = platform.system()
    
    if system == 'Windows':
        os.system('cls')
    elif system == 'Linux':
        os.system('clear')

clear()
