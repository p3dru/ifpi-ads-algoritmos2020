def sherlock_e_anagramas(string):
    letras = saber_se_tem_letras_iguais(string)
    pedacos = saber_se_tem_pedacos_iguais(string)
    resultado = (letras + pedacos)
    print(letras)
    print(pedacos)
    print(resultado)
    

def saber_se_tem_letras_iguais(string):
    iguais = posicao = 0
    for posicao in range(len(string)):
        letra_setada = string[posicao]
        nova_string = string[posicao+1:]
        for letra in nova_string:
            if letra == letra_setada:
                iguais += 1
                break
    return iguais

def verificar_se_todos_estão_na_string(palavra_anterior, palavra_seguinte):
    contador = iguais = 0
    for letra in palavra_anterior:
        if letra in palavra_seguinte == True:
            contador += 1
    if contador == len(palavra_seguinte):
        iguais = 1
    else:
        iguais = 0
    return iguais

def saber_se_tem_pedacos_iguais(string):
    nova_string = ""
    nova_string_seguinte = ""
    pontos = 0
    for contador in range(len(string)):
        if contador >= 1 and contador < len(string):
            nova_string = string[:contador]
            nova_string_seguinte = string[1:contador + 1]
            pontos += verificar_se_todos_os_elementos_estao(nova_string, nova_string_seguinte) #possível_erro
            pontos += verificar_se_substring_in(nova_string, string, contador) #possível_erro
    return pontos
            
def verificar_se_todos_os_elementos_estao(palavra, palavra_seguinte):
    score = iguais = 0
    palavra_criada = ""
    for elemento in range(len(palavra)):
        if palavra[elemento] in palavra_seguinte:
            score += 1
    if score == len(palavra):
        iguais = 1
    return iguais

def verificar_se_substring_in(nova_string, string, contador):
    score = 0
    if nova_string in string[contador:]:
        score += 1
    return score

casos = int(input())
while casos > 0:
    palavra = input()
    sherlock_e_anagramas(palavra)
    casos -= 1
    
