value1 = int(input("Digite o primeiro valor: "))
value2 = int(input("Digite o segundo valor: "))
value3 = int(input("Digite o terceiro valor: "))
if value1 != 0 and value2 != 0 and value3 != 0:
    if value1 > 0 and value2 > 0 and value3 > 0:
        produto = value1 * value2 * value3
        print("O produto dos números é:", produto)
    elif value1 > 0 or value2 > 0 or value3 > 0:
        soma = value1 + value2 + value3
        print("A soma dos números é: ",soma)
    else:
        media = (value1 + value2 + value3) / 3
        print("A média dos valores é: ",media)
    if value1 == 0 and value2 == 0 and value3 == 0:
        print("Todos os valores são iguais a zero")
    else:
        if value1 == 0 and value2 == 0:
            print("O primeiro e o segundo valor iguais a zero")
        elif value2 == 0 and value3 == 0:
            print("O segundo e o terceiro valor são iguais a zero")
        elif value1 == 0 and value3 == 0:
            print("O primeiro e o terceiro valor são iguais a zero")
        
            
