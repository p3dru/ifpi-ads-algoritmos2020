inicio = int(input("Digite um inicio: "))
fim = int(input("Digite o fim: "))
while inicio < fim:
    if inicio == 1:
        inicio += 1
    if inicio % 2 != 0 and inicio % 3 != 0 and inicio % 5 != 0 and inicio % 7 != 0 and inicio % 11 != 0 and inicio % 13 != 0 and inicio % 17 or inicio == 2 or inicio == 3 or inicio == 5 or inicio == 7 or inicio == 11:
        print(f"O número {inicio} é primo")
    inicio += 1
