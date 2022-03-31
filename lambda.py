'''


¿Qué son las expresiones lambda?
• Son funciones anónimas.
lambda parametros : expresion

'''


def ordeno3(usuarios):
  """ Usamos sorted con una expresión lambda"""
  return sorted(usuarios, key=lambda usuario: usuario[0])
usuarios = [
('JonY BoY', 'Nivel3', 15),
('1962', 'Nivel1', 12),
('caike', 'Nivel2', 1020),
('Straka^', 'Nivel2', 1020),
]
print(ordeno3(usuarios))

print('-'*50)

lista_de_acciones = [lambda x: x * 2, lambda x: x * 3]
print(f'los tipos de datos lambda son  {type(lista_de_acciones[0])}')

param = 4
for accion in lista_de_acciones:
  print(accion(param))