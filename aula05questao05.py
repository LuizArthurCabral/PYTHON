

cont = 0

while cont < 30:
    cont = cont + 1 
    name = input("Digite o nome do aluno: ")
    nota1 = float(input("Digite a primeira nota: "))
    nota2 = float(input("Digite a segunda nota: "))
    media = (nota1 + nota2)/ 2
    if media > 0 and media < 10:
        print("As notas estão válidas \nA média do aluno é", media)
        if media >= 6:
            print("O aluno está classificado")
        else:
            print("Aluno desclassificado")
    else:
        print("As notas são inválidas")
