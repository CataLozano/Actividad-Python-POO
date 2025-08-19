class Motor:
    def arrancar(self):
        print("Motor arrancado")
    
    def apagar(self):
        print("Motor apagado")

class Rueda:
    def inflar(self):
        print("Rueda inflada")
    
    def desinflar(self):
        print("Rueda desinflada")

class Ventana:
    def abrir(self):
        print("Ventana abierta")
    
    def cerrar(self):
        print("Ventana cerrada")

class Puerta:
    def __init__(self):
        self.ventana = Ventana()
    
    def abrir(self):
        print("Puerta abierta")
    
    def cerrar(self):
        print("Puerta cerrada")

class Coche:
    def __init__(self):
        self.motor = Motor()
        self.ruedas = [Rueda() for _ in range(4)]
        self.puertas = [Puerta() for _ in range(2)]
    
    def arrancar(self):
        self.motor.arrancar()
    
    def apagar(self):
        self.motor.apagar()
    
    def inflar_ruedas(self):
        for rueda in self.ruedas:
            rueda.inflar()

    def abrir_puertas(self):
        for puerta in self.puertas:
            puerta.abrir()

    def mostrar_info(self):
        print("Coche con 1 motor, 4 ruedas y 2 puertas listo.")
