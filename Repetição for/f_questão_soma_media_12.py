quantidade_de_numeros = int(input("Digite a quantidade de numeros que deseja: "))
soma = media = 0
for numeros in range(1, quantidade_de_numeros + 1):
    numero = int(input("Digite um valor: "))
    soma += numero
    media = soma / numeros
print(f"A soma de todos os números é: {soma}\n"
      f"A média de entre os números digitados é: {media:.2f}")
