fatorial = total = int(input("Digite um número para que seja exibido seu fatorial: "))
while fatorial > 1:
    fatorial -= 1
    total *= fatorial
print(total)
