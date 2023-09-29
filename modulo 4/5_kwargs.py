# **Kwargs(Keyword arguments)
def concatenar(**palavras):
    frase = ''
    for palavra in palavras.values():
        frase += palavra + ' '
    print(frase)

concatenar(a='Nós', b='somos', c='Pythonistas', d='profissionais')

def fazer_calculo(nome, *args, **kwargs):
    print(nome)
    print(args)
    print(kwargs)
    for arg in args:
        print(arg)
    for kwarg in kwargs:
        print(kwarg)

fazer_calculo('Daniel',4,3,5,a=4, b=5, c=3)