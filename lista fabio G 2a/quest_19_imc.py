altura = float(input("Digite sua altura (em metros): "))
peso = float(input("Digite seu peso: "))
imc = peso / (altura ** 2)
if imc < 25:
    print("Você está no peso normal")
elif 25 <= imc <= 30:
    print("Você está obeso")
elif imc > 30:
    print("Vocês está com obesidade mórbida")
