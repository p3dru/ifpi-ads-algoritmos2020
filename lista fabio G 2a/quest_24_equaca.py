def cal_delta(x, y, z):
    delta = (y ** 2) - (4 * x * z)
    return delta

def calcular_raiz_1(x, y):
    raiz_1 = (-(y) + (delta ** 0.5)) / (2 * x)
    return raiz_1

def calcular_raiz_2(x, y):
    raiz_2 = (-(y) - (delta ** 0.5)) / (2 * x)
    return raiz_2


a = int(input("Digite o valor de A: "))
b = int(input("Digite o valor de B: "))
c = int(input("Digite o valor de C: "))
if a != 0:
    delta = cal_delta(a, b, c)
    if delta > 0:
        raiz_1 = calcular_raiz_1(a, b)
        raiz_2 = calcular_raiz_2(a, b)
        print(f"As raizes da equação são {raiz_1} e {raiz_2}")
    elif delta == 0:
        raiz_1 = calcular_raiz_1(a, b)
        print(f"A equação possui apenas uma raiz real que é {raiz_1}")
    else:
        print("A função não possui raiz")