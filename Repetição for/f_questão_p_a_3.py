inicio = int(input("Digite o início da P.A: "))
limite = int(input("Digite um valor limite: "))
razao = int(input("Digite a razão de crescimento: "))
for numeros in range(inicio, limite + 1):
    if inicio < limite + 1:
        print(inicio)
        inicio += razao
        
