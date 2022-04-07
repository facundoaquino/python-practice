'''
¿Dónde se busca los módulos?
• Directorio actual + otros directorios definidos en la variable de ambiente PYTHONPATH

El módulo: deque (“double-ended queue”)
– Permite implementar pilas y colas.
''' 


# import the function 1

import os
import sys
 
from functions_m import double
 
def double(n):
  return n*3

print( double(8))

# import the function 2

# import functions_m

# print( functions_m.double(9))


print(sys.path.append('..'))
 
from helpers import triple 

print(triple.triple(9))
 

from helpers import clear_str 

print(clear_str.clear_str('testing a funcion from another directory'))
 
print('this is the main funcion')