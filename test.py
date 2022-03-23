
from time import time


for times in range(4):
    print(f'intento numero {times+1}')    
    str = input('ingresa una cadena: ')
    if 'r' in str:
        print(str)