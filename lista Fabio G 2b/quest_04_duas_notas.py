nota_1 = float(input("Digite sua primeira nota: "))
nota_2 = float(input("Digite sua segunda nota: "))
media = (nota_1 + nota_2) / 2
if media == 10:
    print("Aprovado com distinção")
elif media >= 7 and media < 10:
    print("Aprovado")
elif media < 7:
    print("Reprovado")
else:
    print("Digite notas válidas")