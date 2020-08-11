def numero_primo(numero):
    if numero % 2 != 0 and numero % 3 != 0 and numero % 5 != 0 and numero % 7 != 0 and numero % 11 != 0:
        print(numero, end=" ")
    elif numero == 2 or numero == 3 or numero == 5 or numero == 7 or numero == 11:
        print(numero, end=" ")


limite_inferior = int(input("Digite um valor de início: "))
limite_superior = int(input("Digite um valor limite: "))
if limite_inferior == 1:
    limite_inferior = 2
for x in range(limite_inferior, limite_superior):
    numero_primo(x)
