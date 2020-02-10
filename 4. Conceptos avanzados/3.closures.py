# Un Closure (cierre) es un objeto de función que recuerda los valores en los ámbitos incluídos,
# incluso si no están presentes en la memoria

def funcionA(x):
    def funcionB(y):
        return x+y
    return funcionB

funcion = funcionA(5)
print(funcion(3))
