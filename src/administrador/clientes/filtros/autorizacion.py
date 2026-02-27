from filtro import Filtro

class Autorizacion(Filtro):
    
    def ejecucion (self, cliente):
        print("Autorizacion concedida a " + cliente + "!")