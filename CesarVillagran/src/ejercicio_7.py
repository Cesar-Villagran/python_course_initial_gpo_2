class Producto:

    def __init__(self, nombre: str): 
        """ Constructor de la clase """
        self._nombre = nombre

    @property
    def nombre(self) -> str:
        """ Permite acceder a la propiedad del nombre de forma segura """
        return self._nombre
    
    @nombre.setter
    def nombre(self, nuevo_nombre):
        if(len(nuevo_nombre) < 1):
            raise ValueError("El nombre no puede estar vacio")
        self._nombre = nuevo_nombre

