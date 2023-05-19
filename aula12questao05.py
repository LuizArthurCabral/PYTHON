array = [-5, 10, -8, -3, 5, 10, 11, 8, -9, 10, -6]

cont = 0
positivos = []
negativos = []
contnum = 0
contarray = 0  
while cont < len(array):
    if array[cont] >= 1:
        positivos.append(array[cont])
        
    else:
        negativos.append(array[cont])
    cont = cont + 1 
print("Positivos")    
while contarray < len(positivos):
    print(positivos[contarray])
    contarray = contarray + 1

print("Negativos")
while contnum < len(negativos):
    print(negativos[contnum])
    contnum = contnum + 1 
 




    
