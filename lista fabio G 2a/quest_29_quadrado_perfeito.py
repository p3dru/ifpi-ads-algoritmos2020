numero = int(input("Digite um numero de 4 digitos: "))
digitos_frente = numero // 100
digitos_tras = numero % 100
soma = digitos_tras + digitos_frente
raiz_numero = numero ** 0.5
if raiz_numero == soma:
    print(f"O número {numero} é uma quadrado perfeito")
else:
    print(f"O número {numero} não é uma quadrado perfeito")
