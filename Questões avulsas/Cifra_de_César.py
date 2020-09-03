palavra = input("Digite a palavra a ser criptografada: ")
rotacao = int(input("Digite a quantidade de posições a ser deslocada: "))
nova_palavra = nova_palavra = ""
diferenca = 0
for letra in palavra:
    if rotacao > 0:
        if 65 <= ord(letra) <= 90:
            if 64 < (ord(letra) + rotacao) <= 90:
                nova_letra = chr(ord(letra) + rotacao)
            elif 64 < (ord(letra) + rotacao) > 90:
                diferenca = 90 - ord(letra)
                nova_letra = chr(65 + (rotacao - diferenca) - 1)
        if 97 <= ord(letra) <= 122:
            if 96 < (ord(letra) + rotacao) <= 122:
                nova_letra = chr(ord(letra) + rotacao)
            elif 96 < (ord(letra) + rotacao) > 122:
                diferenca = 122 - ord(letra)
                nova_letra = chr(97 + (rotacao - diferenca) - 1)
    elif rotacao < 0:
        if 97 <= ord(letra) <= 122:
            if 123 > (ord(letra) + rotacao) >= 97:
                nova_letra = chr(ord(letra) + rotacao)
            elif (ord(letra) + rotacao) < 97:
                diferenca = ord(letra) - 97
                nova_letra = chr(122 + (rotacao + diferenca) + 1)
        if 65 <= ord(letra) <= 90:
            if 91 > (ord(letra) + rotacao) >= 65:
                nova_letra = chr(ord(letra) + rotacao)
            elif (ord(letra) + rotacao) < 65:
                diferenca = ord(letra) - 65
                nova_letra = chr(90 + (rotacao + diferenca) + 1)
        nova_palavra += nova_letra
print(nova_palavra)


def rotate_word(palavra, rotacao):
    palavra = input("Digite a palavra a ser criptografada: ")
    rotacao = int(input("Digite a quantidade de posições a ser deslocada: "))
    nova_palavra = nova_palavra = ""
    diferenca = 0
    for letra in palavra:
        if rotacao > 0:
            if 65 <= ord(letra) <= 90:
                if 64 < (ord(letra) + rotacao) <= 90:
                    nova_letra = chr(ord(letra) + rotacao)
                elif 64 < (ord(letra) + rotacao) > 90:
                    diferenca = 90 - ord(letra)
                    nova_letra = chr(65 + (rotacao - diferenca) - 1)
            if 97 <= ord(letra) <= 122:
                if 96 < (ord(letra) + rotacao) <= 122:
                    nova_letra = chr(ord(letra) + rotacao)
                elif 96 < (ord(letra) + rotacao) > 122:
                    diferenca = 122 - ord(letra)
                    nova_letra = chr(97 + (rotacao - diferenca) - 1)
        elif rotacao < 0:
            if 97 <= ord(letra) <= 122:
                if 123 > (ord(letra) + rotacao) >= 97:
                    nova_letra = chr(ord(letra) + rotacao)
                elif (ord(letra) + rotacao) < 97:
                    diferenca = ord(letra) - 97
                    nova_letra = chr(122 + (rotacao + diferenca) + 1)
            if 65 <= ord(letra) <= 90:
                if 91 > (ord(letra) + rotacao) >= 65:
                    nova_letra = chr(ord(letra) + rotacao)
                elif (ord(letra) + rotacao) < 65:
                    diferenca = ord(letra) - 65
                    nova_letra = chr(90 + (rotacao + diferenca) + 1)
        nova_palavra += nova_letra
    return nova_palavra
