#entrada
idade = int(input("Digite sua idade em dias: "))
#processamento
anos = idade // 365
meses = (idade % 365) // 30
dias_restantes = (idade % 365) % 30
#saida
print(f"A idade em dias digitada corresponde à {anos} anos, {meses} meses e {dias_restantes} dias")