a0 = int(input("Digite um início: "))
limite = int(input("Digite o limite: "))
r = int(input("Digite a razão da P.G: "))
anterior = a0
for x in range(a0, limite):
    if x == a0:
        anterior = a0
        if anterior < limite:
            print(anterior, end=" -> ")
    else:
        anterior = anterior * r
        if anterior < limite:
            print(anterior, end=" -> ")
print("O próximo número ultrapassa")