class Clinica:
    def __init__(self):
        self.turnos = []

    def agregar_turno(self, nombre):
        self.turnos.append(nombre)
        print(f"Turno asignado a {nombre}")

    def mostrar_turnos(self):
        if not self.turnos:
            print("No hay turnos pendientes.")
            return

        print("Turnos pendientes:")
        for idx, nombre in enumerate(self.turnos):
            print(f"{idx + 1}. {nombre}")

    def atender_paciente(self):
        if not self.turnos:
            print("No hay turnos pendientes.")
            return
        
        nombre = self.turnos.pop(0)
        print(f"Atendiendo a {nombre}")

# Ejemplo de uso
if __name__ == "__main__":
    clinica = Clinica()

    # Agregar algunos pacientes
    clinica.agregar_turno("Juan Pérez")
    clinica.agregar_turno("María López")
    clinica.agregar_turno("Carlos Díaz")

    # Mostrar turnos pendientes
    clinica.mostrar_turnos()

    # Atender pacientes
    clinica.atender_paciente()
    clinica.atender_paciente()

    # Mostrar turnos restantes
    clinica.mostrar_turnos()
