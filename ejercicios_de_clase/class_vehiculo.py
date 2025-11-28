class Vehiculo:
    def __init__(self, marca: str, modelo: str, año: int):
        self.__marca = marca
        self.__modelo = modelo
        self.__año = año
        self.__disponible = True

    def marcar_vendido(self):
        if self.__disponible:
            self.__disponible = False
            print(f"El vehículo {self.__marca} {self.__modelo} ({self.__año}) ha sido marcado como **Vendido**.")
        else:
            print(f"El vehículo ya estaba marcado como no disponible.")

    def __str__(self):
        estado = "Sí (Disponible)" if self.__disponible else "No (Vendido)"
        return (
            f"--- Detalles del Vehículo ---\n"
            f"Marca: {self.__marca}\n"
            f"Modelo: {self.__modelo}\n"
            f"Año: {self.__año}\n"
            f"Disponibilidad: {estado}"
        )

# --- Ejemplos de Uso ---
coche = Vehiculo("Honda", "CRV", 2024)

print("Estado Inicial:")
print(coche)

coche.marcar_vendido()

print("\nEstado Final:")
print(coche)