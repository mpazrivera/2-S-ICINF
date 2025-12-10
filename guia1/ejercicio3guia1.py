class Producto:
    """
    Clase que representa un producto individual con control de stock y precio.
    """
    def __init__(self, nombre, precio, stock_inicial, codigo_barra):
        # Atributos [cite: 41, 42, 43, 44]
        self.nombre = nombre 
        self.precio = precio 
        self.cantidad_disponible = stock_inicial
        self.codigo_barra = codigo_barra
        # Atributo: historial de cambios en el stock (lista) [cite: 36, 45]
        self.historial_stock = [(stock_inicial, "Inicial")] 

    def __str__(self):
        """
        Método mágico para mostrar el estado actual del producto en formato texto.
        """
        # Método mágico para mostrar el estado actual del producto en formato texto [cite: 50]
        return (f" Producto: {self.nombre} (Cod: {self.codigo_barra})\n"
                f"   Precio Unitario: ${self.precio:,.2f}\n"
                f"   Stock Disponible: {self.cantidad_disponible} unidades\n"
                f"   Valor Total Stock: ${self.calcular_valor_total():,.2f}")

    def actualizar_stock(self, cambio_stock, razon):
        # Método que actualiza el stock del producto y añade el cambio al historial [cite: 49]
        if self.cantidad_disponible + cambio_stock >= 0:
            self.cantidad_disponible += cambio_stock
            self.historial_stock.append((cambio_stock, razon))
            print(f"Stock de '{self.nombre}' actualizado. Nuevo stock: {self.cantidad_disponible}")
        else:
            print(f" Error: No se puede decrementar el stock de '{self.nombre}' a menos de 0.")

    def calcular_valor_total(self):
        """
        Calcula el valor total de los productos disponibles.
        """
        # Implementar método que calcule el valor total de los productos disponibles [cite: 50]
        return self.precio * self.cantidad_disponible

class Inventario:
    def __init__(self):
        # Atributo: diccionario de productos, clave=código, valor=instancia Producto [cite: 35, 54]
        self.productos = {} 

    def agregar_producto(self, producto):
        """
        Agrega un nuevo producto al inventario. La clave es el código de barras.
        """
        # Método que agregue un nuevo producto al inventario [cite: 56]
        if producto.codigo_barra in self.productos:
            print(f" Error: El producto con código {producto.codigo_barra} ya existe.")
        else:
            self.productos[producto.codigo_barra] = producto
            print(f" Producto '{producto.nombre}' agregado al inventario.")

    def actualizar_stock_producto(self, codigo_barra, cambio_stock, razon):
        # Método que actualice el stock de un producto en el inventario [cite: 56]
        if codigo_barra in self.productos:
            self.productos[codigo_barra].actualizar_stock(cambio_stock, razon)
        else:
            print(f" Error: Producto con código {codigo_barra} no encontrado.")

    def mostrar_inventario(self):
        # Método que muestre todos los productos del inventario y sus detalles [cite: 57]
        print("\n=== Inventario Actual ===")
        if not self.productos:
            print("El inventario está vacío.")
            return
        
        for codigo, producto in self.productos.items():
            print("---")
            print(producto)
            print(f"   Historial de Stock: {producto.historial_stock}")
        print("-------------------------")
        print(f"VALOR TOTAL INVENTARIO: ${self.calcular_valor_total():,.2f}") # Se usa el método de valor total [cite: 58]

    def calcular_valor_total(self):
        """
        Calcula el valor total de todos los productos en el inventario.
        """
        # Implementar un método que calcule el valor total de todos los productos en el inventario [cite: 58]
        valor_total = sum(producto.calcular_valor_total() for producto in self.productos.values())
        return valor_total


# Ejemplo de Uso:
if __name__ == "__main__":
    # Crear instancias de Producto
    prod1 = Producto("Laptop", 850000.0, 10, "LTP001")
    prod2 = Producto("Mouse Óptico", 15000.0, 50, "MS002")

    # Crear instancia de Inventario
    mi_inventario = Inventario()

    # Agregar productos al inventario [cite: 56]
    mi_inventario.agregar_producto(prod1)
    mi_inventario.agregar_producto(prod2)

    # Mostrar inventario inicial [cite: 57]
    mi_inventario.mostrar_inventario()

    # Actualizar stock de un producto [cite: 56]
    mi_inventario.actualizar_stock_producto("LTP001", -2, "Venta a Cliente A")
    mi_inventario.actualizar_stock_producto("MS002", 15, "Recepción de Proveedor")

    # Mostrar inventario después de las actualizaciones
    mi_inventario.mostrar_inventario()