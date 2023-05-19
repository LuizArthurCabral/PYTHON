
cont = 0
somatoria = 0
contentre = 0
while cont < 5:
    cont = cont + 1
    compra = float(input("Digite o valor do preço de compra:"))
    venda = float(input("Digite o valor do preço de venda:"))
    lucro = venda - compra
    somatoria = somatoria + lucro
    print("O Lucro da escultura é de:",lucro,"\nA somatória dos lucros é de:",somatoria)
    
    if venda > 20 and venda < 50:
        contentre = contentre + 1
        print("Houveram ",contentre, "vendas entre os valores de R$ 20.00 e R$50.00")
            
