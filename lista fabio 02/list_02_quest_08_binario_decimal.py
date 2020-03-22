#entrada
numero_binario = int(input("Digite um numero binario de quatro digitos: "))
#processamento
bin_4 = numero_binario // 1000
bin_3 = (numero_binario // 100) % 10
bin_2 = ((numero_binario // 10) % 100) % 10
bin_1 = numero_binario % 10
convertido_1 = bin_1 * 1
convertido_2 = bin_2 * 2
convertido_3 = bin_3 * 4
convertido_4 = bin_4 * 8
decimal = convertido_1 + convertido_2 + convertido_3 + convertido_4
#saida
print(f"O numero {bin_4}{bin_3}{bin_2}{bin_1} em binário equivale à {decimal} decimal.")