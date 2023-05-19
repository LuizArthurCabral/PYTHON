
cont = 0
arrays = []
soma = 0

while cont < 6:
    arrays.append(int(input("Informe um número: ")))
    
    if arrays[cont] % 2 == 0:
        soma = soma + arrays[cont]
    cont = cont + 1
    
contarray = 0
while contarray < len(arrays):
    print(arrays[contarray])
    contarray = contarray + 1 
print(arrays[0])
print(arrays[1])
print(arrays[2])
print(soma)
