from filtro import Filtro

class Autentificacion(Filtro):

    def ejecucion (self, cliente):
        print("Autentificacion ok " + cliente + "!")

if __name__ == "__main__":
    autentificacion = Autentificacion()
    autentificacion.ejecucion("Francisco")