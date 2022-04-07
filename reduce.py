'''
reduce function
'''


from functools import reduce


lis = [1, 3, 5, 6, 2, ]

# the 3erd paramether it´s optional and is the acumulator initial value
r_list = reduce(lambda a,b:a+b,lis,10)

print(r_list)