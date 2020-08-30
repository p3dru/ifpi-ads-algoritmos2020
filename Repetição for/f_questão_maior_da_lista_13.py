quantidade = int(input("Digite a quantidade de números que deseja: "))
maior = 0
for numeros in range(1, quantidade + 1):
    numero = int(input("Digite um número: "))
    if numero > maior:
        maior = numero
print(f"O maior número da lista é {maior}")
