# existen varios metodos especiales en python esta ocasion esta el metodo new e init

class Clase():
    # metodo especial __new__()
    # primero se invoca el new, antes del init
    # no requiere un parametro self
    # recibe una referencia a la clase que lo esta invocando, devuelve un objeto
    def __new__(cls):
        print('Ejecutando __new__()')
        # se usa super para poder retornar el objeto y seguir con el metodo init
        return  super().__new__(cls)

    # metodo especial __init__()
    def __init__(self):
        print('Ejecutando __init__()')

# se crea una instancia para ver el funcionamiento
c = Clase()