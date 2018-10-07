import re
datos = input()

#filtramos solo caracteres por medio de una Expresion Regular
pattern = re.compile(r'[a-zA-Z]*')
dd = re.findall(pattern, datos)

#string de minusculas
letras = "".join(dd).lower()
letrasEnLista = list(letras)

#Eliminamos elementos repetidos y lo hacemos lista
letrasEnLista = list(set(letrasEnLista))

#ordenamos sin repetidas y ya en minusculas
letrasEnLista.sort()

#imprimimos el string
print("".join(letrasEnLista))

cantidad = len(letrasEnLista)
inicio = 1
salida = ""

for x in range(0,cantidad):
    for y in range(inicio,cantidad):
        salida = salida + (letrasEnLista[x] + letrasEnLista[y] ) +" "
    inicio = inicio + 1

print(salida)


