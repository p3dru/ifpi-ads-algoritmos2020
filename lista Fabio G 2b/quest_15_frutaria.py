quantidade_morangos = float(input("Digite a quantidade (em kg) de morangos: "))
quantidade_macas = float(input("Digite a quantidade (em kg) de maçãs: "))
ate_5_morango = 2.5
ate_5_macas = 1.8
depois_5_morango = 2.2
depois_5_macas = 1.5
total_kg = quantidade_macas + quantidade_morangos
if quantidade_morangos <= 5:
    preco_total_morangos = quantidade_morangos * ate_5_morango
elif quantidade_morangos > 5:
    preco_total_morangos = quantidade_morangos * depois_5_morango
if quantidade_macas <= 5:
    preco_total_macas = quantidade_macas * ate_5_macas
elif quantidade_macas > 5:
    preco_total_macas = quantidade_macas * depois_5_macas
total_a_ser_pago = preco_total_macas + preco_total_morangos
if total_kg > 8 or total_a_ser_pago > 25:
    desconto = (total_a_ser_pago / 100) * 10
    total_a_ser_pago = total_a_ser_pago - desconto
print(f"O total a ser pago será de R${total_a_ser_pago:.2f}")