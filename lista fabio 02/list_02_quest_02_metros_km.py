#entrada
metros = int(input("Digite um valor em metros: "))
#processamento
km = metros // 1000
metros_restantes = metros % 1000
#saida
print(f"{metros} metros equivalem à {km} km e {metros_restantes} metros")