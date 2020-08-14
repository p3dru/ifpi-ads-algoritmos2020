numero = int(input("Digite um número: "))
possivel_raiz = quadrado = 1
while quadrado < numero:
    possivel_raiz += 1
    quadrado = possivel_raiz ** 2
possivel_raiz -= 1
quadrado = possivel_raiz ** 2
print(f"O maior quadrado possível menor que {numero} é {possivel_raiz ** 2} (quadrado de {possivel_raiz})")
