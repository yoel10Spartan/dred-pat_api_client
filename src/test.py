def mi_decorador(funcion):
    def nueva_funcion(a, b):
        print("Se va a llamar")
        c = funcion(a, b)
        print("Se ha llamado")
        return c
    return nueva_funcion

class Hola:
    decorador = 0
    
    def __init__(self, decorator) -> None:
        self.decorator = decorator

    