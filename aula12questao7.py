array = []

i = 0
cont = 0
while i < 10:
    array.append(int(input("Informe um número: ")))


    i = i + 1
while cont < len(array):   
    if array[9]:
        array[9] = array[0]
    cont = cont + 1
            
print(array[9])        

