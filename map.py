
'''
map(fun, iter)
Parameters :

fun : It is a function to which map passes each element of given iterable.
iter : It is a iterable which is to be mapped
'''



def doble(x):
  return 2*x
lista = [1, 2, 3, 4, 5, 6, 7]
dobles = list(map(doble, lista))
print(dobles)

print('-'*50)
 

 
# NOTE : The returned value from map() (map object) then can be passed to functions like list() (to create a list), set() (to create a set) .
lista2 = [1, 2, 3, 4, 5, 6, 7]
dobles2 = list(map(doble, lista))
print()


# We can also use lambda expressions with map to achieve above result.

list_numbers = [ 1,2,4,5,6,7,8,5,3,2,4,5,3,1]
doubles3 = list(map(lambda num : num*2 ,list_numbers))
print(doubles3)
 

