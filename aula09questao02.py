
option = int(input("Identifique a opção desejada ( 1 - Pode Votar, 2 - Categoria, 3 - Pode Alistar ? , 4 - Encerra programa):"));

while option != 4:
    if option == 1:
        age = int(input("Digite a sua idade: "));
        nationality = input("Digite a sua nacionalidade: ");
        if age >= 16 and (nationality == "Brasileiro" or nationality == "brasileiro"):
            print("Está apto a votar");
        else:
            print("Não está apto a votar");
    elif option == 2:
        age = int(input("Digite a sua idade: "));
        if age <= 11:
            print("Criança");
        elif age >= 12 and age <= 20:
            print("Adolescente");
        elif age >= 31 and age <= 59:
            print("Adulto");
        elif age >= 60:
            print("Idoso");
    elif option == 3:
        gender = input("Informe o seu sexo: ");
        age = int(input("Digite a sua idade: "));
        if age >= 18 and (gender == "Masculino" or gender == "masculino"):
            print("Está apto a se alistar");
        else:
            print("Não está apto a se alistar.");
    option = int(input("Identifique a opção desejada ( 1 - Pode Votar, 2 - Categoria, 3 - Pode Alistar ? , 4 - Encerra programa):"));
            
        

    
