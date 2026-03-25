from target import Target

class vehiculo(Target):

    def ejecucion(self, cliente: str):
        print("Puerta abierta" + " " + cliente + "!")

if __name__ == "__main__":
    vehiculo = vehiculo()
    vehiculo.ejecucion("Francisco")