import math

numero = int(input())
nova_palavra = nova_letra = ""
contador = 1
for voltas in range(numero):
    palavra = input()
    for letra in palavra:
        if 65 <= ord(letra) <= 90 or 97 <= ord(letra) <= 122:
            nova_palavra += chr(ord(letra) + 3)
        else:
            nova_palavra += letra
    """print(nova_palavra)"""
    nova_palavra = nova_palavra[::-1]
    """print(nova_palavra)"""
    metade = math.trunc(len(nova_palavra) / 2)
    primeira_parte = nova_palavra[:metade]
    segunda_parte = nova_palavra[metade:]
    """print(segunda_parte)"""
    for letra in segunda_parte:
        nova_letra = chr(ord(letra) - 1)
        primeira_parte += nova_letra
    print(primeira_parte)
    nova_palavra = primeira_parte = segunda_parte = ""
    
    
