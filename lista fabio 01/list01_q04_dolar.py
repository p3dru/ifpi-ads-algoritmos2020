#entrada
dollar = float(input("Valor do dolar: "))
valor_em_dolar = float(input("Digite um valor em dólar a ser convertido: "))

#processamento
converter_para_real = valor_em_dolar * dollar
#saída
print("O preço de {:.2f} dólar(es) é {:.2f} real(is).".format(valor_em_dolar, converter_para_real))
