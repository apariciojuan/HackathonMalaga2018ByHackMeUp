cantidad = input()

lista = []
for x in range(0,int(cantidad)):
    dato = input()
    lista.append(dato.split(" "))

lista2 = []
nombre = ""

for y in range(int(cantidad)):
    for x in range(len(lista[y]) -1):
        #esto es porque me ponia 2 espacios entre el monto y el numero, los test daban error
        if x == len(lista[y]) -2:
            nombre += str(lista[y][x])
        else:
            nombre += str(lista[y][x]) + " "

    lista2.append([nombre, lista[y][x +1]])
    nombre = ""

dic = {}

for x in lista2:
    if x[0] in dic:
        dic[x[0]] += int(x[len(x) -1])
    else:
        dic[x[0]] = int(x[len(x) - 1])

for key, value in dic.items():
    print(key, value)