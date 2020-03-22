dia_atual = int(input("Digite o dia atual: "))
mes_atual = int(input("Digite o mes atual: "))
ano_atual = int(input("Digite o ano atual: "))
dia_nasc = int(input("Digite o dia de nascimento: "))
mes_nasc = int(input("Digite o mes de nascimento: "))
ano_nasc = int(input("Digite o ano de nascimento: "))
total_dias_nasc = dia_nasc + (mes_nasc * 30)
total_dias_atual = dia_atual + (mes_atual * 30)
if total_dias_nasc == total_dias_atual:
    idade_ano = (ano_atual - ano_nasc)
elif total_dias_nasc < total_dias_atual:
    idade_ano = (ano_atual - ano_nasc)
else:
    idade_ano = (ano_atual - ano_nasc) - 1
print(f"A idade em anos dessa pessoa é de {idade_ano} ano(s)")