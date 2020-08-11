habitantes = int(input("Digite a quantidade de habitantes: "))
media_salarial = 0
media_filhos = 0
contador = 0
porcentagem = 0
media_filhos_final = 0
media_salarial_final = 0
for x in range(habitantes):
    salario = float(input("Digite o seu salário: "))
    filhos = int(input("Digite a quantidade de filhos que tem: "))
    media_salarial += salario
    media_filhos += filhos
    if salario <= 1000:
        contador += 1
    porcentagem = (contador / habitantes) * 100
    media_filhos_final = media_filhos / habitantes
    media_salarial_final = media_salarial / habitantes
print()
print("=" * 60)
print(f"Media de saĺário populacional: R${media_salarial_final:.2f}\n"
      f"Media de número de filhos: {media_filhos_final:.2}\n"
      f"O percentual das pessoas que recebem até R$1000.00 é de {porcentagem:.2f}%")
