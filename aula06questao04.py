
cont = 0
value = 0
old = 0
contsim = 0
contnao = 0

while cont < 1000:
    cont = cont + 1
    age = int(input("Digite a sua idade: "))
    info = input("Digite a informação presente na sua carteirinha: ")
    card = int(input("Digite o valor da entrada inteira: "))
    if age < 18:
        print("Menor de idade não pode participar do show")
    elif age > 18 and (info == "Sim" or info == "sim"):
        contsim = contsim + 1 
        metade = card / 2
        value = value + metade
        old = (old + age) / cont
        
        print("Pode participar do show e como possui carteirinha paga meia entrada\nValor a ser pago: ",metade)
        
    else:
        contnao = contnao  + 1 
        value = value + card
        print("Pode participar, porém pagará entrada inteira.nValor a ser pago: ",card)

        

print("A média das idade das pessoas que pagaram meia ",old)
print("O valor total arrecadado na bilheteria", value)
if contsim > contnao:
        print("Mais pessoas pagaram meia entrada do que inteira. \nTotal de pessoas que pagaram meia: ",contsim)

elif contnao > contsim:
        print("Mais pessoas pagaram a inteira\nTotal de pessoas que compraram inteira: ",contnao)
else:
        print("As quantidade de pessoas que compraram entrada inteira é a mesma de pessoas que pagaram meia")
