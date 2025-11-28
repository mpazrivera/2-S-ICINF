class Persona:
    def __init__(self, nombre, edad, altura: float, peso: float):
        self.nombre = nombre
        self.edad = edad
        self.altura = altura  
        self.peso = peso 

    def saludar(self):
        print(f"Hola, mi nombre es {self.nombre} y tengo {self.edad} años.")

    def calcular_imc(self):
        if self.altura <= 0:
            print("Error: La altura debe ser un valor positivo para calcular el IMC.")
            return None

        # Cálculo del IMC: peso / altura al cuadrado
        imc = self.peso / (self.altura ** 2)

        # Clasificación del IMC
        if imc < 18.5:
            mensaje_estado = "Bajo Peso"
        elif 18.5 <= imc < 25.0:
            mensaje_estado = "Peso Normal"
        elif 25.0 <= imc < 30.0:
            mensaje_estado = "Sobrepeso"
        else: # imc >= 30.0
            mensaje_estado = "Obesidad"

        print(f"El IMC de {self.nombre} es: {imc:.2f}")
        print(f"Clasificación según el IMC: {mensaje_estado}")

        return imc

    def promedio_asignatura(self, nota1: float, nota2: float, nota3: float):
        promedio = (nota1 + nota2 + nota3) / 3

        print(f"Promedio de Notas para {self.nombre}")
        print(f"Notas: {nota1}, {nota2}, {nota3}")
        print(f"Promedio calculado: {promedio}")

        if promedio >= 4.0:
            print(f"¡Felicidades! {self.nombre} APROBÓ la asignatura.")
        else:
            print(f"Lo siento, {self.nombre} NO APROBÓ la asignatura.")

        return promedio

# Crear una instancia de Persona (Nombre, Edad, Altura, Peso)
persona1 = Persona("Ana López", 30, 1.70, 75.5)
persona2 = Persona("Carlos Ruiz", 22, 1.85, 68.0)

print(f"IMC de {persona1}")
persona1.calcular_imc()

persona2.calcular_imc() 

persona1.promedio_asignatura(5.5, 3.8, 4.2)
persona2.promedio_asignatura(3.0, 3.5, 3.9)