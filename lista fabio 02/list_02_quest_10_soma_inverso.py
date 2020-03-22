#entrada
numero = int(input("Digite um número de 3 digitos: "))
#processamento
centenas = numero // 100
dezenas = ((numero % 100) // 10) * 10
unidades = ((numero % 100) % 10) * 100
inverso = centenas + dezenas + unidades
soma = numero + inverso
#saida
print(f"A soma de {numero} e seu inverso {inverso} é {soma}")
