def primeira_parte(palavra):
    nova_palavra = ""
    for letra in palavra:
        nova_palavra += nova_letra(letra)
    return nova_palavra
        
def nova_letra(letra):
    ord_letra = ord(letra)
    if 64 < ord_letra < 91 or 96 < ord_letra < 123:
        ord_letra += 3
        ord_letra = chr(ord_letra)
    else:
        ord_letra = chr(ord_letra)
    return ord_letra

def segunda_parte(palavra):
    palavra_invertida = palavra[::-1]
    return palavra_invertida

def terceira_parte(palavra):
    meio = int(len(palavra) / 2)
    primeira_parte = palavra[:meio]
    segunda_parte = palavra[meio:]
    segunda_parte = transformar_segunda_parte(segunda_parte)
    palavra_completa = primeira_parte + segunda_parte
    return palavra_completa

def transformar_segunda_parte(palavra):
    segunda_parte = ""
    for letra in palavra:
        nova_letra = ord(letra) - 1
        nova_letra = chr(nova_letra)
        segunda_parte += nova_letra
    return segunda_parte
    
    

casos = int(input())
contador = 0
while contador < casos:
    palavra = input()
    primeira_passada = primeira_parte(palavra)
    print(primeira_passada)
    segunda_passada = segunda_parte(primeira_passada)
    print(segunda_passada)
    terceira_passada = terceira_parte(segunda_passada)
    print(terceira_passada)
    contador += 1
