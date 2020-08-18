lista = []
contador = 0
while True:
    contador += 1
    lista.append(int(input("Digite um número: ")))
    opcao = input("Deseja continuar? ")
    if opcao in "Nn":
        break
lista.sort(reverse=True)
print(f"Foram adicionados {contador} numeros à lista")
print(f"A lista em ordem decrescente: {lista}")
if 5 in lista:
    print("O número 5 está na lista")
else:
    print("O número 5 não está na lista")
