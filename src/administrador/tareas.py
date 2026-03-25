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

    def ejecucion(self, cliente: str):

        for filtro in self.tareas:

            if isinstance(filtro, str):
                print(f"Ejecutando filtro (string): {filtro}")
            else:
                filtro.ejecucion(cliente)
        
        if self.target:
            if isinstance(self.target, str):
                print(f"Ejecutando Target (string): {self.target} para {cliente}")
            else:
                self.target.ejecucion(cliente)

if __name__ == "__main__":
    tareas = Tareas()
    tareas.addTarea("Autentificacion")
    tareas.addTarea("Autorizacion")
    tareas.setTarget("Vehiculo")
    print(tareas.getTareas())
    print(tareas.getTarget())
    