# EJEMPLO 1
def Lower(elementos):
    return elementos.lower()

lista = ['JUAN', 'Pedro', 'AlexAnDRa']

print([cad.lower() for cad in lista])
# Se aprovecha las bondades de la programación funcional
print(list(map(Lower, lista)))



# EJEMPLO 2
# Funcion de orden superior
def saludo(idioma):
    def es():
        print('Hola')
    def en():
        print('Hello')
    idioma_func = {'es':es, 'en':en}

    return idioma_func[idioma]

saludar = saludo('en')
saludar()



# EJEMPLO 3
from functools import reduce

numeros = {1, 3, 2, 4}
def suma(x, y):
    return x + y

sumar = reduce(suma, numeros)
print(sumar)
