fichas = int(input("Digite a quantidade de fichas a serem lidas: "))
contador = 1
mais_gordo = id_mais_gordo = mais_magro = id_mais_magro = 0
while contador <= fichas:
    numero_id = int(input("Id: "))
    peso = int(input("Digite o peso: "))
    if contador == 1:
        mais_gordo = mais_magro = peso
        id_mais_gordo = id_mais_magro = numero_id
    else:
        if peso > mais_gordo:
            mais_gordo = peso
            id_mais_gordo = numero_id
        if peso < mais_magro:
            mais_magro = peso
            id_mais_magro = numero_id
    contador += 1
print(f"O boi mais gordo pesa: {mais_gordo:.2f}  Kg\n"
      f"A id do boi mais gordo é: {id_mais_gordo}\n"
      f"O boi mais magro pesa: {mais_magro:.2f} Kg\n"
      f"A id do boi mais magro é: {id_mais_magro}\n")
