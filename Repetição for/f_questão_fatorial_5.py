fatorial = int(input("Digite um número para que seja exibido seu fatorial: "))
total = 1
for numero in range(fatorial, 1, -1):
    total *= numero
print(f"O fatorial de {fatorial} é: {total}")
