def linhas(arroz):
    print(arroz)

def colunas(feijao):
    print(feijao)

def quatro_linhas_quatro_colunas(u, o): #chama as outras funções e atribui as mesmas variáveis na mesma ordem
    linhas(u)
    colunas(o)
    linhas(u)
    colunas(o)
    linhas(u)
    colunas(o)
    linhas(u)
    colunas(o)
    linhas(u)


x = "+ - - - - + - - - - + - - - - + - - - - +"
y = "|         |         |         |         |"
quatro_linhas_quatro_colunas(x, y) #chama a função e atribui dois argumentos para ela