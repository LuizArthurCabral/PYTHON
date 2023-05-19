cont = 0



while cont < 50:
     cont = cont + 1
     quantity = int(input("Digite a quantidade presente em estoque: "))
     price = float(input("Digite o preço de custo do produto: "))
     sale  = float(input("Digite o preço de venda do produto: "))
     lucro = sale - price
     lucrototal = quantity * lucro 
     print("O lucro sobre o produto é de: ",lucro)
     print("Caso todo o estoque seja vendido,o lucro total será de",lucrototal)
