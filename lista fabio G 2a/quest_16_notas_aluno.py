nota_1 = float(input("Digite a primeira nota: "))
nota_2 = int(input("Digite a segunda nota: "))
media = (nota_2 + nota_1) / 2
if media >= 7:
    print("Aprovado")
else:
    exame_final = float(input("Digite a nota do exame final: "))
    media = (exame_final + media) / 2
    if media >= 5:
        print("Aprovado")
    else:
        print("Reprovado")