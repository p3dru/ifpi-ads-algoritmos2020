#entrada
horas = int(input("Digite uma quantidade de horas: "))
#processamento
semanas = (horas // 24) // 7
dias = (horas // 24) % 7
horas_restantes = horas % 24
#saida
print(f"{horas} horas correspondem à {semanas} semanas, {dias} dias e {horas_restantes} horas")

#achei a resposta certa dessa questãos sem querer resolvendo a questão 7 kkkkkkkkkkkk
#era tão simples, bastava lembrar o que eram as horas restantes