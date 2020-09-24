def slice_manual(palavra, tamanho):
    palavra_final = palavra[:tamanho]
    return palavra_final

def eh_maiuscula(palavra):
    contador_upper = 0
    maiusculas = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for letra in palavra:
        if letra in maiusculas:
            contador_upper += 1
    return contador_upper

def eh_minuscula(palavra):
    contador_lower = 0
    minusculas = "abcdefghijklmnopqrstuvwxyz"
    for letra in palavra:
        if letra in minusculas:
            contador_lower += 1
    return contador_lower

def eh_digito(palavra):
    contador_digito = 0
    digito = "0123456789"
    for letra in palavra:
        if letra in digito:
            contador_digito += 1
    return contador_digito

def eh_especial(palavra):
    contador_especial = 0
    especial = "!@#$%^&*()-+"
    for letra in palavra:
        if letra in especial:
            contador_especial += 1
    return contador_especial


comprimento_de_string = int(input())
string = input()
string = slice_manual(string, comprimento_de_string)
pontos = diferenca = 0
if comprimento_de_string >= 6:
    pontos += 1
maiusculas = eh_maiuscula(string)
if maiusculas > 0:
    pontos += 1
minusculas = eh_minuscula(string)
if minusculas > 0:
    pontos += 1
digitos = eh_digito(string)
if digitos > 0:
    pontos += 1
especiais = eh_especial(string)
if especiais > 0:
    pontos += 1
if pontos == 5:
    print("Senha Forte")
else:
    if comprimento_de_string >= 6:
        diferenca = 5 - pontos
    else:
        diferenca = 6 - comprimento_de_string
    print(diferenca)
