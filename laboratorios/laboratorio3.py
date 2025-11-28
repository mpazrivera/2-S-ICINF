#clases prinipales
class Contenido:
    def __init__(self, titulo= str, anio =int):
        self.titulo = titulo
        self.anio = anio

    def mostrar_detalle(self)->str:
        print(f"Titulo: {self.titulo},año: {self.anio}")

class Reproducible:
    def reproducir(self):
        pass

class Calificable:
    def __init__(self, rating = float):
        self.rating = 0.0

    def calificar (self)->str:
        print (f"El rating es: {self.rating}")

#subclases
class Película(Contenido, Reproducible):
    def __init__(self, titulo = str, anio = int, duracion_minutos = int):
        super().__init__(titulo, anio)
        self.duracion_minutos = duracion_minutos

    def reproducir(self)->str :
        print(f"Reproduciendo""{self.titulo}", "duración: {self.anio}")
    
class Documental(Contenido):
    def __init__(self, titulo=str, anio=int, tema = str):
        super().__init__(titulo, anio)
        self.tema = tema

    def reproducir (self):
        pass

class Miniserie (Contenido, Reproducible, Calificable):
    def __init__(self, titulo=str, anio=int, rating = float, num_episodios = int):
        Contenido().__init__(titulo, anio) 
        Reproducible().__init__()
        Calificable().__init__(rating)
        self.num_episodios = num_episodios

    def reproducir(self)-> str: 
        print(f"Se esta reproduciendo la serie {self.titulo}, del año: {self.anio}, rating: {self.rating}, num_episodios: {self.num_episodios}")


#creación de objetos
#peli1 = Película("Eterno", 2025, 107)
doc1 = Documental("Las aventuras de pepe",2006, "entretención")
minis1 = Miniserie("Peppa pig", 2000, 4.5, 9)


minis1.reproducir()
minis1.calificar()
minis1.mostrar_detalle()