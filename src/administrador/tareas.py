class Tareas:
    
    def __init__(self):
        self.tareas = []
        self.target = ""

    def getTareas(self):
        return self.tareas
    
    def getTarget(self):
        return self.target
    
    def setTarget(self, target):
        self.target = target
    
    def addTarea(self, tarea):
        self.tareas.append(tarea)

if __name__ == "__main__":
    tareas = Tareas()
    tareas.addTarea("Autentificacion")
    tareas.addTarea("Autorizacion")
    tareas.setTarget("Vehiculo")
    print(tareas.getTareas())
    print(tareas.getTarget())
    