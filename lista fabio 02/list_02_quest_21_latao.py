#entrada
latao = float(input("Informe a quantidade de latão que deseja ser feito: "))
#processamento
cobre = (latao * 70) / 100
zinco = (latao * 30) / 100
#saida
print(f"Para se fazer {latao:.2f} kg de latão, são necessários {cobre:.2f} kg de cobre e {zinco:.2f} kg de zinco")