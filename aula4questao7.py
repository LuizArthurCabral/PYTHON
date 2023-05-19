profissao = input("Digite qual é a sua profissão ?")
opcao = input("Você deseja participar dos minicursos ?")
traducao = input("Deseja tradução simultânea ?")




if profissao == "Estudante" or profissao == "Professores":
        ingresso = 100
        minicurso = 50
        simultanea = 20
        
        if opcao == "Sim" and traducao == "Sim":
        
            valor = ingresso + minicurso + simultanea
            print("O valor total é: ",valor)
        elif opcao == "Sim" and traducao == "Não":
            valor = ingresso + minicurso
            print("O valor total é: ",valor)
        elif opcao == "Não" and traducao == "Sim":
            valor = ingresso + simultanea
            print("O valor total é: ",valor)

        else:
            ingresso = 100
            print("O valor total é: ",ingresso)
else:

        ingresso = 150
        minicurso = 50
        simultanea = 20

        if opcao == "Sim" and traducao == "Sim":

            valor = ingresso + minicurso + simultanea
            print("O valor total é: ",valor)
        elif opcao == "Sim" and traducao == "Não":
            valor = ingresso + minicurso
            print("O valor total é: ",valor)
        elif opcao == "Não" and traducao == "Sim":
            valor = ingresso + simultanea
            print("O valor total é: ",valor)
        else:
            ingresso = 150
            print("O valor total é: ",ingresso)
