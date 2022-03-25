'''
Las listas se pueden concatenar (+) y repetir (*)
'''

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