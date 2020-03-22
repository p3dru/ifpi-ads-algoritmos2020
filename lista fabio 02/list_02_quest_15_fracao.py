#entrada
numerador_1 = int(input("Digite o valor do numerador 1: "))
denominador_1 = int(input("Digite o valor do denominador 1: "))
numerador_2 = int(input("Digite o valor do numerador 2: "))
denominador_2 = int(input("Digite o valor do denominador 2: "))
#processamento
mmc = denominador_2 * denominador_1
numerador_1 = (mmc / denominador_1) * numerador_1
numerador_2 = (mmc / denominador_2) * numerador_2
soma = numerador_2 + numerador_1
#saida
print(f"A soma das frações {numerador_1:.0f}/{denominador_1} e {numerador_2:.0f}/{denominador_2} é {soma:.0f}/{mmc}")