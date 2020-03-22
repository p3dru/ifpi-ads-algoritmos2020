x_1 = int(input("Digite o valor de x1: "))
y_1 = int(input("Digite o valor de y1: "))
x_2 = int(input("Digite o valor de x2: "))
y_2 = int(input("Digite o valor de y2: "))
if x_1 > 0:
    lado_x = (x_1 * -1) + x_2
elif x_2 > 0:
    lado_x = (x_2 * -1) + x_1
elif x_2 > 0 and x_1 > 0 and x_2 > x_1:
    lado_x = x_2 - x_1
elif x_2 > 0 and x_1 > 0 and x_1 > x_2:
    lado_x = x_1 - x_2
if y_1 > 0:
    lado_y = (y_1 * -1) + y_2
elif y_2 > 0:
    lado_y = (y_2 * -1) + y_1
elif y_2 > 0 and y_1 > 0 and y_2 > y_1:
    lado_y = y_2 - y_1
elif y_2 > 0 and y_1 > 0 and y_1 > y_2:
    lado_y = y_1 - y_2

area = lado_x * lado_y
if area < 0:
    area = area * -1
print(f"A area do retângulo é de {area}")