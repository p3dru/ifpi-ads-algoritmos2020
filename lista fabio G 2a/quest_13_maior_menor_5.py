def calc_maior(x, y, z, a, b):
    maior = 0
    if maior < x:
        maior = x
        if maior < y:
            maior = y
            if maior < z:
                maior = z
                if maior < a:
                    maior = a
                    if maior < b:
                        maior = b
    return maior

def calc_menor(x, y, z, a, b):
    menor = x
    if menor > y:
        menor = y
    if menor > z:
        menor = z
    if menor > a:
        menor = a
    if menor > b:
        menor = b
    return menor


numero_1 = int(input("Digite um número: "))
numero_2 = int(input("Digite um número: "))
numero_3 = int(input("Digite um número: "))
numero_4 = int(input("Digite um número: "))
numero_5 = int(input("Digite um número: "))
maior = calc_maior(numero_1, numero_2, numero_3, numero_4, numero_5)
menor = calc_menor(numero_1, numero_2, numero_3, numero_4, numero_5)
print(f"O maior número lido é o {maior} e o menor é {menor}")