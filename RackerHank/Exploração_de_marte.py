def Exploração_de_marte(palavra, quantidade):
    correta = "SOS" * quantidade
    erros = 0
    for letra in range(len(palavra)):
        if palavra[letra] != correta[letra]:
            erros += 1
    print(erros)
    

string = input()
palavras = int(len(string) / 3)
Exploração_de_marte(string, palavras)
