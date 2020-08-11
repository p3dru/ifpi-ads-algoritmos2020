tamanho_lista = int(input("Digite o tamanho da lista: "))
soma = 0
media = 0
for x in range(tamanho_lista):
    numero = int(input(f"Digite o número {x+1}: "))
    soma += numero
    media = soma / (x + 1)

print(f"A soma dos números é {soma} e a média é {media:.2f}")