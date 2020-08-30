funcionarios = int(input("Digite o número de funcionários: "))
for i in range(funcionarios):
    codigo_funcionario = int(input("Digite o seu código: "))
    horas = float(input("Digite as horas trabalhadas: "))
    dependentes = int(input("Digite a quantidade de dependentes: "))
    total_horas_cash = horas * 12
    total_dependentes_cash = dependentes * 40
    salario_bruto = total_horas_cash + total_dependentes_cash
    inss = (salario_bruto * 8.5) / 100
    ir = (salario_bruto * 5) / 100
    salario_liquido = salario_bruto - (inss + ir)
    print(f"Valor descontado do INSS (8,5%) = R$ {inss:.2f}\n"
          f"Valor descontado do IR (5%) = R$ {ir:.2f}\n"
          f"Salário bruto = R$ {salario_bruto:.2f}\n"
          f"Salário líquido = R$ {salario_liquido:.2f}\n")
