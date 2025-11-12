""" #Args y kwargs

# args: argumentyos posicionales
def procesar_datos(*args) -> None:
    print(f"Argumentos posicionales recibidos: {args}")

procesar_datos(2,3,4)

# kwargs: argumentos nombrados
def saludo_dinamico(**kwarg) -> None:
    print(f"Saludos a cualquiera{kwarg}")

saludo_dinamico(nombre = "Cesar", edad=30) """

#Generadores-> Se usan para manejar grandes volumenes de datos, utiliza yield en lugar de return

def generar_datos(limite: int):
    ''' Generador que produce numeros hasta un limite dado '''
    print("Inicio del generador")
    for num in range(limite):
        print(f"Bucle en posicion: {num}")
        yield num
    print("Fin del generador")

print("Uso del generador")
generador = generar_datos(5)

for item in generador:
    print(f"Valor generado: {item}")

# Ejercicio de generador para calcular la serie fibonacci
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

for num in fibonacci(10):
    print(num, end = " ")        