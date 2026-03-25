from cliente import Cliente

class Mollapp(Cliente):
    def __init__(self):
        self.programador = None

    def set_programador_tareas(self, programador):
        self.programador = programador
    
    def enviar_peticion(self, id_cliente):
        if self.programador is not None:
            # Según tu diagrama, el cliente llama a ejecutar_tareas
            self.programador.ejecutar_tareas(id_cliente)
        else:
            print("Mollapp: Error - No se puede enviar la petición porque no hay programador.")

if __name__ == "__main__":
    app = Mollapp()
    
    # 1. Comprobamos el estado inicial
    print(f"¿Tiene programador al inicio?: {app.programador}")
    
    # 2. Comprobamos qué pasa si enviamos algo sin configurar
    app.enviar_peticion("Francisco")
    
    # 3. Simulamos la asignación (usando un string solo para ver que se guarda)
    app.set_programador_tareas("Objeto_Programador_Prueba")
    print(f"¿Tiene programador ahora?: {app.programador}")