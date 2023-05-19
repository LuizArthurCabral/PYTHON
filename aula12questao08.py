

array = []
i = 0 

value = int(input("Informe um valor: "))
while value != 0:
    array.append(value)

    value = int(input("Informe um valor: "))

while i < len(array):
    if array[i] < 0:
        array[i] = abs(array[i])
    i = i + 1
print(array)
        
