numero = int(input("Digite um valor N: "))
quadrado = 0
quadrado_inferior = 0
for x in range(numero + 1):
    quadrado = x ** 2
    if quadrado < numero:
        quadrado_inferior = quadrado
print(quadrado_inferior)
