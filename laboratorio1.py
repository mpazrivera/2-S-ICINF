class Gatito:
    def __init__(self, nombre, edad, color, nivel_energia, nivel_hambre):
        self.nombre = nombre
        self.edad = edad
        self.color = color
        self.nivel_energia = 100  # 100 es energía máxima
        self.nivel_hambre = 0     # 0 es sin hambre

    #Parte b
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
        return f"Gato: {self.nombre}, Edad: {self.edad}, Energía: {self.nivel_energia}, Hambre: {self.nivel_hambre}"

#Creación de gatitos
gatito1 = Gatito("Ruperta", 2, "Blanco", 100, 0)
gatito2 = Gatito("Blanca", 3, "Negro", 80, 20)
gatito3 = Gatito("Oreo", 1, "Blanco con negro", 60, 40)
gatito4 = input(Gatito)

gatito2.alimentar()
gatito4.alimentar()