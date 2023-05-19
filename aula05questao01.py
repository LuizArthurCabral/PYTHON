
cont = 0
contnegativo = 0
contzero = 0
contquestion = 0
while cont <= 6:
    cont = cont + 1
    question = int(input("Digite um número: "))
    
    if question > 0:
        contquestion = contquestion + question 
        print("A soma dos valores positivos é igual",contquestion)
    elif question == 0:
        contzero = contzero + 1
        print("Foram digitados ", contzero, "números iguais a zero")
    else:
        contnegativo = contnegativo + 1 
        print("Foram digitados ",contnegativo, "números negátivos")
