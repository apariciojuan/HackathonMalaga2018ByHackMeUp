datos = input()

numero = datos[0]
repetidos = 0

for x in datos:
    if numero == x:
        repetidos = repetidos +1
    else:
        salida = "("+str(numero)+", "+str(repetidos)+")"
        print(salida)
        numero = x
        repetidos = 1
        
salida = "("+str(numero)+", "+str(repetidos)+")"
print(salida)
