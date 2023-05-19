lado1 = int(input("Digite o comprimento do primeiro lado: "))
lado2 = int(input("Digite o comprimento do segundo lado: "))
lado3 = int(input("Digite o comprimento do terceiro lado: "))
if lado1 == lado2 and lado2 == lado3:
    print("A figura é um triângulo equilátero")
elif lado1 == lado2 and lado3 != lado1:
    print("A figura é um triângulo isósceles")
elif lado1 == lado3 and lado2 != lado3:
    print("A figura é um triângulo isósceles")
elif lado2 == lado3 and lado1 != lado2:
    print("A figura é um triângulo isósceles")
else:
    print("A figura é um triângulo escaleno")
