loop = int(input("Digite um valor para N: "))
soma = 0
for x in range(loop):
    soma += (1/(x+1))
print(f"O valor da somas de N frações é: {soma:.2f}")
