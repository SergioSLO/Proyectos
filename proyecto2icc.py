from sklearn import datasets
import cv2

#Función de ordenamiento

def insertion_sort(lista):
    n = len(lista)

    for i in range(1, n):
        key = lista[i]
        j = i - 1

        while j >= 0 and lista[j][1] > key[1]:
            lista[j + 1] = lista[j]
            j -= 1

        lista[j + 1] = key

#Se carga la data
digits = datasets.load_digits()
#Data registrado de dataset de sklearn

promedios = [[[0 for x in range(9)] for j in range(9)] for i in range(10)]
sumas = [[[0 for x in range(9)] for j in range(9)] for i in range(10)]

#Se inicializa las matrices de promedios
for i in range(10):
    for j in range(9):
        promedios[i][j][8] = i


print(len(digits.target))
print(len(digits.images))

#Obtención de las matrices de promedios
for i in range(len(digits.images)):
    numero = digits.target[i]
    for j in range(8):
        for x in range(8):
            promedios[numero][j][x] += int(digits.images[i][j][x])
            sumas[numero][j][x] += 1

for i in range(10):
    for j in range(8):
        for x in range(8):
            promedios[i][j][x] = int(promedios[i][j][x]//sumas[i][j][x])


# for i in range(10):
#     for j in range(9):
#         for x in range(9):
#             print(promedios[i][j][x], end=",")
#         print()

#Procesado de imagenes

print("\nProcesado de imagen:")
Ruta = input("Ingrese la ruta de la imagen:")
img_array = cv2.imread(Ruta, cv2.IMREAD_GRAYSCALE)
nueva_img = cv2.resize(img_array, (8,8))

for i in range(len(nueva_img)):
    for j in range(len(nueva_img[i])):
        nueva_img[i][j] = 255 - nueva_img[i][j]


for i in range(len(nueva_img)):
    for j in range(len(nueva_img[i])):
        nueva_img[i][j] = nueva_img[i][j]*16/255

print()
print(nueva_img)

#Analisis de la computadora

print("\nAnalisis de la computadora:")
distancias = []

for i in range(len(digits.images)):
    lista = [i,0]
    for j in range(8):
        for x in range(8):
            dif = nueva_img[j][x] - digits.images[i][j][x]
            lista[1] += dif**2
    lista[1] = lista[1]**0.5
    distancias.append(lista)

insertion_sort(distancias)
print("Pos\tDistancia\t\t Target")
for i in range(3):
    print(distancias[i][0], "  ",distancias[i][1], "\t",digits.target[distancias[i][0]])

uno = digits.target[distancias[0][0]]
dos = digits.target[distancias[1][0]]
tres = digits.target[distancias[2][0]]
if uno == dos and dos == tres:
  print("\nSoy la inteligencia artificial, y estoy 100% seguro que el digito ingresado corresponde al numero", uno)
elif uno == dos:
  print("\nSoy la inteligencia artificial, y creo que el digito ingresado corresponde al numero", uno)
elif tres == dos:
  print("\nSoy la inteligencia artificial, y creo que el digito ingresado corresponde al numero", dos)
elif uno == tres:
  print("\nSoy la inteligencia artificial, y creo que el digito ingresado corresponde al numero", uno)
else:
  print("\nLo más parecido es un", uno)

#Analisis de las distancias con el promedio

print("\nAnalisis de los promedios:")
distancias = []

for i in range(len(promedios)):
    lista = [i,0]
    for j in range(8):
        for x in range(8):
            dif = nueva_img[j][x] - promedios[i][j][x]
            lista[1] += dif**2
    lista[1] = lista[1]**0.5
    distancias.append(lista)

insertion_sort(distancias)
print("Pos\tDistancia\t\t Target")
print(distancias[0][0], "  ",distancias[0][1], "\t",digits.target[distancias[0][0]])
