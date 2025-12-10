class Animal:
    def __init__(self, nombre, edad, peso, genero):
        self.nombre = nombre
        self.edad = edad
        self.peso = peso    # Atributo: peso (en kg)
        self.genero = genero # Atributo: genero

    def dormir(self):
        # 2. Método General: dormir
        print(f"💤 {self.nombre} está durmiendo.")

    def mostrar_ficha(self):
        # 3. Método de Ficha: Muestra atributos base
        print("--- Ficha Base del Animal ---")
        print(f"Nombre: {self.nombre}")
        print(f"Edad: {self.edad} años")
        print(f"Peso: {self.peso} kg")
        print(f"Género: {self.genero}")

class Perro(Animal):
    def __init__(self, nombre, edad, peso, genero, raza):
        # 1. Actualizar __init__: Usar super() para la inicialización base
        super().__init__(nombre, edad, peso, genero)
        self.raza = raza # Atributo específico

    def mostrar_ficha(self):
        # 2. Sobrescribir mostrar_ficha
        super().mostrar_ficha() # a. Llama al método de la superclase
        # b. Imprime el atributo específico
        print(f"Raza: {self.raza}")
        
    def ladrar(self):
        print(f" {self.nombre} dice: ¡Guau! ¡Guau!")


class Gato(Animal):
    def __init__(self, nombre, edad, peso, genero, color_pelaje):
        # 1. Actualizar __init__: Usar super() para la inicialización base
        super().__init__(nombre, edad, peso, genero)
        self.color_pelaje = color_pelaje # Atributo específico

    def mostrar_ficha(self):
        # 2. Sobrescribir mostrar_ficha
        super().mostrar_ficha() # a. Llama al método de la superclase
        # b. Imprime el atributo específico
        print(f"Color de Pelaje: {self.color_pelaje}")
        
    def maullar(self):
        """Método específico de Gato."""
        print(f" {self.nombre} dice: ¡Miau!")


class Pajaro(Animal):
    def __init__(self, nombre, edad, peso, genero, color_plumaje):
        # a. Debe heredar de Animal y usar super()
        super().__init__(nombre, edad, peso, genero)
        # b. Atributo específico
        self.color_plumaje = color_plumaje 

    def volar(self):
        # c. Método nuevo y específico
        print(f" {self.nombre} está volando alto.")
        
    def mostrar_ficha(self):
        # d. Sobrescribir mostrar_ficha (usando super() + específico)
        super().mostrar_ficha()
        print(f"Color de Plumaje: {self.color_plumaje}")
       
if __name__ == "__main__":

    print("\n--- PERRO: 'Max' ---")
    max_perro = Perro(nombre="Max", edad=4, peso=30.5, genero="Macho", raza="Pastor Alemán")
    max_perro.mostrar_ficha()     # Sobrescrito (llama a super)
    max_perro.ladrar()            # Específico
    max_perro.dormir()            # Heredado

    print("\n--- GATO: 'Luna' ---")
    luna_gato = Gato(nombre="Luna", edad=2, peso=4.1, genero="Hembra", color_pelaje="Gris Atigrado")
    luna_gato.mostrar_ficha()     # Sobrescrito (llama a super)
    luna_gato.maullar()           # Específico
    luna_gato.dormir()            # Heredado

    print("\n--- PÁJARO: 'Chirri'")
    chirri_pajaro = Pajaro(nombre="Chirri", edad=1, peso=0.1, genero="Macho", color_plumaje="Amarillo y Verde")
    chirri_pajaro.mostrar_ficha() 
    chirri_pajaro.volar()        
    chirri_pajaro.dormir()       