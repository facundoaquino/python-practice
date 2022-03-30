'''
Un conjunto es una colección de datos heterogéna, desordenada, NO indexada y sin
elementos duplicados.

Operaciones con conjuntos
• Pensemos en las operaciones matemáticas sobre conjuntos:
 in: retonar si un elemento pertenece o no a un conjunto.
 |: unión entre dos conjuntos.
 &: intersección entre dos conjuntos.
 -: diferencia de conjuntos.

 Para crear un conjunto, basta con encerrar una serie de elementos entre llaves {}, o bien usar el constructor de la clase set() y pasarle como argumento un objeto iterable (como una lista, una tupla, una cadena …).

Para añadir un elemento a un conjunto se utiliza el método add(). También existe el método update(), que puede tomar como argumento una lista, tupla, string, conjunto o cualquier objeto de tipo iterable
'''


unSet = {'pepe'}
print(unSet)

otherSet = set('anything')
print(otherSet)


bandas_nacionales = set(("Soda Stéreo", "La Renga"))
print(bandas_nacionales)

bandas_internacionales = set(["Greta Van Fleet", "Led Zeppelin"])
print(bandas_internacionales)