# La introspeccion nos sirve para indagar en que tenemos dentro de nuestras clases, objetos

class Introspeccion():
    def __init__(self, valor):
        self.valor=valor

    def segundoMetodo(self):
        print('Segundo metodo')

    def tercerMetodo(self):
        print('Tercer metodo')

# se crea una instancia de la clase
dato = Introspeccion('val')
# se visualiza la informacion que contiene el objeto
print(dir(dato))

# forma de comprobar si dato es instancia de determinada clase es este caso Introspeccion
print(isinstance(dato, Introspeccion))

# forma de comprobar si dato contiene cierto atributo
print(hasattr(dato, 'tercerMetodo'))
