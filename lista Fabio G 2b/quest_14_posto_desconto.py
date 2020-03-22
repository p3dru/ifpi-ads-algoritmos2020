litros = float(input("Digite a quantidade de litros: "))
tipo = input("Digite o tipo de combustível: ")
if litros <= 20 and tipo == "A":
    total = litros * 1.9
    desconto = (total / 100) * 3
    total_com_desconto = total - desconto
elif litros > 20 and tipo == "A":
    total = litros * 1.9
    desconto = (total / 100) * 5
    total_com_desconto = total - desconto
elif litros <= 20 and tipo == "G":
    total = litros * 2.5
    desconto = (total / 100) * 4
    total_com_desconto = total - desconto
elif litros > 20 and tipo == "G":
    total = litros * 2.5
    desconto = (total / 100) * 6
    total_com_desconto = total - desconto
print(f"O valor total do abastecimento é de R${total_com_desconto:.2f}")