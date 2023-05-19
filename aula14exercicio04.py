array = []

option = input("Vamos iniciar? ")
i = 0
while option != "Não":
    flowers = []
    flowers.append(i)
    flowers.append(input("Informe o nome da flor: "))
    flowers.append(float(input("Informe o valor da unidade da flor: ")))
    array.append(flowers)
    option = input("Deseja continuar? ")
    i = i + 1

i = 0
bigger = 0

while i < len(array):
    print("Flor: ",array[i][0],"\nNome:",array[i][1],"\nPreço da unidade:",array[i][2])
    value = 12 * array[i][2]
    print("-----------------------------------------------------------------------------")
    print(array[i][0],"- Nome:",array[i][1],"- o valor do buquê com 12 flores:",value)
    print("-----------------------------------------------------------------------------")
    if value > bigger:
        bigger = value
        name = array[i][1]
    i = i + 1

print("Valor da flor mais cara: ",bigger,"\nNome da flor: ",name)
