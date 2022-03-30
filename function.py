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