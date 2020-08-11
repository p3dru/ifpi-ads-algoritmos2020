funcionarios = int(input("Quantos funcionário tem em sua empresa: "))
valor_hora = 12
valor_dependente = 40
for x in range(funcionarios):
    codigo = input("Digite o seu código: ")
    horas_trabalhadas = float(input("Digite o número de horas trabalhadas: "))
    dependentes = int(input("Digite o número de dependentes: "))
    salario = (horas_trabalhadas * valor_hora) + (dependentes * valor_dependente)
    ir = (salario * 5) / 100
    inss = (salario * 8.5) / 100
    salario_liquido = (salario - ir) - inss
    print(f"O funcionário {codigo} recebe ao todo R${salario:.2f}\nTem os seguintes descontos:\n"
          f"IR = {ir:.2f}\nINSS = {inss:.2f}\n"
          f"E recebe ao todo R${salario_liquido:.2f}")