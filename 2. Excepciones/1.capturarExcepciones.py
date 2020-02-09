# se crea una lista
lista = [2,5]

# inicia el proceso de excepciones
# se intenta ejecutar una acción en este caso presentar el contenido que tiene el índice 5 de la lista
try:
    print(lista[5])
# en caso de no poder ejecutar lo anterior ya que el índice 5 esta fuera de rango
# se ejecuta la excpeción IndexError (hay varios tipos esta solo es una)
except IndexError:
    print('Error: error en el índice')
# si no se presentase excepción se ejecutaría el else
else:
    print('No existe error')
# finalmente se ejecuta la finalización de la excepción
finally:
    print('Se ejecutó')
