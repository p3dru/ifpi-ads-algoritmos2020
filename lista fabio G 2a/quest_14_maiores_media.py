def maior_que_a_media(media, x, z, y, a, b):
    if media < x:
        print(f"O número {x} é acima da média")
    if media < y:
        print(f"O número {y} é acima da média")
    if media < z:
        print(f"O número {z} é acima da média")
    if media < a:
        print(f"O número {a} é acima da média")
    if media < b:
        print(f"O número {b} é acima da média")

numero_1 = int(input("Digite um número: "))
numero_2 = int(input("Digite um número: "))
numero_3 = int(input("Digite um número: "))
numero_4 = int(input("Digite um número: "))
numero_5 = int(input("Digite um número: "))
media = (numero_5 + numero_4 + numero_3 + numero_2 + numero_1) / 5
maior_que_a_media(media, numero_1, numero_2, numero_3, numero_4, numero_5)