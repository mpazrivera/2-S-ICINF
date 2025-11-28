class Fraccion:

    def __init__(self, numerador, denominador):

        if denominador == 0:
            raise ValueError("El denominador no puede ser cero.")
        def calcular_mcd(a, b):
            while b:
                a, b = b, a % b
            return a

        if denominador < 0:
            numerador *= -1
            denominador *= -1

        divisor = calcular_mcd(abs(numerador), abs(denominador))
        self.numerador = numerador // divisor
        self.denominador = denominador // divisor


    def __str__(self):
        """Devuelve la fracción como una cadena (e.g., '2/3')."""
        return f"{self.numerador}/{self.denominador}"

    def __add__(self, otra):
        nuevo_numerador = (self.numerador * otra.denominador) + (otra.numerador * self.denominador)
        nuevo_denominador = self.denominador * otra.denominador
        
        return Fraccion(nuevo_numerador, nuevo_denominador)

    def __mul__(self, otra):
        nuevo_numerador = self.numerador * otra.numerador
        nuevo_denominador = self.denominador * otra.denominador
        
        return Fraccion(nuevo_numerador, nuevo_denominador)

    def __eq__(self, otra):
        return (self.numerador == otra.numerador) and (self.denominador == otra.denominador)

    def valor_decimal(self):
        return self.numerador / self.denominador
    
# Creación (10/15 se simplifica a 2/3)
f1 = Fraccion(10, 15)
f2 = Fraccion(1, 6)
f3 = Fraccion(4, 6)

print(f"F1: {f1}, F2: {f2}, F3: {f3}")

suma = f1 + f2
print(f"Suma: {f1} + {f2} = {suma}")
