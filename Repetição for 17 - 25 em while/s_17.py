denominador_final = int(input("Digite um número: "))
contador = 1
resultado = 0
while contador <= denominador_final:
    resultado += 1 / contador
    contador += 1
print(f"O resultado de S é: {resultado:.2f}")
