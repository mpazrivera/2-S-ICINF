class Libro:
    def __init__(self, titulo, autor, anio_publicacion, cantidad_disponible):
        # Atributos [cite: 75]
        self.titulo = titulo
        self.autor = autor
        self.anio_publicacion = anio_publicacion
        self.cantidad_disponible = cantidad_disponible

    def __str__(self):
        """Representación en texto de la información del libro."""
        return (f"{self.titulo} - {self.autor} ({self.anio_publicacion})\n"
                f"   Disponibles: {self.cantidad_disponible}")

    def actualizar_stock(self, cambio):
        """Actualiza la cantidad disponible del libro."""
        if self.cantidad_disponible + cambio >= 0:
            self.cantidad_disponible += cambio
            print(f" Stock de '{self.titulo}' actualizado. Nuevo stock: {self.cantidad_disponible}")
        else:
            print(f" Error: No hay suficientes copias de '{self.titulo}' para realizar el cambio.")

class Biblioteca:
    """
    Clase que gestiona una colección de libros.
    """
    def __init__(self):
        # Atributo: diccionario de libros donde la clave es el título y el valor es la instancia Libro [cite: 77]
        self.libros = {} 

    def agregar_libro(self, libro):
        """
        Agrega un nuevo libro a la biblioteca o actualiza el stock si ya existe.
        """
        # Los libros se pueden agregar [cite: 78]
        if libro.titulo in self.libros:
            print(f"El libro '{libro.titulo}' ya existe. Se añade al stock existente.")
            self.libros[libro.titulo].cantidad_disponible += libro.cantidad_disponible
        else:
            self.libros[libro.titulo] = libro
            print(f"Libro '{libro.titulo}' agregado a la biblioteca.")

    def buscar_libro(self, titulo):
        # Permitir la búsqueda de libros por título [cite: 76, 78]
        titulo_normalizado = titulo.strip() 
        if titulo_normalizado in self.libros:
            print(f"\n Libro encontrado:")
            print(self.libros[titulo_normalizado])
            return self.libros[titulo_normalizado]
        else:
            print(f"Libro con título '{titulo}' no encontrado.")
            return None

    def actualizar_libro(self, titulo, cambio_stock):
        # Los libros se pueden actualizar [cite: 78]
        libro = self.buscar_libro(titulo)
        if libro:
            libro.actualizar_stock(cambio_stock)

    def mostrar_inventario(self):
        print("\n=== Inventario de la Biblioteca ===")
        if not self.libros:
            print("La biblioteca está vacía.")
            return
        
        for libro in self.libros.values():
            print("---")
            print(libro)
        print("-----------------------------------")


# Ejemplo de Uso:
if __name__ == "__main__":
    biblioteca = Biblioteca()

    # Agregar libros
    libro1 = Libro("Cien Años de Soledad", "García Márquez", 1967, 5)
    libro2 = Libro("El Señor de los Anillos", "J.R.R. Tolkien", 1954, 3)
    
    biblioteca.agregar_libro(libro1)
    biblioteca.agregar_libro(libro2)
    biblioteca.mostrar_inventario()

    # Buscar libro
    biblioteca.buscar_libro("Cien Años de Soledad")

    # Actualizar stock (préstamo/devolución)
    print("\n--- Actualización de Stock (Préstamo) ---")
    biblioteca.actualizar_libro("El Señor de los Anillos", -1) # Prestar 1
    
    print("\n--- Inventario Final ---")
    biblioteca.mostrar_inventario()