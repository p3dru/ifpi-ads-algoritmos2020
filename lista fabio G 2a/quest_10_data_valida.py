dia = int(input("Digite o dia: "))
mês = int(input("Digite o mês: "))
ano = int(input("Digite o ano: "))
if dia > 31 or mês == 2 and dia > 30 or mês > 12:
    print("Data inválida")
else:
    print("Data válida")