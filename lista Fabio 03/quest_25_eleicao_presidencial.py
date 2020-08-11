eleitores = int(input("Digite a quantidade de eleitores: "))
total_candidato_1 = 0
total_candidato_2 = 0
total_candidato_3 = 0
total_nulos = 0
total_brancos = 0
vencedor = 0
voto = 0
for x in range(eleitores):
    voto = int(input("Digite seu voto: "))
    if voto == 1:
        total_candidato_1 += 1
    elif voto == 2:
        total_candidato_2 += 1
    elif voto == 3:
        total_candidato_3 += 1
    elif voto == 9:
        total_nulos += 1
    elif voto == 0:
        total_brancos += 1
print(f"Total dos candidato 1: {total_candidato_1}")
print(f"Total dos candidato 2: {total_candidato_2}")
print(f"Total dos candidato 3: {total_candidato_3}")
print(f"Total dos votos nulos: {total_nulos}")
print(f"Total dos votos brancos: {total_brancos}")
if total_candidato_1 > total_candidato_2 and total_candidato_1 > total_candidato_3:
    vencedor = "Candidato 1"
elif total_candidato_2 > total_candidato_1 and total_candidato_2 > total_candidato_3:
    vencedor = "Candidato 2"
elif total_candidato_3 > total_candidato_2 and total_candidato_3 > total_candidato_1:
    vencedor = "Candidato 3"
elif total_candidato_1 == total_candidato_2:
    vencedor = "Empate entre os candidatos 1 e 2"
    if total_candidato_1 == total_candidato_2 == total_candidato_3:
        vencedor = "Empate entre os 3 candidatos"
elif total_candidato_1 == total_candidato_3:
    vencedor = "Empate entre os candidatos 1 e 3"
    if total_candidato_1 == total_candidato_2 == total_candidato_3:
        vencedor = "Empate entre os 3 candidatos"
elif total_candidato_3 == total_candidato_2:
    vencedor = "Empate entre os candidatos 2 e 3"
    if total_candidato_1 == total_candidato_2 == total_candidato_3:
        vencedor = "Empate entre os 3 candidatos"
print()
print("=" * 60)
print(f"Vencedor da eleição: {vencedor}")
print("=" * 60)
