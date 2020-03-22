file_ate_5 = 4.9
file_depois_5 = 5.8
alcatra_ate_5 = 5.9
alcatra_depois_5 = 6.8
picanha_ate_5 = 6.9
picanha_depois_5 = 7.8
opcao = input("Digite a opção que deseja: ")
kg = float(input("Digite a quantidade de kg que quer: "))
if opcao == "file" and kg <= 5:
    total_bruto = file_ate_5 * kg
elif opcao == "file" and kg > 5:
    total_bruto = file_depois_5 * kg
elif opcao == "alcatra" and kg <= 5:
    total_bruto = alcatra_ate_5 * kg
elif opcao == "alcatra" and kg > 5:
    total_bruto = alcatra_depois_5 * kg
elif opcao == "picanha" and kg <= 5:
    total_bruto = picanha_ate_5 * kg
elif opcao == "picanha" and kg > 5:
    total_bruto = picanha_depois_5 * kg
pagamento = input("Como deseja pagar: ")
if pagamento == "cartão" or pagamento == "cartao":
    desconto = (total_bruto / 100) * 5
    total = total_bruto - desconto
else:
    desconto = 0
    total = total_bruto
print(f"Tipo de carne: {opcao}\nQuantidade de carne: {kg:.2f}kg\n"
      f"Preço total: {total_bruto:.2f}\nTipo de pagamento: {pagamento}\n"
      f"Valor de desconto: {desconto:.2f}\nTotal a pagar: R${total:.2f}")