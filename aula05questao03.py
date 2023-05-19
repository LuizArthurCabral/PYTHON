cont = 0
contidade = 0
contnacional = 0
contidosos = 0
contitaly = 0
contfrench = 0



while cont < 6:
    cont = cont + 1
    idade = int(input("Digite a sua idade: "))
    nacionalidade = input("Digite a sua nacionalidade: ")
    sexo = input("Digite o seu sexo: ")
    if nacionalidade == "Brasileira" and idade > 20 and idade < 30 and sexo == "Masculino":
        contnacional = contnacional + 1
        print("Foram digitados ",contnacional," homens de nacionalidade Brasileira e com idade de entre 20 a 30 anos")
    elif idade >= 65 and nacionalidade == "Brasileira":
        contidosos = contidosos + 1
        print("Foram digitados ",contidosos,"idosos de nacionalidade Brasileira")
    elif idade >= 65 and nacionalidade == "Italiano":
        contitaly = contitaly + 1
        print("Foram digitados ",contitaly,"idosos de nacionalidade italiana")
    
    elif idade >= 65 and nacionalidade == "Francês":
        contfrench = contfrench + 1
        print("Foram digitados ",contfrench,"idosos de nacionalidade francesa")
    else:
        contidade = contidade + idade
        media = contidade / cont
        print("A média das idades é de:", media)
