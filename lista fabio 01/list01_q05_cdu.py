#entrada
numero = int(input("Digite um número de 3 dígitos: "))
#processamento
centenas = numero // 100
dezenas = (numero % 100) // 10 #pega o resto da divisão e divide (inteiro) por 10
unidades = (numero % 100) % 10 #pega o resto da divisão e divide (resto) por 10
somatorio = centenas + dezenas + unidades
#saida
print("A soma dos elementos é {}" .format(somatorio))