denominador_final = int(input("Digite um número: "))
contador = 1
resultado = 0
for elemento in range(1, denominador_final + 1):
    resultado += 1 / contador
    contador += 1
print(f"O resultado de S é: {resultado:.2f}")
