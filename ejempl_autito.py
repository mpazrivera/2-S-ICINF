class Vehiculo():
    # Constructor de la clase vehiculo
    # Atributos de la clase vehiculo (características compartidas por todos los objetos de la clase)
    def __init__(self, marca, modelo, año, color):
        self.marca = marca
        self.modelo = modelo
        self.año = año
        self.color = color 

    # Métodos de la clase vehiculo (comportamientos)
    def acelerar (self):
        print(f"el {self.marca} esta acelerando")

    def frenar(self):
        print(f"el {self.marca} está frenando")

# Creando un objeto de la clase 
audi = Vehiculo("Audi", "R8", 2018, 'negro') 
toyota = Vehiculo("Toyota", "Corolla", 2020,"blanco")
ford = Vehiculo("Ford", "focus", 1,"azul")

# Impresión de los atributos de los objetos
print(f"La marca del auto es: {audi.marca}")
print(f"El modelo del 2° auto es: {toyota.modelo}")
print(f"La marca del 3° auto es: {ford.marca}")

# Llamada a los métodos de los objetos
audi.acelerar()
toyota.acelerar()
ford.frenar()