#entrada
numero_1 = int(input("Digite um numero: "))
numero_2 = int(input("Digite um outro numero: "))
#processamento
quociente = numero_1 //  numero_2
resto = numero_1 % numero_2
#saida
print(f"O valor do quociente da divisão do primeiro pelo segundo é {quociente:.2f} e o resto é {resto}")