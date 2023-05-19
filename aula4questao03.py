sexo = input("Digite o seu sexo 'F'-feminino ou 'M'-Masculino: ")
turno = input("Digite o seu turno ‘M’ – Matutino ou ‘V’ – Vespertino): ")
if sexo == "M" and turno == "M":
    print("Bom dia,querido!")
elif sexo == "M" and turno == "V":
    print("Boa tarde,querido")
elif sexo == "F" and turno == "M":
    print("Bom dia,querida")

elif sexo == "F" and turno == "V":
    print("Boa tarde,querida")
else:
    print("Faltam dados")
