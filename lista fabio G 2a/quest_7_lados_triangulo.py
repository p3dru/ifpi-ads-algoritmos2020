lado_1 = int(input("Digite um lado: "))
lado_2 = int(input("Digite outro lado: "))
lado_3 = int(input("Digite mais um lado: "))
if (lado_1 + lado_2) > lado_3 and (lado_3 + lado_2) > lado_1 and (lado_1 + lado_3) > lado_2 and lado_2 != 0 and lado_1 != 0 and lado_3 != 0:
    print("Forma um triângulo")
    if lado_3 == lado_1 == lado_2:
        print("E é equilátero.")
    elif lado_2 == lado_1 or lado_2 == lado_3 or lado_1 == lado_3:
        print("E é isosceles.")
    elif lado_3 != lado_1 != lado_2:
        print("E é escaleno.")
else:
    print("Não forma triângulo.")