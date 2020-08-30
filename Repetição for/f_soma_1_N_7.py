numero = contador = int(input("Digite um número: "))
numero -= 1
contador -= 1
for numeros in range(contador, 1, -1):
    if contador > 2:
        numero += contador - 1
        contador -= 1
print(f"A soma de todos os números entre 1 à N é {numero}") 
    
