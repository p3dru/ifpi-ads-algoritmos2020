numero = int(input("Digite o número para que seja exibido o fatorial: "))
fatorial = 1
print("O fatorial é feito da seguinte forma:")
for x in range(numero, 1 - 1, -1):
    if x > 1:
        print(x, end=" * ")
    else:
        print(x)
    fatorial *= x
print(f"\nO valor do fatorial de {numero} é {fatorial}")
