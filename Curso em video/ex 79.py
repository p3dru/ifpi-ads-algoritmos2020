lista_de_numeros = []
while True:
    numero = int(input("Digite um número: "))
    if numero not in lista_de_numeros:
        lista_de_numeros.append(numero)
    else:
        print("Número já consta na lista, não adicionarei!")
    opcao = input("Deseja continuar? ")
    if opcao in "NnNãoNÃOnão":
        break
print("+-" * 30)
print("Todos os valores foram computados")
print("+-" * 30)
lista_de_numeros.sort()
print(f"A lista em ordem é {lista_de_numeros}")
