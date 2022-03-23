# Ingresar palabras desde el teclado hasta ingresar la palabra FIN. Imprimir
# aquellas que empiecen y terminen con la misma letra.

def getInput():
    str = input('ingresa una palabra: ')
    return str
    


inp = getInput()
while not(inp ==  'FIN'):
    print(inp)
    inp = getInput()
