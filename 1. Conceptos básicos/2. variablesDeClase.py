# Las variables de clase son las que estan ligadas a la clase en general, no se requiere una instancia

class Estudiante():
    # variable de clase que esta definida directamente dentro de la clase y no precede de la palabra reservada self
    edad = 15
    def __init__(self, nombre, apellido):
        self.nombre=nombre
        self.apellido=apellido

# se imprime el valor de las variables de clase, sin necesidad de crear una instancia
print(Estudiante.edad)