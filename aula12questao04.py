array = [10, 5, 8, 20, 50, 10, 5, 8, 8, 60, 10, 5, 5, 3, 50]
cont = 0
qt = 0
option = input("Vamos iniciar?")
while option != "Não":
    identify = int(input("Informe um número: "))
    while cont < len(array):
        if array[cont] == identify:
            qt = qt + 1
        cont = cont + 1 
    option = input("Vamos continuar? ")
print("O número aparece: ",qt)
