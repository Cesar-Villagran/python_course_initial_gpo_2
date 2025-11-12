import logging


class CustomError(Exception):
    pass

def funcion_con_error(n1: int):
    if(n1 < 0):
        raise CustomError("Ocurrio un Errro")
    logging.info("El numero es correcto.")

try:
    funcion_con_error(-5)
except Exception as e:
    logging.error(f"Error: {e}")
else:
    logging.info("Ejecucion correcta")
finally:
    logging.info("Ejecucion finalizada")