#entrada
saques = int(input("Digite o valor que deseja sacar: "))
#processamento
notas_100 = saques // 100
resto = saques % 100
notas_50 = resto // 50
resto = resto % 50
notas_20 = resto // 20
resto = resto % 20
notas_10 = resto // 10
resto = resto % 10
notas_5 = resto // 5
resto = resto % 5
notas_2 = resto // 2
resto = resto % 2
notas_1 = resto
print(f"Notas de 100: {notas_100}\nNotas de 50: {notas_50}\n"
      f"Notas de 20: {notas_20}\nNotas de 10: {notas_10}\n"
      f"Notas de 5: {notas_5}\nNotas de 2: {notas_2}\nNotas de 1: {notas_1}")