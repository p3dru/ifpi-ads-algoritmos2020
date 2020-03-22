#entrada
metros_por_segundo = float(input("Digite o valor em m/s: "))
#processamento
transformacao = metros_por_segundo * 3.6
#saída
print("O resultado do valor digitado em Km/h é: {:.2f}".format(transformacao))