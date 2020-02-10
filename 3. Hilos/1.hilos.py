# los hilos se utilizan cuando se quiere realizar varias tareas a la vez
# los hilos comparten el espacio de memoria a diferencia de los procesos que tienen memoria reservada para cada uno de ellos
# revisar el código antes de ejcutar ya que los hilos pueden quedarse en memoria ejecutandose
import threading
import time

# se define la clase MiHilo que va ser la encargada de generar los hilos
class MiHilo(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    # Se ejecuta las acciones del hilo
    def run(self):
        # se imprime el nombre del hilo que empieza a ejecutarse
        print('{} iniciado'.format(threading.currentThread().getName()))
        # pausa de un segundo para poder entender mejor
        time.sleep(1)
        #se imprime el nombre del hilo que termina de ejecutarse
        print('{} Terminado'.format(self.getName()))

# estas sentencias ejecutan el archivo
if __name__ == "__main__":
    for x in range(4):
        hilo = MiHilo()
        hilo.start()
        time.sleep(.25)
