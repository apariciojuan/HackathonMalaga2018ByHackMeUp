dato=input()

lista = [] #lista de letras
for x in range(ord("a"), ord("z")+1):
    lista.append(chr(x))

sublista = lista[0:int(dato)]
sublista = sublista[::-1] #invertimos el orden

filas = int(dato) -1
rango = 1
listaInversa = [] #guarda las salidas para imprimir la parte invertida

for x in range(0,len(sublista)):
    if int(dato) == 1:
        print ("-a-")
        break
    else:
        linea = "--" * (filas)
        derecha = ""
        izquierda = ""

        for c in range(0,rango):
            if c == rango or c == 0:
                izquierda = izquierda + sublista[c]
            else:
                izquierda = izquierda + "-"+ sublista[c]

        for v in reversed(range(0, rango -1)):
            derecha = derecha + "-"+sublista[v]

        salida = linea+izquierda+derecha+linea
        filas = filas - 1
        rango = rango +1

    listaInversa.append(salida)
    print(salida)

#imprime la parte invertida
for x in reversed(listaInversa[:-1:]):
    print(x)