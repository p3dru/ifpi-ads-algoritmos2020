a0 = int(input("Digite o valor inicial: "))
limite = int(input("Digite o limite: "))
r = int(input("Digite a razão: "))
for x in range(a0, limite, r):
    if x <= limite - r:
        print(x, end=" -> ")
    else:
        print(x)
