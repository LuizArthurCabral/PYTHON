cont = 0

while cont < 10:
    cont = cont + 1
    classe = input("Digite a classe de iluminação do cômodo: ")
    medida = float(input("Digite a medida do cômodo em metros quadrados: "))
    if classe == "A" or classe == "a": 
      potencia = 15 * medida
      lampadas = potencia // 60 
      print("A potência necessária para iluminar o cômodo é de: ",potencia)
      print("A quantidade de lâmpadas necessárias para iluminar o ambiente: ",lampadas)
    elif classe == "B" or classe == "b":
        potencia = 18 * medida
        lampadas = potencia // 60
        print("A potência necessária para iluminar o cômodo é de: ",potencia)
        print("A quantidade de lâmpadas necessárias para iluminar o ambiente: ",lampadas)
    elif classe == "C" or classe == "c":
        potencia = 20 * medida
        lampadas = potencia // 60
    else:
        print("Os dados não estão de acordo com o perguntado!")
