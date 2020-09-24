def Funny_not_Funny(testes):
    while testes > 0:
        string = input()
        string_invertida = inverter_string(string)
        erros = percorrer_strings(string, string_invertida)
        if erros == 0:
            print("Funny")
        else:
            print("Not Funny")
        testes -= 1

def inverter_string(palavra):
    palavra_invertida = palavra[::-1]
    return palavra_invertida

def percorrer_strings(palavra_1, palavra_2):
    diferenca = diferenca_inversa = erros = 0
    for letra in range(len(palavra_1) - 1):
        diferenca = ord(palavra_1[letra]) - ord(palavra_1[letra + 1])
        diferenca_inversa = ord(palavra_2[letra]) - ord(palavra_2[letra + 1])
        diferenca = módulo(diferenca)
        diferenca_inversa = módulo(diferenca_inversa)
        if diferenca != diferenca_inversa:
            erros += 1
    return erros

def módulo(numero):
    modulo = 0
    if numero >= 0:
        modulo = numero
    else:
        modulo = numero * -1
    return modulo

testes = int(input())
Funny_not_Funny(testes)
