class Vehiculo:
    def __init__(self, marca: str, modelo: str, año: int, precio: float):
        self.__marca = marca
        self.__modelo = modelo
        self.__año = año
        self.__precio = precio
        self.__disponible = True

    def marcar_vendido(self):
        self.__disponible = False

    def esta_disponible(self):
        return self.__disponible

    def get_modelo(self):
        return self.__modelo
    
    def __str__(self):
        estado = "Disponible" if self.__disponible else "Vendido"
        return f"{self.__marca} {self.__modelo} ({self.__año}) - Precio: ${self.__precio:,.2f} - Estado: {estado}"
    
class Concesionaria:
    def __init__(self):
        self.inventario = [] 
        print("Concesionaria iniciada.")

    def agregar_vehiculo(self, vehiculo: Vehiculo):
        self.inventario.append(vehiculo)
        print(f"Agregado: {vehiculo.get_modelo()}")

    def mostrar_vehiculos(self):
        if not self.inventario:
            print("El inventario está vacío.")
            return

        print("Inventario de Vehículos ---")
        for i, vehiculo in enumerate(self.inventario):
            print(f"{i+1}. {vehiculo}")

    def vender_vehiculo(self, modelo_a_vender: str):
        encontrado = False
        
        for vehiculo in self.inventario:
            if vehiculo.get_modelo().lower() == modelo_a_vender.lower():
                encontrado = True
                
                if vehiculo.esta_disponible():
                    vehiculo.marcar_vendido()
                    print(f"Venta Exitosa: {modelo_a_vender} vendido y marcado como no disponible.")
                    return
                else:
                    print(f"Fallo en Venta: {modelo_a_vender} ya fue vendido.")
                    return
        
        if not encontrado:
            print(f"Error: Vehículo '{modelo_a_vender}' no encontrado.")

#Crear instancia y agregar vehículos.
print("Carga de Inventario")
mi_concesionaria = Concesionaria()

v1 = Vehiculo("Kia", "Picanto", 2024, 15000.00)
v2 = Vehiculo("Mazda", "CX-5", 2023, 35500.00)
v3 = Vehiculo("Tesla", "Model 3", 2025, 50000.00)

mi_concesionaria.agregar_vehiculo(v1)
mi_concesionaria.agregar_vehiculo(v2)
mi_concesionaria.agregar_vehiculo(v3)

print("Inventario Inicial")
mi_concesionaria.mostrar_vehiculos()

print("Realizar Venta")
mi_concesionaria.vender_vehiculo("CX-5")


print("nventario Final")
mi_concesionaria.mostrar_vehiculos()