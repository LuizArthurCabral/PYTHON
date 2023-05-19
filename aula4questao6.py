permissao = input("O motorista está a usar cinto ? 'S' para sim e 'N' não: ")
permissao2 = input("O motorista está sóbrio ? 'S' para sim e 'N' não: ")
permissao3 = input("O motorista está com o carro com a revisão em dia? 'S' para sim e 'N' não: ")
if permissao == "S" and permissao2 == "S" and permissao3 == "S":
     print("O motorista está em condição de dirigir")
else:
    print("O motorista não está em condição de dirigir")
