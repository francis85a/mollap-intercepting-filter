from cliente import Cliente

class Mollapp(Cliente):
    def __init__(self):
        self.programador = None

    def set_programador_tareas(self, programador):
        self.programador = programador
    
    def enviar_peticion(self, id):
        self.programador.ejecutar_tareas(id)

