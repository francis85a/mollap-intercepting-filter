class Cliente():

    def set_programador_tareas(self, programador):
        pass

    def enviar_peticion(self, peticion: str):
        pass
    

if __name__ == "__main__":
    print("--- Probando Clase Base Cliente ---")
    
    # 1. Instanciamos la clase
    cliente_test = Cliente()

    # 2. Probamos set_programador_tareas con un string simple
    # Solo para ver que el método acepta el argumento y hace el print
    cliente_test.set_programador_tareas("Programador_Prueba_1")

    # 3. Probamos enviar_peticion
    cliente_test.enviar_peticion("LOGIN_USER")

    print("--- Test de Cliente Finalizado ---")