lado_1 = int(input("Digite o lado do triangulo: "))
lado_2 = int(input("Digite o lado do triangulo: "))
lado_3 = int(input("Digite o lado do triangulo: "))
if lado_1 > lado_2 and lado_1 > lado_3:
    print(f"O lado 1 é a hipotenusa e os lados 2 e 3 são os catetos.")
elif lado_2 > lado_1 and lado_2 > lado_3:
    print(f"O lado 2 é a hipotenusa e os lados 1 e 3 são os catetos.")
elif lado_3 > lado_2 and lado_3 > lado_1:
    print(f"O lado 3 é a hipotenusa e os lados 1 e 2 são os catetos.")