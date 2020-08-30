numero_final = int(input("Digite um número: "))
contador = 1
for i in range(numero_final, 0, -1):
    if contador == 1:
        total = contador / numero_final
        contador += 1
        numero_final -= 1
    else:
        if contador % 2 == 0:
            total -= numero_final / contador
            contador += 1
            numero_final -= 1
        else:
            total += contador / numero_final
            contador += 1
            numero_final -= 1
print(f"O valor de s é: {total:.2f}")
