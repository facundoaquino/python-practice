'''
The primary difference between the list sort() function and the sorted() function is that the sort() function will modify the list it is called on. The sorted() function will create a new list containing a sorted version of the list it is given. The sorted() function will not modify the list passed as a parameter.
'''


def ordeno1(cadena="ss"):
  """ Implementación usando sort"""
  lista = cadena.split()
  lista.sort(key=str.lower)
#lista.sort()
  return lista


print(ordeno1("Hoy puede ser un gran día. "))  


# Otra posible solución
def ordeno2(cadena):
    """ Implementación usando sorted"""
    lista = cadena.split()
    return sorted(lista, key=str.lower)
print(ordeno2("Hoy puede ser un gran día. "))