multiplicando = 1
contador = 1
total = 0
for numeros in range(1, 101):
    if multiplicando != 11 and contador != 11:
        total = multiplicando * contador
        print(f"{multiplicando} X {contador} = {total}")
        contador += 1
        if contador == 11:
            print("=+" * 20)
            contador = 1
            multiplicando += 1
