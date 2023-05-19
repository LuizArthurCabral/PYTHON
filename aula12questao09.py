array = []
cont = 0
i = 0
indice = 0
indice2 = 5
while cont < 10:
    array.append(float(input("Informe o número que deseja inserir: ")))

    cont = cont + 1

print(array)


while i < len(array):
    while indice < 5:
        array[indice] = array[indice] * 2
        indice = indice + 1

    while indice2 < 10:
        array[indice2] = array[indice2] / 2
        indice2 = indice2 + 1
    i = i + 1

print(array)
