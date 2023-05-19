array = []
i = 0
listaA = []
listaB = []
while i < 20:
    array.append(int(input("Informe um número: ")))
    if array[i] % 2 == 0:
        listaA.append(array[i])

    if array[i] % 2 == 1:
        listaB.append(array[i])

    i = i + 1
print(array)
print(listaA)
print(listaB)
