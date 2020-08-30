habitantes = int(input("Quantidades de habitantes para a pesquisa: "))
contador = 1
total_salarios = total_filhos = contador_até_1000 = 0
for elementos in range(habitantes):
    salario = float(input("Digite o seu salário: "))
    filhos = int(input("Quantos filhos você tem: "))
    total_salarios += salario
    total_filhos += filhos
    if salario <= 1000:
        contador_até_1000 += 1
media_salarial = total_salarios / habitantes
media_de_filhos = total_filhos / habitantes
print(f"A média salarial da população pesquisada é de: R$ {media_salarial:.2f}")
print(f"A média de filhos da população pesquisada é de: {media_de_filhos:.2f}")
percentual_até_1000 = (contador_até_1000 * 100) / habitantes
print(f"O percentual de pessoas que ganham até R$ 1000,00 é de {percentual_até_1000:.2f}%")
