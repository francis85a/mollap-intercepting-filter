from filtro import Filtro

class Autentificacion(Filtro):

    def ejecucion (self, cliente):
        print("Autentificacion ok " + cliente + "!")