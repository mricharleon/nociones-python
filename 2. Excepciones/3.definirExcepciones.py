# Se puede definir excepciones personalizadas
# se crea una clase que hereda de Exception
class Err(Exception):
    def __init__(self, valor):
        print('Fue el error debido a:', valor)

# se lanza la excepción antes creada
try:
    raise Err('test de error')
except Err:
    print('Error escrito')
