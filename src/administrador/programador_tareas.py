from administrador import Tareas

class ProgramadorTareas:
    def __init__(self, target):
        self.tareas = Tareas()
        self.tareas.setTarget(target)
    
    def getTareas(self):
        return self.tareas

    def setTarea(self, tarea):
        self.tareas.addTarea(tarea)

    def ejecutarTarea(self, mensaje):
        self.tareas.ejecucion(mensaje)