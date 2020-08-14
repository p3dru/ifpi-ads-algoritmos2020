quantidade_de_numeros = int(input("Digite a quantidade de numeros que deseja: "))
contador = soma = media = 0
while contador < quantidade_de_numeros:
    numero = int(input("Digite um valor: "))
    soma += numero
    contador += 1
    media = soma / contador
print(f"A soma de todos os números é: {soma}\n"
      f"A média de entre os números digitados é: {media:.2f}")
