""" 
Funciones
Lambdas -> Funcion anonima simple y limitada a una 
Maps -> 
Filters-> 
"""
''' Funcion para saludar'''
def saludar() -> None:
    #funcion para saludar
    print("Tenemos hambreeeeee")

''' Funcion para saludar personalizado'''
def saludarPersona(nombre: str) -> None:
    print(f"Hola, {nombre}")
    
    
saludar()
saludarPersona("Cesar")

""" 
Funcion que muestra el precio final de un producto con el IVA aplicando.
"""
def precio_final(precio_base: float) -> None: 
    iva_aplicable: float = 0.16
    monto_iva: float = precio_base * iva_aplicable
    precio_final: float = precio_base + monto_iva
    print(f"El precio total de producto es: {round(precio_final, 2)}")

precio_final(147)
    