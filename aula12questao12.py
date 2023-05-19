name = []
value = []
i = 0
bigger = []
summedia = 0
cont = 0
while i < 6:
    name.append(input("Informe o nome do aluno: "))
    value.append(int(input("Informe a média do aluno: ")))
    summedia = summedia + value[i]
    i = i + 1
    media = summedia / i
while cont < len(value):
    
    if value[cont] > media:
        bigger.append(name[cont])
    cont = cont + 1


print(media)
print(bigger)
