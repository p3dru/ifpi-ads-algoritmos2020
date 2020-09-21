def mais_de_20(documento):
    for palavra in documento:
        word = palavra.strip()
        if len(word) > 20:
            print(word)
    print()

def nao_tem_e_meu_parcerin(documento):
    for palavra in documento:
        word = palavra.strip()
        if "e" not in word:
            print(word)
    print()

def letras_safadinhas(documento):
    proibidas = input("Digite as letras proibidas: ")
    for palavra in documento:
        word = palavra.strip()
        tem_na_palavra(proibidas, word)
    print()

def tem_na_palavra(restritos, palavra):
    contador = 0
    for elementos in range(len(restritos)):
        if restritos[elementos] in palavra:
            contador += 1
    if contador == 0:
        print(palavra)

def letras_desejadas(documento):
    permitidas = input("Digite as letras desejadas: ")
    for palavra in documento:
        word = palavra.strip()
        so_se_tiver(permitidas, word)

def so_se_tiver(permitidas, palavra):
    contador = 0
    for letra in range(len(palavra)):
        if palavra[letra] not in permitidas:
            contador += 1
    if contador == 0:
        print(palavra)
    print()

def uses_all(documento):
    obrigatorias = input("Digite as letras obrigatórias: ")
    for palavra in documento:
        words = palavra.strip()
        tem_todas(obrigatorias, words)
    print()

def tem_todas(pedidas, palavra):
    contador = 0
    for letra in range(len(pedidas)):
        if pedidas[letra] not in palavra:
            contador += 1
    if contador == 0:
        print(palavra)

def is_abecedarianis(documento):
    diferenca = 0
    for palavra in documento:
        word = palavra.strip()
        diferenca = diferenca_entre_letras(word)
        if diferenca < len(word):
            print(word)
    print()

def diferenca_entre_letras(palavra):
    diferenca = 0
    for letra in range(len(palavra) - 1):
        letra_atual = ord(palavra[letra])
        proxima = ord(palavra[letra + 1])
        diferenca += diferenca_modulo(letra_atual, proxima)
    return diferenca

def diferenca_modulo(letra_atual, letra_seguinte):
    diferenca = letra_seguinte - letra_atual
    if 2 > diferenca >= 0:
        diferenca = diferenca
    else:
        diferenca = 100
    return diferenca

    
letra = "e"
print("Digite uma das opções abaixo (a respeito do arquivo words.txt):\n"
      "1- Para procurar palavras com mais de 20 letras\n"
      f"2- Para procurar palavras que não possue a letra {letra}\n"
      "3- Para procurar palavras que não usam as letras que você desejar\n"
      "4- Para procurar palavras que usem apenas as letras que você desejar\n"
      "5- Para procurar palavras que usem obrigatoriamente (ao menos uma vez) as letras que você desejar\n"
      "6- Para procurar palavras na qual as letras estejam apenas em ordem alfabética crescente\n"
      "0- Para sair do programa")
print()
opcao = int(input("Digite a opção desejada: "))
print()
while opcao != 0:
    arquivo = open("words.txt")
    if opcao == 1:
        mais_de_20(arquivo)
    elif opcao == 2:
        nao_tem_e_meu_parcerin(arquivo)
    elif opcao == 3:
        letras_safadinhas(arquivo)
    elif opcao == 4:
        letras_desejadas(arquivo)
    elif opcao == 5:
        uses_all(arquivo)
    elif opcao == 6:
        is_abecedarianis(arquivo)
    elif opcao == 0:
        print("Obrigado por utilizar")
        break
    else:
        print("Opção inválida")
    opcao = int(input("Digite a opção desejada: "))
    print()
    arquivo.close()
    
        


