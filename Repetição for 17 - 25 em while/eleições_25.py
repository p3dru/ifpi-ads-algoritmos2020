quantidade_eleitores = int(input("Digite a quantidade de eleitores: "))
contador = 1
candidato_1 = candidato_2 = candidato_3 = voto_nulo = voto_branco = 0
while contador <= quantidade_eleitores:
    voto = int(input("Digite o seu voto: "))
    if voto == 1:
        candidato_1 += 1
    elif voto == 2:
        candidato_2 += 1
    elif voto == 3:
        candidato_3 += 1
    elif voto == 9:
        voto_nulo += 1
    elif voto == 0:
        voto_branco += 1
    contador += 1
print(f"O candidato 1 teve {candidato_1} votos\n"
      f"O candidato 2 teve {candidato_2} votos\n"
      f"O candidato 3 teve {candidato_3} votos\n"
      f"Total de votos nulos: {voto_nulo}\n"
      f"Total de votos branco: {voto_branco}\n")
if candidato_1 > candidato_2 and candidato_1 > candidato_3:
    print("O candidato 1 venceu a eleição")
if candidato_2 > candidato_3 and candidato_2 > candidato_1:
    print("O candidato 2 venceu a eleição")
if candidato_3 > candidato_1 and candidato_3 > candidato_2:
    print("O candidato 3 venceu a eleição")
