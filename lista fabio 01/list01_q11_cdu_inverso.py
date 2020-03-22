#entrada
numero = int(input("Digite um número de 3 digitos: "))
#processamento
centenas = numero // 100
dezenas = (numero % 100) // 10
unidade = (numero % 100) % 10
centenas = str(centenas)
dezenas = str(dezenas)
unidade = str(unidade)
#saida
print(unidade + dezenas + centenas)