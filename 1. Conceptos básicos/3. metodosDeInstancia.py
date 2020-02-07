# Los metodos de instancia son aquellas funciones que se hacen uso desde una instancia de clase

class Estudiante():
    edad = 15
    def __init__(self, nombre, apellido):
        self.nombre=nombre
        self.apellido=apellido
    
    # declaramos el metodo de instancia
    # en metodos de instancia se recibe el atributo self
    def estudiar(self):
        print('Estoy estudiando')

# Se crea la instancia de la clase estudiante
estudiante1 = Estudiante('Carlos', 'Perez')
# se llama al metodo de instancia
estudiante1.estudiar()