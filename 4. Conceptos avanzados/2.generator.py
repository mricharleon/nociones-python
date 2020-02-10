# Los generadores son objetos invocables,
# tales como las funciones y los métodos, los cuales implementan un método __next__(). Por lo general esto se realiza utilizando la expresión yield.

def numeros():
    n=1
    while True:
        # Esta expresión regresa un objeto del ámbito local de una función al ámbito superior de ésta,
        # pero a diferencia de return la función no es terminada, sino que continúa su ejecución.
        yield n
        n=n+1

i=numeros()
print(i)
print(i.__next__())
print(i.__next__())
print(i.__next__())
print(i.__next__())
print(i.__next__())
