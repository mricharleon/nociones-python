# Las variables de instancia son aquellas que estan estrictamente relacionadas con la instancia de una clase

class Estudiante():
    # el atributo self es necesario
    def __init__(self, nombre, apellido):
        # son variables de instancia ya que estan precesdidas de la palabra reservada self
        self.nombre=nombre
        self.apellido=apellido

# se crea la instancia 
estudiante1 = Estudiante('Carlos', 'Perez')
# se imprime el valor de las variables de instancia, nombre y apellido
print(estudiante1.nombre, estudiante1.apellido)