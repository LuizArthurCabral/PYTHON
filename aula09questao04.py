import random
qt = 0
option = input("Vamos iniciar o jogo ?");

while option == "Sim":
    luck = random.randint(0,100)
    value = int(input("Chute um número: "));
    qt = qt + 1
    if value > luck:
        print("O valor digitado é maior que o valor correto. ");
    elif value < luck:
        print("O valor informado é menor que o valor correto. ");
    while value != luck:
        value = int(input("Chute um número: "));
        qt = qt + 1
        if value > luck:
            print("O valor digitado é maior que o valor correto. ");
        elif value < luck:
            print("O valor informado é menor que o valor correto. ");
    print("Parabéns!!,o número correto é: ",luck);
    print("Quantidade de tentativas: ",qt);
    option = input("Vamos jogar novamente ?");
    
        
    
    
