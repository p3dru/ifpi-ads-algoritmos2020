denominador = numerador = 1
total = 0
for i in range(50):
    print(f"{numerador} / {denominador}")
    total += numerador / denominador
    valor = numerador / denominador
    numerador += 2
    denominador += 1
print(f"O total de s é: {total:.2f}")

