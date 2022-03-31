
'''
Las claves deben ser únicas e inmutables
Las claves pueden ser cualquier tipo inmutable.
Las cadenas y números siempre pueden ser claves.
Las tuplas se pueden usar sólo si no tienen objetos mutables.

claves = musica.keys()
valores = musica.values()
items = musica.items()

• del: permite borrar un par clave:valor
• clear(): permite borrar todo

Otra forma de crear diccionarios
• Podemos usar dict().

'''


notas = {"Janis Joplin":10, "Elvis Presley": 9, "Bob Marley": 5, "Jimi Hendrix": 9 , "charly":10}

print(f'metodo .items()    {notas.items()}')


# add key and value
notas[2]='eppe'

print(notas)
print(notas["charly"])

isCharl = "charl" in notas


# Por comprensión

dicci = dict ([(x, x**2) for x in (2, 4, 6)])

print(f'diccionario por comprension con constructor dict  {dicci}')
