#entrada
anos_fumando = int(input("Há quanto tempo fuma: "))
cigarros_dia = int(input("Quantos cigarros por dia fuma: "))
preco_carteira = float(input("Quanto custa a carteira: "))
#processamento
preco_unidade = preco_carteira / 20
total = (cigarros_dia * (anos_fumando * 365)) * preco_unidade
#saida
print(f"O valor total gasto foi de R${total:.2f}")