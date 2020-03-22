#entrada
salario = float(input("Digite seu salário: "))
#processamento
aumento = salario * (25 / 100)
salario_total = salario + aumento
#saida
print(f"Seu salário era de R${salario:.2f}, recebeu aumento de R${aumento:.2f} e o total agora é de R${salario_total:.2f}")