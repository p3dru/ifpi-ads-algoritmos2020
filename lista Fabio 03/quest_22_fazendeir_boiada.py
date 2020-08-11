quantidade = int(input("Digite a quantidade de bois que tem: "))
mais_gordo = 0
nid_gordo = 0
mais_magro = 0
nid_magro = 0
for x in range(quantidade):
    nid = int(input("Digite o número de identificação: "))
    nome = input("Digite o nome do boi: ")
    kg = int(input("Digite o peso do boi: "))
    if x == 0:
        mais_gordo = kg
        nid_gordo = nid
        mais_magro = kg
        nid_magro = kg
    else:
        if kg > mais_gordo:
            mais_gordo = kg
            nid_gordo = nid
        elif kg < mais_magro:
            mais_magro = kg
            nid_magro = nid
print(f"O boi mais gordo pesa Kg {mais_gordo:.2f}\nO numero de identificação do mais gordo é {nid_gordo}\n"
      f"O boi mais magro pesa Kg {mais_magro:.2f}\nO numero de identificação do mais magro é {nid_magro}")