valor_1 = int(input("Digite um valor: "))
valor_2 = int(input("Digite outro valor: "))
print(                  "Digite 1 para somar\nDIgite 2 para subtrair"
                  "\nDigite 3 para multiplicar\n"
                  "Digite 4 para dividir")
opcao = int(input("O que deseja fazer? "))
if opcao == 1:
    print(valor_1 + valor_2)
elif opcao == 2:
    print(valor_1 - valor_2)
elif opcao == 3:
    print(valor_2 * valor_1)
elif opcao == 4:
    print(valor_1 / valor_2)
else:
    print("Opção inválida, tente novamente...")