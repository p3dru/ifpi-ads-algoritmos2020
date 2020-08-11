quantidade_lista = int(input("Digite o tamanho da lista: "))
maior = 0
for x in range(quantidade_lista):
    numero = int(input("Digite um número: "))
    if numero > maior:
        maior = numero

print(f"O maior número lido é {maior}")