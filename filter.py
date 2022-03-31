

'''
The filter() method filters the given sequence with the help of a function that tests each element in the sequence to be true or not.


'''


from os import sep


def esImpar(num):
    return num % 2 != 0

list_numbers = [2,3,4,5,1,23,43,13,76,3]

impares = list(filter (esImpar,list_numbers))
print(f'imapres  {impares}')

print('-'*50)

impares2= list(filter(lambda n : n%2 !=0 , list_numbers))
print(impares2)
 