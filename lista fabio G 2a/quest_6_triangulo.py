angulo_1 = int(input("Digite um ângulo: "))
angulo_2 = int(input("Digite outro ângulo: "))
angulo_3 = int(input("Digite mais um ângulo: "))
soma = angulo_1 + angulo_2 + angulo_3
if soma == 180 and angulo_1 != 0 and angulo_2 != 0 and angulo_3 != 0:
    print("É possível formar um triângulo.")
    if angulo_3 < 90 and angulo_2 < 90 and angulo_1 < 90:
        print("Forma um triângulo acutângulo.")
    elif angulo_3 == 90 or angulo_2 == 90 or angulo_1 == 90:
        print("Forma um triângulo retângulo.")
    elif angulo_3 > 90 or angulo_2 > 90 or angulo_1 > 90:
        print("Forma um triângulo obtusângulo.")
else:
    print("Não é possível formar um triângulo.")