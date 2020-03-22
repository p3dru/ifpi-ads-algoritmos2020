#entrada
numero = int(input("Digite um número inteiro e de 3 digitos: "))
#processamento
centenas = numero // 100 #unidades
dezenas = ((numero % 100) // 10) * 10 #isola e multiplica por 10 pra garantir as dezenas
unidades = ((numero % 100) % 10) * 100 #isola o numero de unidades e multiplica por 100 já virando centenas
numero_inverso = unidades + dezenas + centenas
diferenca = numero - numero_inverso
#saida
print(f"A diferença entre {numero} e {numero_inverso} é de {diferenca}")