contsim = 0
cont = 0
contnao = 0
erro = 0
pessoas = int(input("Digite quantas pessoas foram ao festival: "))


while cont < pessoas:
    cont = cont + 1
    question = input("Você gostou das apresentações do festival ?")
    if question == "Sim" or question == "sim":
        contsim = contsim + 1
        print("A quantidade de pessoas que gostaram do festival: ",contsim)
    elif question == "Não" or question == "não":
        contnao = contnao + 1
        print("A quantidade de pessoas que não gostaram do festival: ",contnao)
    else:
        erro = erro + 1
        print("Informação não está de acordo com o perguntado")

    if contsim > contnao:
        print("A maioria das pessoas gostaram do festival")
    elif contnao > contsim: 
        print("A maioria das pessoas não gostaram do festival")
    elif contnao == contsim:
        print("A quantidade de pessoas que gostaram do festival é igual às que não gostaram")


