multiplicando = 1
contador = 1
while multiplicando != 11 and contador != 11:
    resultado = multiplicando * contador
    print(f"{multiplicando} X {contador} = {resultado}")
    contador += 1
    if contador == 11:
        print("-+" * 30)
        multiplicando += 1
        contador = 1
        
    
