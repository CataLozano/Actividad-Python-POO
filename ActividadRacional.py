#ü .Crea una clase Racional que permita trabajar con números racionales (fracciones). Incluye los siguientes métodos: constructores (por defecto y parametrizado), accedentes, leer(), suma, resta, multiplicación, división.

import math

class Racional:
    def __init__(self, numerador=0, denominador=1):
        if denominador == 0:
            raise ValueError("El denominador no puede ser cero")
        self.numerador = numerador
        self.denominador = denominador
        self.simplificar()

    # Accedentes (getters)
    def get_numerador(self):
        return self.numerador
    
    def get_denominador(self):
        return self.denominador

    # Leer valores
    def leer(self):
        self.numerador = int(input("Ingrese numerador: "))
        self.denominador = int(input("Ingrese denominador: "))
        if self.denominador == 0:
            raise ValueError("El denominador no puede ser cero")
        self.simplificar()

    # Operaciones
    def suma(self, otro):
        return Racional(self.numerador * otro.denominador + otro.numerador * self.denominador,
                        self.denominador * otro.denominador)

    def resta(self, otro):
        return Racional(self.numerador * otro.denominador - otro.numerador * self.denominador,
                        self.denominador * otro.denominador)

    def multiplicacion(self, otro):
        return Racional(self.numerador * otro.numerador,
                        self.denominador * otro.denominador)

    def division(self, otro):
        return Racional(self.numerador * otro.denominador,
                        self.denominador * otro.numerador)

    # Simplificación automática
    def simplificar(self):
        mcd = math.gcd(self.numerador, self.denominador)
        self.numerador //= mcd
        self.denominador //= mcd

    def __str__(self):
        return f"{self.numerador}/{self.denominador}"