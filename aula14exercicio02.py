empresa = []


i = 0

while i < 2:
    funcionario = []
    funcionario.append(input("Informe o seu nome: "))
    funcionario.append(input("Informe o seu setor: "))
    funcionario.append(float(input("Informe a sua nota da prova escrita: ")))
    funcionario.append(float(input("Informe a sua nota da prova prática: "))) 
    empresa.append(funcionario) 
    i = i + 1
    

i = 0
while i < len(empresa):
    
    print(empresa[i])
    i = i + 1

i = 0
while i < len(empresa):
    soma = (empresa[i][2] + empresa[i][3]) / 2
    if soma >= 7:
        print("Funcionários com nota igual ou acima de 7: ",empresa[i][0])
    i = i + 1
i = 0
setor = input("Informe o setor que deseja verificar: ")
while i < len(empresa):
    if setor == empresa[i][1]:
        print(empresa[i][0])
    i = i + 1 
