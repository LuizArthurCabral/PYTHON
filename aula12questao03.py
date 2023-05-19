array = [10, 5, 8, 20, 50, 10, 5, 8, 8 ,60 ,10, 5, 5, 3, 50]
cont = 0
bigger = 0
sumvalue = 0
contposition = 0
while cont < len(array):
    if array[cont] > bigger:
        bigger = array[cont]
    if array[cont] >= 1:
        sumvalue = sumvalue + array[cont]


    cont = cont + 1 
print(bigger)
print(sumvalue)
print(array[0])
print(array[1])
print(array[2])
print(array[3])
print(array[4])
while contposition < len(array):
    if array[contposition] % 2 == 0:
        print(contposition)
    contposition = contposition + 1

