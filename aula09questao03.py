qtwage = 0
qt = 0
smaller = 999999999
smallerman = ""
maxsale = 2512
vendedor = input("Digite o nome do vendedor: ");
while vendedor != "Sair":
    wage = int(input("Digite o valor do salário do funcionário: "));
    quantity = int(input("Digite a quantidade de camisetas vendidas pelo funcionário: "));
    if quantity > 2512:
        print("Erro");
    else: 
        value = wage + (quantity *  0.5);
        qt = qt + quantity
        qtwage = qtwage + value
    if value <= 1000:
        print("O ", vendedor, " está na categoria A e o valor a ser recebido por ele é de: ",value);

    elif value > 1000 and value <= 1500:
        print("O ", vendedor, " está na categoria B e o valor a ser recebido por ele é de: ",value);

    elif value > 1500 and value <= 2000:
        print("O ", vendedor, " está na categoria C e o valor a ser recebido por ele é de: ",value);

    elif value > 2000:
        print("O ", vendedor, " está na categoria D e o valor a ser recebido por ele é de: ",value);        
        
    

    if smaller > quantity:
        smaller = quantity
        smallerman = vendedor
    vendedor = input("Digite o nome do vendedor: ");
print("O total gasto com o pagamento do salário dos vendedores foi de: ",qtwage);
print("O vendedor que vendeu a menor quantidade de camisetas é ",smallerman," e a quantidade de camisetas vendidas é: ",smaller);
