'''
Counter — Contar Objetos Hashables
Un Counter es un contenedor que registra cuántas veces se agregan valores equivalentes. Se puede usar para implementar los mismos algoritmos para los cuales otros lenguajes comúnmente usan una bolsa o una estructuras de conjunto múltiple.

Inicializando
Counter admite tres formas de inicialización. Su constructor se puede llamar con una secuencia de elementos, un diccionario que contiene claves y recuentos, o usando argumentos de palabra clave que mapean nombres cadena a los conteos.


'''



from collections import Counter



#  inicialización
print(Counter(['a', 'b', 'c', 'a', 'b', 'b']))
print(Counter({'a': 2, 'b': 3, 'c': 1}))
print(Counter(a=2, b=3, c=1))


text = 'Counter admite tres formas de inicialización. Su constructor se puede de con una de de elementos, un de que contiene claves y recuentos, o usando argumentos de palabra clave que mapean nombres cadena a los conteos.'

text_splited = text.split(' ')

counter_words = Counter(text_splited)
print(counter_words)

# EL METODO MOST_COMMON DEL COUNTER DEVUELVE UNA LISTA DE TUPLAS CON LOS VALORES MAS SALIDORES
max_repeted=list(counter_words.most_common(1)[0])

 

for word in max_repeted:
    print(type(word))

print(f'la palabra \'{max_repeted[0]}\' aparecio {max_repeted[1]} veces')
