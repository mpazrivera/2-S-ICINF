
class Gato:
    contador_id = 1  

    def __init__(self, nombre, edad, color, raza, salud, peso):
        self.nombre = nombre
        self.edad = edad
        self.color = color
        self.__id = Gato.contador_id
        self.__raza = raza
        self.__salud = salud
        self.__peso = peso
        self.energia = 100
        self.hambre = 0
    
        self.__historial = ["Se creó el gato"]

        Gato.contador_id += 1

    def obtener_id(self):
        return self.__id

    def obtener_raza(self):
        return self.__raza

    def obtener_salud(self):
        return self.__salud

    def obtener_peso(self):
        return self.__peso

    def modificar_salud(self, nueva_salud):
        self.__salud = nueva_salud
        self.__historial.append("Salud cambiada a " + nueva_salud)

    def modificar_peso(self, nuevo_peso):
        self.__peso = nuevo_peso
        self.__historial.append("Peso cambiado a " + str(nuevo_peso))


    def jugar(self):
        if self.energia >= 20:
            self.energia -= 20
            self.hambre += 20
            self.__historial.append("Jugó y gastó energía")
            print(self.nombre, "jugó. Energía:", self.energia, "Hambre:", self.hambre)
        else:
            print(self.nombre, "está muy cansado para jugar.")

    def alimentar(self):
        self.energia += 20
        self.hambre -= 20
        if self.energia > 100:
            self.energia = 100
        if self.hambre < 0:
            self.hambre = 0
        self.__historial.append("Comió y recuperó energía")
        print(self.nombre, "comió. Energía:", self.energia, "Hambre:", self.hambre)

    def mostrar_historial(self):
        print("Historial de", self.nombre)
        for h in self.__historial:
            print(" -", h)

    def __str__(self):
        return f"Gato: {self.nombre}, Edad: {self.edad}, Color: {self.color}, Energía: {self.energia}, Hambre: {self.hambre}, Raza: {self.__raza}, Salud: {self.__salud}, Peso: {self.__peso} kg"


class Espacio:
    def __init__(self, nombre_lugar, capacidad_maxima):
        self.nombre_lugar = nombre_lugar
        self.capacidad_maxima = capacidad_maxima
        self.__gatos = []

    def agregar_gato(self, gato):
        if len(self.__gatos) < self.capacidad_maxima:
            self.__gatos.append(gato)
            print(gato.nombre, "ha sido agregado al espacio", self.nombre_lugar)
        else:
            print("No se puede agregar a", gato.nombre, ". El espacio", self.nombre_lugar, "está lleno.")

    def mostrar_gatos(self):
        print("Gatos en el espacio", self.nombre_lugar)
        for gato in self.__gatos:
            print(" -", gato.nombre, "Edad:", gato.edad, "Raza:", gato.obtener_raza(), "Peso:", gato.obtener_peso(), "kg")

if __name__ == "__main__":
    # crear gatos
    gato1 = Gato("Ruperta", 2, "Blanco", "Persa", "Buena", 5)
    gato2 = Gato("Blanca", 3, "Negro", "Bengalí", "Buena", 4.5)
    gato3 = Gato("Oreo", 1, "Blanco con negro", "Siamés", "Regular", 4.5)
    gato4 = Gato("Mango", 2, "Anaranjado", "Bengalí", "Mala", 4.0)
    gato5 = Gato("Copito", 4, "Gris", "British Shorthair", "Buena", 4.5)
    # crear espacios
    terraza = Espacio("Terraza", 2)
    salon = Espacio("Salón", 4)

    # agregar gatos
    terraza.agregar_gato(gato1)
    terraza.agregar_gato(gato2)
    terraza.agregar_gato(gato4)  # no debería entrar
    salon.agregar_gato(gato3)
    salon.agregar_gato(gato5)

    # mostrar gatos en espacios
    terraza.mostrar_gatos()
    salon.mostrar_gatos()

    # interacciones
    gato2.jugar()
    gato4.alimentar()

    # mostrar historial
    gato2.mostrar_historial()

    # mostrar estado de un gato
    print(gato1)

    # simular que un gato salió
    print("El gatito", gato5.nombre, "salió del lugar")