datos = input()
datos = list(datos)
alumnos = datos[0]
asignaturas = datos[2]

lista = []

for y in range(0,int(asignaturas)):
    notas = input()
    lista.append(notas.split(" "))

for x in range(int(alumnos)):
    media = 0
    for y in range(int(asignaturas)):
        media += float(lista[y][x])

    media = media / int(asignaturas)

    #Para ver los 2 difitos a la derecha aunque sean cero
    print("%.2f" % round(media, 2))

