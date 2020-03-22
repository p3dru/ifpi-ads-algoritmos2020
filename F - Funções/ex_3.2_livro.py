#passo 1
#def do_twice(f): #pega uma função e executa
#    f()
#    f()


#def print_spam(): #define uma função
#    print('spam')

#do_twice(print_spam) #chama do_twice passando print_spam como argumento

#passo_2
def do_twice(x, y): #só está definindo como chamar em duas vezes a mesma função
    x(y)
    x(y)

#passo 3
#def print_twice(bruce):
#    print(bruce)
#    print(bruce)

#passo 4 com erro
#do_twice(print_twice("spam"))

#passo 4
def do_four(x, y):
    do_twice(x, y)
    do_twice(x, y)

#do_twice(print(), "arroz e feijão") dá erro por conta dos parênteses abertos, já que é uma função, só deixa sem
y = "arroz e feijão"
#do_twice(print, y) chamaria do_twice
do_four(print, y)

"""
#passos olhando a resposta no github
def do_twice(func, arg):
    func(arg)
    func(arg)


def print_twice(arg):
    print(arg)
    print(arg)


def do_four(func, arg):
    do_twice(func, arg)
    do_twice(func, arg)


do_twice(print, 'spam') #aqui ela recebe a função print, e aplica "spam" pra ser printado...  aHAAAAM AGORA EU ENTENDI
print() #com ou sem aspas vazias dá no mesmo

do_four(print, 'spam') #aqui aplica também a função print e aplica "spam" pra ser printado"""


#quando for chamar funções em outras funções, não usar parenteses