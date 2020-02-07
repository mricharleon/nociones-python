# se usan metodos que son comunes entre dos o mas clases

class Perro():
    def avanzar(self):
        print('Caminando')

class Aguila():
    def avanzar(self):
        print('volando')

# se define un metodo que va ser el encargado de establecer el vinculo entre el metodo en comun de las clases
def mover(animal):
    animal.avanzar()

# se crean las instancias de las clases previamente creadas
p = Perro()
a = Aguila()

# se llama al metodo con su respectivo objeto como parametro
mover(p)
mover(a)