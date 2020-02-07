# Los metodos de clase son aquellos que se hace uso sin necesidad de crear una instancia

class Estudiante():
    def __init__(self):
        pass

    # en metodos de clase requiere una directiva que se denomina @classmethod (Decorador)
    @classmethod
    # declaramos el metodo de clase y es necesario el atributo cls
    def leer(cls):
        print('Estoy leyendo')

# se llama al metodo de clase sin necesidad de crear una instancia
Estudiante.leer()