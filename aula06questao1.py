cont = 0

contimpares = 0 
contpares = 0
contpositivos = 0
soma = 0
while cont < 10:
    cont = cont + 1 
    value1 = int(input("Digite um número: "))
    
    antecessor = value1 - 1
    sucessor = value1 + 1
    print("O antecessor do número é: ",antecessor)
    print("O sucessor ao número é: ",sucessor)
    if value1 % 2 == 0 and value1 > 0 and value1 > 50 :
        contpares = contpares + 1
    elif value1 % 2 == 1:
        contimpares = contimpares + 1
        soma = soma + value1
        
    if value1 > 0:
        contpositivos = contpositivos + 1
        percentual = contpositivos * 100 / 10

print("A a quantidade de números pares, positivos e maiores que 50: ",contpares)
print("A quantidade de números ímpares: ",contimpares)
print("A soma de todos os números ímpares é: ",soma)



print("O percentual de números positívos é de: ",percentual)
