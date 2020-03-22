nota_1 = float(input("Digite a nota 1: "))
nota_2 = float(input("Digite a nota 2: "))
media = (nota_2 + nota_1) / 2
print(f"Nota 1: {nota_1}\nNota 2: {nota_2}\nMédia: {media}")
if media <= 4:
    conceito = "E"
    print(f"Conceito: {conceito}")
elif 4 < media <= 6:
    conceito = "D"
    print(f"Conceito: {conceito}")
elif 6 < media <= 7.5:
    conceito = "C"
    print(f"Conceito: {conceito}")
elif 7.5 < media <= 9:
    conceito = "B"
    print(f"Conceito: {conceito}")
else:
    conceito = "A"
    print(f"Conceito: {conceito}")
if conceito == "E" or conceito == "D":
    print("REPROVADO")
else:
    print("APROVADO")