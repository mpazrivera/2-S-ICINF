class Carrito:
    def __init__(self):
        # Lista de títulos agregados por el/la cliente (privada)
        self.__titulos = [] 

    # --- Accesor ---
    def obtener_titulos(self):
        """Devuelve la lista de títulos en el carrito."""
        return self.__titulos

    # --- Mutador ---
    def agregar_titulo(self, titulo):
        """Agrega un título al carrito."""
        self.__titulos.append(titulo)

    # --- Mutador ---
    def limpiar_carrito(self):
        """Vacía la lista de títulos."""
        self.__titulos = []
        
    def __len__(self):
        return len(self.__titulos)


class Libreria:
    # Tasa de descuento fija para clientes frecuentes, inicia con 5%
    __DESCUENTO_SOCIOS = 0.05 
    # Mínimo y máximo para el descuento (Invariante de Clase)
    __MIN_DESCUENTO = 0.05
    __MAX_DESCUENTO = 0.10

    def __init__(self, nombre):
        # Nombre de la librería (privada)
        self.__nombre = nombre 
        # Catálogo: {título: precio} (privado)
        self.__catalogo = {} 
        # Instancia del Carrito
        self.__carrito = Carrito() 
        
        # Ejecutar verificación de invariantes al inicio
        self.__verificar_invariantes()

    def __verificar_invariantes(self):
        # Invariante 1: Precios Positivos
        for precio in self.__catalogo.values():
            assert precio > 0, "Invariante violada: Precio del libro debe ser mayor a 0."
            
        # Invariante 2: Rango de Descuento
        assert self.__MIN_DESCUENTO <= Libreria.__DESCUENTO_SOCIOS <= self.__MAX_DESCUENTO, \
               f"Invariante violada: El descuento debe estar entre {self.__MIN_DESCUENTO} y {self.__MAX_DESCUENTO}."
    @classmethod
    def set_descuento_socios(cls, nuevo_descuento):
        # Debe poder cambiarse con un mutador de clase que valide el rango [0.05, 0.10]
        try:
            assert cls.__MIN_DESCUENTO <= nuevo_descuento <= cls.__MAX_DESCUENTO, \
                   f"El descuento debe estar entre {cls.__MIN_DESCUENTO*100}% y {cls.__MAX_DESCUENTO*100}%."
            cls.__DESCUENTO_SOCIOS = nuevo_descuento
            print(f"Tasa de descuento de socios actualizada a {nuevo_descuento*100:.0f}%.")
        except AssertionError as e:
            print(f"Error al establecer descuento: {e}")
            
    # ----------------------------------------------------
    # Métodos Estáticos
    # ----------------------------------------------------
    @staticmethod
    def calcular_precio_con_descuento(monto, descuento):
        """
        Calcula el precio final aplicando un descuento.
        """
        # Asegurarse de que el monto sea positivo
        assert monto > 0, "Aserto violado: El monto a aplicar descuento debe ser positivo."
        # Asegurarse de que el descuento este dentro del intervalo establecido (0 a 1)
        assert 0 <= descuento <= 1, "Aserto violado: El descuento debe estar entre 0 y 1."
        
        # Crear un método estático que reciba un monto y el descuento para calcular el precio con descuento.
        precio_final = monto * (1 - descuento)
        
        # Verificar que el monto total a pagar sea positivo
        assert precio_final >= 0, "Aserto violado: El precio final no puede ser negativo."
        
        return precio_final
    
    def obtener_precio(self, titulo):
        # Un método que permita agregar un libro al catálogo. Utilizar un accesor para verificar que el libro este en el catálogo.
        return self.__catalogo.get(titulo)

    # --- Mutador (público) ---
    def agregar_libro_a_catalogo(self, titulo, precio):
        try:
            # Asegurarse de que los precios sean positivos utilizando asertos en los métodos donde se manejan precios.
            assert precio > 0, "Aserto violado: El precio del libro debe ser mayor a 0."
            
            self.__catalogo[titulo] = precio
            print(f"Libro '{titulo}' con precio ${precio:,.2f} agregado al catálogo.")
            self.__verificar_invariantes() # Re-verificar invariantes después de la mutación
        except AssertionError as e:
            print(f" Error al agregar libro: {e}")

    # --- Mutador (público) ---
    def agregar_libro_a_carrito(self, titulo):
        try:
            assert titulo in self.__catalogo, f"Aserto violado: El libro '{titulo}' no existe en el catálogo."
            
            self.__carrito.agregar_titulo(titulo)
            print(f"Libro '{titulo}' agregado al carrito.")
            # No es necesario __verificar_invariantes() ya que el precio y el descuento no cambian.
        except AssertionError as e:
            print(f"Error al agregar al carrito: {e}")

    # --- Método Público ---
    def calcular_total_carrito(self, es_frecuente=False):
        subtotal = 0.0
        
        for titulo in self.__carrito.obtener_titulos():
            if titulo in self.__catalogo:
                 subtotal += self.__catalogo[titulo]
    
        total = subtotal
        descuento_aplicado = 0.0
        
        if es_frecuente:
            # Si el cliente es frecuente (frecuente=True), aplica el descuento de clase usando la variable de clase.
            descuento_aplicado = Libreria.__DESCUENTO_SOCIOS
            # Usar el método estático para calcular el precio
            total = Libreria.calcular_precio_con_descuento(subtotal, descuento_aplicado)
        
        print("\n--- Resumen del Carrito ---")
        print(f"Subtotal: ${subtotal:,.2f}")
        print(f"Socio Frecuente: {'Sí' if es_frecuente else 'No'}")
        if es_frecuente:
            print(f"Descuento Aplicado ({descuento_aplicado*100:.0f}%): ${subtotal - total:,.2f}")
        print(f"TOTAL A PAGAR: ${total:,.2f}")
        
        # Se debe sumar los precios de los títulos del carrito.
        # Verificar que el monto total a pagar sea positivo
        assert total >= 0, "Aserto violado: El total a pagar debe ser positivo."
        return total

    # --- Accesor (público) ---
    def mostrar_catalogo(self):
        """Muestra el catálogo actual de la librería."""
        print(f"\n=== Catálogo de {self.__nombre} ===")
        for titulo, precio in self.__catalogo.items():
            print(f"- {titulo}: ${precio:,.2f}")
        print("---------------------------------")
        
    # --- Accesor (público) ---
    def mostrar_carrito(self):
        """Muestra los libros en el carrito."""
        titulos = self.__carrito.obtener_titulos()
        print(f"\n=== Carrito Actual ({len(titulos)} libros) ===")
        if titulos:
            for titulo in titulos:
                print(f"- {titulo}")
        else:
            print("El carrito está vacío.")
        print("---------------------------------")
        

