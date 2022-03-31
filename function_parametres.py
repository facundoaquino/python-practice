def imprimo(*args):
    """ Esta función imprime los argumentos y sus tipos"""
    # args es una tupla que representa a los parámetros pasados.
    print(f'args:  {args}')
    
    for valor in args:
      print(f"{valor} es de tipo {type(valor)}")

imprimo('2323',2323,(1,2))    


def imprimo_muchos_valores(mensaje_inicial, *en_otro_idioma, **en_detalle):
  print("Mensaje original")
  print(mensaje_inicial)
  print("\nEn otros idiomas")
  print("-" * 40)
  for val in en_otro_idioma:
    print(val)
  print("\nEn detalle")
  print("-" * 40)
  for clave,word in en_detalle.items() :
   print(f"{clave}: {word}")
  print("\nFuente: traductor de Google. ")
imprimo_muchos_valores("Hola",
"hello", "Hallo", "Aloha ", "Witam", "Kia ora",
ingles= "hello",
aleman="Hallo",
hawaiano="Aloha",
polaco="Witam",
maori="Kia ora")


def imprimo_otros_valores(**kwargs):
    for clave, valor in kwargs.items():
        print(f"{clave} es {valor}")


imprimo_otros_valores(banda1='Nirvana', banda2="Foo Fighters", banda3="AC/DC")


def imprimo_contacto(nombre, celu):
    # print(type(celu))
    print(nombre, celu)


contacto = {"nombre": "Messi", "celu": 12345}
imprimo_contacto(**contacto)