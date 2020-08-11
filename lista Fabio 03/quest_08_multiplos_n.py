numero = int(input("Digite um valor para avaliar seus múltiplos: "))
limite_inferior = int(input("Digite o início para a busca: "))
limite_superior = int(input("Digite o limite para a busca: "))
for x in range(limite_inferior, limite_superior + 1):
    if x % numero == 0:
        print(f"O numero {x} é múltiplo de {numero}")
