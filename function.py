def modifico_parametro(x):
    x = 10
a = 2
modifico_parametro(a)
print(a)


def agrego(a, L=[]):
    L.append(a)
    return L
print(agrego(1))
print(agrego(2))
print(agrego(3))


def changeArr(ar):
    ar.append('a')
    return ar

arr =[1,2,3]
print(arr)
changeArr(arr)
print(arr)


# VARIABLES LOCALES Y GLOBALES


x = 12
a = 13
def funcion(a):
    x = 9
    a = 10
funcion(a)
print(a)
print(x)



'''
Las funciones tienen atributos
• **funcion.__doc__: es el docstring**.
• **funcion.__name__**: es una cadena con el nombre la función.
• **funcion.__defaults__**: es una tupla con los valores por defecto de los parámetros opcionales.
'''

print(funcion.__doc__)
print(funcion.__defaults__)
print(funcion.__name__)


i = 4
def funcion(x=i):
    print(x)
i = 10
funcion()