denominador = int(input("Digite um número: "))
numerador = 1
total = 0
while denominador >= 1:
    resultado = numerador / denominador
    numerador += 1
    denominador -= 1
    total += resultado
print(f"O valor de S é: {total:.2f}")
    
