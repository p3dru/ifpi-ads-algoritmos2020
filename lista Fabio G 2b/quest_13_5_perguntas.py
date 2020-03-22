print("Responda Sim ou Não para as próximas perguntas")
print("Telefonou para a vítima ?")
soma = 0
resposta_1 = input("Resposta: ")
print("Esteve no local do crime ?")
resposta_2 = input("Resposta: ")
print("Mora perto da vítima ?")
resposta_3 = input("Resposta: ")
print("Devia para a vítima ?")
resposta_4 = input("Resposta: ")
print("Já trabalhou com a vítima ?")
resposta_5 = input("Resposta: ")
if resposta_1 == "Sim" or resposta_1 == "S" or resposta_1 == "SIM" or resposta_1 == "sim":
    soma += 1
else:
    soma += 0
if resposta_2 == "Sim" or resposta_2 == "S" or resposta_2 == "SIM" or resposta_2 == "sim":
    soma += 1
else:
    soma += 0
if resposta_3 == "Sim" or resposta_3 == "S" or resposta_3 == "SIM" or resposta_3 == "sim":
    soma += 1
else:
    soma += 0
if resposta_4 == "Sim" or resposta_4 == "S" or resposta_4 == "SIM" or resposta_4 == "sim":
    soma += 1
else:
    soma += 0
if resposta_5 == "Sim" or resposta_5 == "S" or resposta_5 == "SIM" or resposta_5 == "sim":
    soma += 1
else:
    soma += 0
if soma == 2:
    print("Suspeito")
elif 2 < soma <= 4:
    print("Cúmplice")
elif soma > 4:
    print("Assassino")
else:
    print("Inocente")