def decorador(funcion):
    def funcionDecorada(*args, **kwargs):
        print('Decorando!')
    return funcionDecorada

@decorador
def funcion():
    print('Entro a la función')

funcion()
