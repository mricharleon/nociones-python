# En ocasiones se requiere lanzar excpeciones para poder ver el flujo del programa
try:
    raise TypeError
except TypeError:
    print('Se ha producido un error de tipo')
