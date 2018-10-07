lista = input()
lista = lista.split(" ")
lista = [int(i) for i in lista]

def maximo(lista):
    maximo = lista[0]
    for x in lista[1:]:
        if x > maximo:
            maximo = x
    return maximo

def suma(lista):
    suma = lista[0]
    for x in lista[1:]:
        suma = suma + x
    return suma

def minimo(lista):
    minimo = lista[0]
    for x in lista[1:]:
        if x < minimo:
            minimo = x
    return minimo

print(suma(lista))
print(minimo(lista))
print(maximo(lista))
