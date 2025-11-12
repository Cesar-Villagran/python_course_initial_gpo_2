import time
#Decoradores
#Medir tiempo de ejecucion de una funcion

def decorador(func):
    def envoltura(*arg, **kwargs):
        inicio = time.time()
        print(f"Tiempo de Inicio: {inicio}")
        ejecucion = func(*arg, **kwargs)
        fin = time.time()
        print(f"Tiempo de ejecucion: {fin - inicio}")
        print(f"Tiempo de finalizacion: {fin}")
        return ejecucion
    return envoltura

@decorador
def enchular():
    time.sleep(1)
    print("Finalizado")
enchular()