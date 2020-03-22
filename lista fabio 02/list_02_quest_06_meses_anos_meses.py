#entrada
meses = int(input("Digite uma quantidade de meses: "))
#processamento
anos = meses // 12
meses_restantes = meses % 12
#saida
print(f"{meses} meses correspondem à {anos} ano(s) e {meses_restantes} mes(es).")