# ----------------------------------------------------
# Ejemplo de Uso y Demostración de Requisitos
# ----------------------------------------------------
if __name__ == "__main__":
    
    libreria = Libreria("La Casa del Libro")

    # 1. Mutador de Clase y Validación de Rango
    print("--- 1. Gestión de Descuento de Clase ---")
    Libreria.set_descuento_socios(0.12) # Falla: fuera de [0.05, 0.10]
    Libreria.set_descuento_socios(0.08) # Éxito: Tasa actualizada

    # 2. Agregar Libro al Catálogo con Aserto (Precio Positivo)
    print("\n--- 2. Gestión de Catálogo y Asertos (Precio) ---")
    libreria.agregar_libro_a_catalogo("Cien Años de Soledad", 25000)
    libreria.agregar_libro_a_catalogo("1984", 18500)
    libreria.agregar_libro_a_catalogo("El Principito", 0) # Falla: Aserto de precio > 0

    # Uso del Accesor para verificar existencia y precio
    print(f"Precio de '1984': ${libreria.obtener_precio('1984'):,.2f}")
    libreria.mostrar_catalogo()

    # 3. Agregar Libro al Carrito con Aserto (Existencia)
    print("\n--- 3. Gestión de Carrito y Asertos (Existencia) ---")
    libreria.agregar_libro_a_carrito("Cien Años de Soledad")
    libreria.agregar_libro_a_carrito("1984")
    libreria.agregar_libro_a_carrito("El Quijote") # Falla: Aserto de existencia en catálogo

    libreria.mostrar_carrito()

    # 4. Cálculo del Total (Sin Descuento)
    print("\n--- 4. Cálculo de Total (Cliente Normal) ---")
    libreria.calcular_total_carrito(es_frecuente=False)

    # 5. Cálculo del Total (Con Descuento)
    print("\n--- 5. Cálculo de Total (Cliente Frecuente con 8%) ---")
    libreria.calcular_total_carrito(es_frecuente=True)

    # 6. Demostración del Método Estático
    print("\n--- 6. Método Estático: Cálculo de Oferta General ---")
    monto_ejemplo = 50000
    descuento_ejemplo = 0.15 # 15% de descuento general (fuera del rango de socios)
    precio_final = Libreria.calcular_precio_con_descuento(monto_ejemplo, descuento_ejemplo)
    print(f"Precio con 15% de descuento sobre ${monto_ejemplo:,.2f}: ${precio_final:,.2f}")

    # 7. Demostración de Aserto en Método Estático
    # Libreria.calcular_precio_con_descuento(-100, 0.10) # Descomentar para probar Aserto de Monto Positivo