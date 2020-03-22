#entrada
valor_total = float(input("Digite o valor total: "))
#processamento
entrada = (valor_total // 3) + (valor_total % 3)
parcelas = valor_total // 3
#saida
print(f"O valor total é de R${valor_total:.2f}, a entrada fica de {entrada:.2f} e as parcelas ficam de {parcelas:.2f}")