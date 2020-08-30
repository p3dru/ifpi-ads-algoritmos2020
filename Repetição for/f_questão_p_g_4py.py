inicio = int(input("Digite o início: "))
limite = int(input("Digite o limite: "))
razao = int(input("Digite a razão de crescimento da P.G: "))
for numeros in range(inicio, limite + 1):
    if inicio < (limite + 1):
        print(inicio)
        inicio *= razao
