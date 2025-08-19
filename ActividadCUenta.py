class Cuenta:
    def __init__(self, numero_cuenta=None, dni=None, saldo=0.0, interes_anual=0.0):
        import random
        self.numero_cuenta = numero_cuenta if numero_cuenta else random.randint(10000000, 99999999)
        self.dni = dni
        self.saldo = saldo
        self.interes_anual = interes_anual

    # Getters y Setters
    def get_numero_cuenta(self):
        return self.numero_cuenta

    def get_dni(self):
        return self.dni

    def set_dni(self, dni):
        self.dni = dni

    def get_saldo(self):
        return self.saldo

    def set_saldo(self, saldo):
        self.saldo = saldo

    def get_interes_anual(self):
        return self.interes_anual

    def set_interes_anual(self, interes):
        self.interes_anual = interes

    # Métodos
    def actualizarSaldo(self):
        interes_diario = self.interes_anual / 365 / 100
        self.saldo += self.saldo * interes_diario

    def ingresar(self, cantidad):
        self.saldo += cantidad

    def retirar(self, cantidad):
        if cantidad <= self.saldo:
            self.saldo -= cantidad
        else:
            print("Saldo insuficiente")

    def mostrar(self):
        print(f"Cuenta Nº: {self.numero_cuenta}")
        print(f"DNI Cliente: {self.dni}")
        print(f"Saldo: {self.saldo:.2f}")
        print(f"Interés anual: {self.interes_anual}%")