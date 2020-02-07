# Las propiedades en python son el resultado de un calculo previo, y se los trata como si fuese variable de clase o instancia pero mucho mas potente y personalizable y sin necesidad de crear un metodo o una funcion

class Circulo():
    def __init__(self, radio):
        self.radio=radio

    # se hace uso del decorador @property
    @property
    def area(self):
        return 3.1416 * (self.radio**2) 

# se crea la instancia con su parametro correspondiente
c = Circulo(10)
# se llama al area como si se tratase de una variable de clase o instancia
print(c.area)