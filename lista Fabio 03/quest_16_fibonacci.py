numero_termos = int(input("Digite o valor de termos que deseja na sequência Fibonacci: "))
print()
proximo = 1
inicio = 0
mostrado = 0
print("0", end=" ")
print("1", end=" ")
for x in range(numero_termos - 2):
    mostrado = proximo + inicio
    print(mostrado, end=" ")
    inicio = proximo
    proximo = mostrado
print()
