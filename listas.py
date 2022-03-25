'''
Una lista es una colección ordenada de elementos.
Las listas son estructuras heterogéneas, es decir que pueden contener cualquier tipo de
datos, inclusive listas.
Las listas son datos MUTABLES. ¿Qué quiere decir esto?
'''

 


notas = [ 4, 6, 7, 3, 8, 1, 10, 4]


print(len(notas))
print(notas[0])
print(notas[0])


# RECORRIENDO LISTA

for num in notas:
    print(num , end=' ')


# RECORRIENDO LISTA2

count = len(notas)

for indx in range(count):
  print(f'indice numero  {indx}' ,  end= ' ')

print()
# Slicing con listas

lettersList =[]

lettersList.append('f')
lettersList.append('f')
lettersList.append('a')
lettersList.append('d')

print(lettersList[0:1])

print(lettersList)

# Asignación de listas
rock = ["Riff", "La Renga", "La Torr"]
blues = ["La Mississip", "Memphis"]
musica = rock
print(rock)

musica.pop()

print(rock)


print('APPEND EN LAS LISTA INSERTA UN ELEMENTO AL FINAL')

myList =['pepe','pedro','marcela']
print(f'la lista es   {myList}')
myList.append('gracie')
print(f'la lista es   {myList}')

print('PODEMOS COPIAR LOS VALORES DE UNA LISTA A OTRA SIN COPIAR LA REFERENCIA Y MODIFICAR TRANQUILES')
myList =['pepe','pedro','marcela']
myListCopied = myList.copy()

print(myListCopied.pop())



 
