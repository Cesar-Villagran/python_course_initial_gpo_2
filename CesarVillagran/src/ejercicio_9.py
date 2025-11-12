""" 
Modelado de objetos mediante composicion y herencia
 """
class Motor:
    def __init__(self, tipo:str):
        self.tipo = tipo

class Rueda:
    def __init__(self, tamano: int):
        self.tamano = tamano

class Coche:
    def __init__(self, marca: str, motor: Motor, ruedas: list[Rueda]):
        self.marca = marca
        self.motor = motor
        self.ruedas = ruedas

        def descripcion(self):
            print(f"Coche marca: {self.marca}")
            print(f"Tipo de motor: {self.motor.tipo}")
            print(f"Coche marca: {len(self.ruedas)}")

auto_uno = Coche(
    marca="Nissan",
    motor="Gasolina",
    ruedas=[1,2,3,4]
)