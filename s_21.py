denominador = numerador = 1
total = 0
while denominador <= 50:
    print(f"{numerador} / {denominador}")
    total += numerador / denominador
    valor = numerador / denominador
    numerador += 2
    denominador += 1
print(f"O total de s é: {total:.2f}")

