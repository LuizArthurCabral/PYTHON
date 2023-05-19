array = []
i = 0
while i < 3:
    value = []
    value.append(i)
    value.append(float(input("Informe a nota do usuário: ")))
    value.append(float(input("Informe a segunda nota do usuário: ")))
    value.append(float(input("Informe a terceira nota do usuário: ")))
    
    array.append(value)
    i = i + 1

i = 0
array2 = []
while i < len(array):
    soma = []
    nota = array[i][1] + array[i][2] + array[i][3]
    soma.append(array[i][0])
    soma.append(nota)
    array2.append(soma)
    print(array[i])
    i = i + 1
i = 0
bigger = 0
while i < len(array2):
    if array2[i][1] > bigger:
        bigger = array2[i][1]
        code = array2[i][0]
    print(array2[i])
    i = i + 1
print("O partcipante vencedor é o: ",code)
