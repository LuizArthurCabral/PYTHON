metro = ""
maiorvalue = 0
valuetotal = 0
valuemin = int(input("Digite o valor mínimo para indenização: "))
metro = float(input("Digite a quantidade de m2 a casa tem em área: "))
while metro != 0: 
    classification = input("Digite a classe da casa (A ou B): ")
    if classification == "A":
        valueind = valuemin + (metro * 500)
        valuetotal = valuetotal + valueind
        print("O valor a ser pago em indenização é de: ",valueind)
    if classification == "B":
        valueind = valuemin + (metro * 300) 
        valuetotal = valuetotal + valueind
        print("O valor a ser pago em indenização é de: ",valueind)
        if valueind > maiorvalue:
            maiorvalue = valueind
            print("Maior valor vendido até agora na classe B: ",maiorvalue)
    metro = float(input("Digite a quantidade de m2 a casa tem em área: "))
print("O valor total gasto pela prefeitura é de: ",valuetotal)
    
