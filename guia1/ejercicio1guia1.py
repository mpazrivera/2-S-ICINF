from datetime import datetime

class ReservaHostal:
    def __init__(self, nombre_cliente, fecha_entrada_str, fecha_salida_str, numero_habitacion):
        
        self.nombre_cliente = nombre_cliente  # Atributo: nombre del cliente [cite: 11]
        self.numero_habitacion = numero_habitacion # Atributo: número de habitación [cite: 11]
        
        # Convertir las cadenas de fecha a objetos datetime
        self.fecha_entrada = datetime.strptime(fecha_entrada_str, '%Y-%m-%d') # Atributo: fecha de entrada [cite: 11]
        self.fecha_salida = datetime.strptime(fecha_salida_str, '%Y-%m-%d')   # Atributo: fecha de salida [cite: 11]

    def __del__(self):
        print(f"Reserva de {self.nombre_cliente} para la habitación {self.numero_habitacion} ha sido cancelada.") [cite: 17]

    def __str__(self):
        """
        Método mágico para mostrar la información de la reserva en formato legible.
        """
        duracion = self.calcular_duracion_estadia() # Uso del método de cálculo
        return (f" Reserva de Hostal\n"
                f"   Cliente: {self.nombre_cliente}\n"
                f"   Habitación: {self.numero_habitacion}\n"
                f"   Entrada: {self.fecha_entrada.strftime('%Y-%m-%d')}\n"
                f"   Salida: {self.fecha_salida.strftime('%Y-%m-%d')}\n"
                f"   Duración: {duracion} noches") [cite: 15]

    def calcular_duracion_estadia(self):
        """
        Calcula la duración de la estadía en días (noches).
        """
        # Método para calcular la duración de la estadía [cite: 14]
        duracion = self.fecha_salida - self.fecha_entrada
        return duracion.days

    def cambiar_fecha_salida(self, nueva_fecha_salida_str):
        """
        Cambia la fecha de salida de la reserva.
        """
        try:
            # Método para cambiar la fecha de salida [cite: 16]
            nueva_fecha = datetime.strptime(nueva_fecha_salida_str, '%Y-%m-%d')
            if nueva_fecha > self.fecha_entrada:
                self.fecha_salida = nueva_fecha
                print(f" Fecha de salida actualizada a {nueva_fecha_salida_str}.")
            else:
                print(" La nueva fecha de salida debe ser posterior a la fecha de entrada.")
        except ValueError:
            print("Formato de fecha inválido. Use YYYY-MM-DD.")


# Ejemplo de Uso:
if __name__ == "__main__":
    print("--- 1. Creación de una reserva ---")
    reserva1 = ReservaHostal(
        nombre_cliente="Ana Torres",
        fecha_entrada_str="2025-12-10",
        fecha_salida_str="2025-12-15",
        numero_habitacion=201
    )
    print(reserva1)

    print("\n--- 2. Modificación de fecha de salida ---")
    reserva1.cambiar_fecha_salida("2025-12-18")
    print(f"Nueva duración: {reserva1.calcular_duracion_estadia()} noches")
    print(reserva1)
    
    print("\n--- 3. Cancelación de la reserva (Eliminación del objeto) ---")
    del reserva1 # Se debe eliminar un objeto ReservaHostal [cite: 17]
    print("El objeto reserva1 ha sido eliminado.")