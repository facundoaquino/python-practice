'''
Necesitamos procesar las notas de los estudiantes de este curso. Queremos
saber:
• cuál es el promedio de las notas;
• cuántos estudiantes están por debajo del promedio.
'''
 

notas = [ 4, 6, 7, 3, 8, 1, 10, 4]

promedio = 0
cantidadNotas = len(notas)
sum=0

for nota in notas:
    sum+=nota
print(f'todas las notas suman  {sum}')

promedio=sum/cantidadNotas

print(f'el promedio es   {promedio}')


debajoDelPromedio=0

for nota in notas:
    if nota<promedio:
        debajoDelPromedio+=1


print(f'Estudiantes debajo del promedio  {debajoDelPromedio}')


