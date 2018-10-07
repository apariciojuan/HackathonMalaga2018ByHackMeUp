dato=input()
filas = int(dato) +1
rango = 2

for x in range(1,filas):
    if dato == 1:
        print ("1")
        break
    else:
        linea = "-" * (filas - 2)
        derecha = ""
        izquierda = ""

        for c in range(1,rango):
            derecha = derecha + str(c)

        for v in range(rango -2, 0, -1):
            izquierda = izquierda + str(v)

        salida = linea+derecha+izquierda+linea
        filas = filas - 1
        rango = rango +1
        print(salida)

"""

n = int(input())
l = range(n)


cadena  = " "
for i in range(1,n):
    for j in range(n - i):
          print(" ", end=" ")
    for j in range(1, i):
          print(j, end=" ")
    for j in range( i, 0, -1 ):
          print(j, end=" ")
    print("\n")
"""
