# Los metodos estaticos se podria decir son aquellos que abarcan los conceptos anteriores y queda a disposicion de cada desarrollador

class Estudiante():
    def __init__(self):
        pass 

    # en metodos estaticos se requiere una directiva que se denomina @staticmethod (Decorador)
    @staticmethod
    # Declaramosn el metodo estaticos y ademas no requiere ningun parametro
    def escribir():
        print('Estoy escribiendo')

# se llama al metodo estatico previamente creando una instancia
estudiante1 = Estudiante()
# se llama al metodo estatico desde la instancia
estudiante1.escribir()