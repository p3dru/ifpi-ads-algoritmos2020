lista = []
par = []
impar = []
while True:
    numero = int(input("Digite um número: "))
    lista.append(numero)
    if numero % 2 == 0:
        par.append(numero)
    else:
        impar.append(numero)
    opcao = input("Deseja continuar? ")
    if opcao in "Nn":
        break
print(f"A lista completa de números digitados é: {lista}")
print(f"A lista de números pares é: {par}")
print(f"A lista de números ímpares é: {impar}")
