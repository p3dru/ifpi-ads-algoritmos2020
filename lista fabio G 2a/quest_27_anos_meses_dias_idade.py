dia_atual = int(input("Digite o dia que estamos: "))
mes_atual = int(input("Digite o mes que estamos: "))
ano_atual = int(input("Digite o ano que estamos: "))
dia_nasc = int(input("Digite o dia que nasceu: "))
mes_nasc = int(input("Digite o mes que nasceu: "))
ano_nasc = int(input("Digite o ano em que nasceu: "))
if dia_atual > dia_nasc:
    idade_dias = (30 - dia_atual) + dia_nasc
else:
    idade_dias = dia_nasc - dia_atual
if mes_atual >= mes_nasc:
    idade_mes = mes_atual - mes_nasc
else:
    idade_mes = (12 - mes_nasc) + mes_atual
total_dias_atual = dia_atual + (mes_atual * 30)
total_dias_nasc = dia_nasc + (mes_nasc * 30)
if total_dias_atual != total_dias_nasc:
    idade_ano = ano_atual - ano_nasc
    idade_ano -= 1
else:
    idade_ano = ano_atual - ano_nasc
print(f"Sua idade é de {idade_dias} dia(s), {idade_mes} mes(es) e {idade_ano} ano(s)")