class Gatito:
    def __init__(self, nombre, edad, color, nivel_energia, nivel_hambre, raza, salud, peso):
        self.nombre = nombre
        self.edad = edad
        self.color = color
        self.__raza = raza        
        self.__salud = salud      
        self.__peso = peso 
        self.nivel_energia = 100  
        self.nivel_hambre = 0     

 # Métodos para obtener los valores privados
    def obtener_raza(self):
        return self.__raza

    def obtener_salud(self):
        return self.__salud

    def obtener_peso(self):
        return self.__peso

    # Métodos para modificar los valores privados 
    def modificar_salud(self, nueva_salud):
        self.__salud = nueva_salud

    def modificar_raza(self, nueva_raza):
        self.__raza = nueva_raza

    def modificar_peso(self, nuevo_peso):
        self.__peso = nuevo_peso

    def jugar(self):
        if self.nivel_energia >= 20:
            self.nivel_energia -= 20
            self.nivel_hambre += 20
            print(f"{self.nombre} ha jugado. Energía: {self.nivel_energia}, Hambre: {self.nivel_hambre}")
        else:
            print(f"{self.nombre} está muy cansado para jugar.")

    def alimentar(self):
        self.nivel_energia += 20
        self.nivel_hambre -= 20
        if self.nivel_energia > 100:
            self.nivel_energia = 100
        if self.nivel_hambre < 0:
            self.nivel_hambre = 0
        print(f"{self.nombre} ha comido. Energía: {self.nivel_energia}, Hambre: {self.nivel_hambre}")
    #Parte c
    def __str__(self):
        return f"Gato: {self.nombre}, Edad: {self.edad}, Color: {self.color}, Energía: {self.nivel_energia}, Hambre: {self.nivel_hambre}, Raza: {self.obtener_raza()}, Salud: {self.obtener_salud()}, Peso: {self.obtener_peso()} kg"


#Creación de gatitos
gatito1 = Gatito("Ruperta", 2, "Blanco", 100, 0, "Persa", "Buena", 5,0)
gatito2 = Gatito("Blanca", 3, "Negro", 80, 20,"Bengalí", "Buena", 4.5)
gatito3 = Gatito("Oreo", 1, "Blanco con negro", 60, 40,"Siamés", "Regular", 4.5)
gatito4 = Gatito("Mango", 2, "anaranjado", 40, 60,"Bengalí", "Mala", 4.0)
gatito5 = Gatito("Copito", 4, "Gris", 80, 40,"British Shorthair", "Buena", 4.5)

#Parte 2 
class Espacio:
    def __init__(self, nombre_lugar, capacidad_maxima):
        self.nombre_lugar = nombre_lugar
        self.capacidad_maxima = capacidad_maxima
        self.gatito = []

    def agregar_gatito(self, gatito):
        if len(self.gatito) < self.capacidad_maxima:
            self.gatito.append(gatito)
            print(f"{gatito.nombre} ha sido agregado al espacio {self.nombre}.")
        else:
            print(f"No se puede agregar a {gatito.nombre}. El espacio {self.nombre} está lleno.")

    def mostrar_gatitos(self):
        print(f"Gatitos en el espacio {self.nombre}:")
        for gatito in self.gatito:
            print(f"{gatito.nombre}, Edad: {gatito.edad}, Raza: {gatito.obtener_raza()}, Peso: {gatito.obtener_peso()} kg")


terraza = Espacio("Terraza", 2)
salon = Espacio("Salon", 4)

# Agregar gatos al espacio
terraza.agregar_gatito(gatito1)
terraza.agregar_gatito(gatito2)
terraza.agregar_gatito(gatito4) #este no pudo ingresar
salon.agregar_gatito(gatito3)
salon.agregar_gatito(gatito5)

# Mostrar información de los gatos en el espacio
terraza.mostrar_gatitos()
salon.mostrar_gatitos()

# Interacciones
gatito2.jugar()
gatito4.alimentar()

# Mostrar estado del gato
print(gatito1)

#Mostar que el gatito salio del lugar
print(f"el gatito {gatito5} salio del lugar")
