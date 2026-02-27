from filtro import Filtro

class Autorizacion(Filtro):
    
    def ejecucion (self, cliente):
        print("Autorizacion concedida a " + cliente + "!")


if __name__ == "__main__":
    autorizacion = Autorizacion()
    autorizacion.ejecucion("Francisco")
