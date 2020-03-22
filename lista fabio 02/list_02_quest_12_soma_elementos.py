#entrada
numero = int(input("Digite um numero de 4 algarismos: "))
#processamento
milhares = numero // 1000
centenas = (numero % 1000) // 100
dezenas =  ((numero % 1000) % 100) // 10
unidades = ((numero % 1000) % 100) % 10
soma = milhares + dezenas + centenas + unidades
#saida
print(f"A soma dos algarismos do número {numero} é {soma}.")