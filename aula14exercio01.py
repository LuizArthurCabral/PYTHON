listaVasos = [["V01",100.00,50.00],["V02",80.00,25.00],["V03",110.00,60.00],["V04",230.00,100.00],["V05",25.00,30.00]]
i = 0
while i < len(listaVasos):
    soma = listaVasos[i][1] + listaVasos[i][2]
    listaVasos[i].append(soma)
    i = i + 1

i = 0
#while i < len(listaVasos):
 #   print(listaVasos[i][0], listaVasos[i][3])
  #  i = i + 1
i = 0
soma = 0 
while i < len(listaVasos):
    soma = soma + listaVasos[i][3]
    i = i + 1
    media = soma / i

i = 0
while i < len(listaVasos):
    if listaVasos[i][3] < media:
        print(listaVasos[i][0])
    i = i + 1 
