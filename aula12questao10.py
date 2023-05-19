array = []
i = 0
indice = 0
quantity = 0
small = 99999999
sumvalue = 0

while i < 20:
    array.append(int(input("Informe um valor : ")))  
    


    if array[i] % 2 == 0:
        quantity = quantity + 1

    if array[i] < small:
        small = array[i] 
    i = i + 1
    
while indice < 10:
    sumvalue = sumvalue + array[indice]
    indice = indice + 1
print(array)        
print("A quantidade de números pares: ",quantity)
print("A soma dos 10 primeiros elementos: ",sumvalue)
        
