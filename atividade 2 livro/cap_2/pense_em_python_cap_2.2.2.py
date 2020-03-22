#resolução unica
preco_de_capa = 24.95
desconto_livrarias = (preco_de_capa / 100) * 40
transporte_primeiro = desconto_livrarias + 3
transporte_resto = desconto_livrarias + 0.75
custo_total = transporte_resto * 59 + transporte_primeiro

print(f"O custo total é de R${custo_total:.2f}.")