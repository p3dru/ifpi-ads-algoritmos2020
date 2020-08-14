quantidade = int(input("Digite a quantidade de números que deseja: "))
contador = 0
maior = 0
while contador < quantidade:
    numero = int(input("Digite um número: "))
    if numero > maior:
        maior = numero
    contador += 1
print(f"O maior número da lista é {maior}")
