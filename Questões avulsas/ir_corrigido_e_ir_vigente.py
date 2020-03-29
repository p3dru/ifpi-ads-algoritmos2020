salario = float(input("Digite o valor de seu salário: "))
aliquota = 0
desconto = 0
salario_corrigido = 0
print("=" * 56)
mensagem_1 = "Tabela IR Vigente"
print(f"{mensagem_1:^56}")
print()
if salario <= 1903.98:
    print(f"Isento na tabela vigente -> R${salario:.2f}")
    print("=" * 56)
elif 1903.98 < salario <= 2826.65:
    desconto = (salario * 7.5) / 100
    salario_corrigido = salario - desconto
    print(f"O valor do novo salário na tabela vigente é R${salario_corrigido:.2f}")
    print("=" * 56)
elif 2826.65 < salario <= 3751.05:
    desconto = (salario * 15) / 100
    salario_corrigido = salario - desconto
    print(f"O valor do novo salário na tabela vigente é R${salario_corrigido:.2f}")
    print("=" * 56)
elif 3751.05 < salario <= 4664.68:
    desconto = (salario * 22.5) / 100
    salario_corrigido = salario - desconto
    print(f"O valor do novo salário na tabela vigente é R${salario_corrigido:.2f}")
    print("=" * 56)
elif 4464.68 < salario:
    desconto = (salario * 27.5) / 100
    salario_corrigido = salario - desconto
    print(f"O valor do novo salário na tabela vigente é R${salario_corrigido:.2f}")
    print("=" * 56)
print("=" * 56)
mensagem_2 = "Tabela IR Corrigida"
print(f"{mensagem_2:^56}")
print()
if salario <= 3881.65:
    print("Isento na tabela corrigida")
    print("=" * 56)
elif 3881.65 < salario <= 5714.11:
    desconto = (salario * 7.5) / 100
    salario_corrigido = salario - desconto
    print(f"O valor do novo salário na tabela corrigida é R${salario_corrigido:.2f}")
    print("=" * 56)
elif 5714.11 < salario <= 7654.67:
    desconto = (salario * 15) / 100
    salario_corrigido = salario - desconto
    print(f"O valor do novo salário na tabela corrigida é R${salario_corrigido:.2f}")
    print("=" * 56)
elif 7654.67 < salario <= 9564.42:
    desconto = (salario * 22.5) / 100
    salario_corrigido = salario - desconto
    print(f"O valor do novo salário na tabela corrigida é R${salario_corrigido:.2f}")
    print("=" * 56)
elif 9564.42 < salario:
    desconto = (salario * 27.5) / 100
    salario_corrigido = salario - desconto
    print(f"O valor do novo salário na tabela corrigida é R${salario_corrigido:.2f}")
    print("=" * 56)
