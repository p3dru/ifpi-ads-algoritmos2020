horas_prof_1 = float(input("Digite a quantidade de horas trabalhadas: "))
valor_hora_prof_1 = float(input("Quanto recebe pora hora/aula: "))
horas_prof_2 = float(input("Digite a quantidade de horas trabalhadas: "))
valor_hora_prof_2 = float(input("Quanto recebe pora hora/aula: "))
total_prof_1 = horas_prof_1 * valor_hora_prof_1
total_prof_2 = horas_prof_2 * valor_hora_prof_2
if total_prof_1 > total_prof_2:
    print("O primeiro professor recebe o maior salário.")
elif total_prof_2 > total_prof_1:
    print("O segundo professor recebe o maior salário.")
else:
    print("Os professores recebem a mesma quantia.")