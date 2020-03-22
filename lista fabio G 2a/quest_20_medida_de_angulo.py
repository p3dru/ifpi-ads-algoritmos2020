angulo = int(input("Digite o valor de um ângulo (entre 0 e 360): "))
if 0 < angulo <= 90:
    print("O ângulo está no primeiro quadrante")
elif 90 < angulo <= 180:
    print("O ângulo está no segundo quadrante")
elif 180 < angulo <= 270:
    print("O angulo está no terceiro quadrante")
elif 270 < angulo < 360:
    print("O angulo está no quarto quadrante")