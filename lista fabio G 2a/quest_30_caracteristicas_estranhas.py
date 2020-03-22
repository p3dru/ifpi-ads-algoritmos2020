numero = int(input("Digite um numero de 4 algarismos: "))
digitos_frente = numero // 100
digitos_tras = numero % 100
soma = digitos_frente + digitos_tras
quadrado_soma = soma ** 2
if quadrado_soma == numero:
    print(f"O numero {numero} atende á essas características estranhas")
else:
    print(f"O numero {numero} não atende à essas características estranhas")