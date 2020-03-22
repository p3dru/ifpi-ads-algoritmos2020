#entrada
custo_fabrica = float(input("Digite o valor de fabrica: "))
#processamento
distribuidor = (custo_fabrica * 28) / 100
impostos = (custo_fabrica * 45) / 100
custo_total = impostos + distribuidor + custo_fabrica
#saida
print(f"O valor total do carro será de R${custo_total:.2f}")