try:
    # Intento para cuando ejecutas desde la raíz (main)
    from administrador.tareas import Tareas
except ImportError:
    # Intento para cuando ejecutas el archivo solo (test individual)
    from tareas import Tareas
    
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


if __name__ == "__main__":
    print("--- Probando ProgramadorTareas ---")
    
    # 1. Creamos el programador con un target de prueba (un simple string)
    prog = ProgramadorTareas("Vehiculo_Prueba")

    # 2. Comprobamos que el objeto Tareas se ha creado
    print(f"¿Objeto Tareas creado?: {prog.getTareas() is not None}")

    # 3. Añadimos un filtro de prueba
    prog.setTarea("Autentificacion_Prueba")

    # 4. Probamos el disparo de ejecución
    prog.ejecutarTarea("Francisco")

    print("--- Test de Programador Finalizado ---")