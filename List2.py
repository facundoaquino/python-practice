'''
Las listas se pueden concatenar (+) y repetir (*)
'''

import string


rock = ["Riff", "La Renga", "La Torre"]
blues =["La Mississippi", "Memphis"]
musica = rock + blues
mas_rock = rock * 3
print(musica)

print(mas_rock)


# ///////////////////////////


lista = [[1,2]] * 3
print(lista)

lista [0][1] = 'cambio'
print(lista)


# /////////////////

lista = [[1,2], 8, 9]
lista2 = lista.copy()
print(id(lista), id(lista2))


# count

letters = ['a','t','g','a']
print(letters.count('o'))

# listas por comprension
# ord devuelve el codigo unicode
digitos = string.digits
codigos = [ord(n) for n in digitos]
print(codigos)


lst  =  [x ** 2  for x in range (1, 11)   if  x % 2 == 1] 
print(f'lista por comprension de los cuadrados de impares de 1 a 9  {lst}')
