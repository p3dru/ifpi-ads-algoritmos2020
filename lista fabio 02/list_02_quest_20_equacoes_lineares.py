#entrada
a = int(input("Digite o valor de a: "))
b = int(input("Digite o valor de b: "))
c = int(input("Digite o valor de c: "))
d = int(input("Digite o valor de d: "))
e = int(input("Digite o valor de e: "))
f = int(input("Digite o valor de f: "))
#processamento
x = (((c * e) - (b * f)) / ((a * e) - (b * d)))
y = (((a * f) - (c * d)) / ((a * e) - (b * d)))
#saida
print(f"Os valores para x e y respectivamente são {x}, {y}")