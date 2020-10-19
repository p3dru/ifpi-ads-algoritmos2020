termos = int(input("Digite a quantidade de termos que deseja: "))
lista = []
primeiro = 0
segundo = 1
terceiro = segundo + primeiro
for elementos in range(termos):
    if elementos == 0:
        lista.append(primeiro)
    elif elementos == 1:
        lista.append(segundo)
    else:
        terceiro = segundo + primeiro
        primeiro = segundo
        segundo = terceiro
        lista.append(terceiro)
print()
print(f"Os {termos} primeiros termos de Fibonacci são: {lista}")
