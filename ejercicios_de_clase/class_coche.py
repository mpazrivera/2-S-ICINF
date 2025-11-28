class Coche:
    def __init__(self, marca: str, gasolina: float, kilometros_recorridos: float = 0.0):
        self.marca = marca
        self.gasolina = gasolina
        self.kilometros_recorridos = kilometros_recorridos
        print(f"Coche {self.marca} creado ({self.gasolina:.1f}L).")

    def conducir(self, kilometros_a_recorrer: float):
        consumo_necesario = kilometros_a_recorrer / 10.0

        if consumo_necesario <= self.gasolina:
            # Gasolina suficiente
            self.gasolina -= consumo_necesario
            self.kilometros_recorridos += kilometros_a_recorrer
            print(f"\n--- Conducción Exitosa ---")
            print(f"El {self.marca} recorrió {kilometros_a_recorrer:.1f} km.")
            print(f"Gasolina restante: {self.gasolina:.1f} L. Km totales: {self.kilometros_recorridos:.1f}.")
        else:
            # Gasolina insuficiente
            kilometros_recorridos_reales = self.gasolina * 10.0
            self.kilometros_recorridos += kilometros_recorridos_reales
            self.gasolina = 0.0

            print(f"\n--- Sin Gasolina ---")
            print(f"El {self.marca} solo recorrió {kilometros_recorridos_reales:.1f} km y se **quedó sin gasolina**.")
            print(f"Km totales: {self.kilometros_recorridos:.1f} km.")

    def cargar_gasolina(self, litros: float):
        if litros > 0:
            self.gasolina += litros
            print(f"\nCargados {litros:.1f} L de gasolina al {self.marca}.")
            print(f"Gasolina total: {self.gasolina:.1f} L.")
        else:
            print("Cantidad de carga inválida.")


coche_a = Coche("Ford", 30.0)
coche_a.conducir(150.0)  # Consume 15L (150/10). Queda: 15.0L
coche_a.cargar_gasolina(10.0) # Queda: 25.0L
coche_a.conducir(300.0)  # Consume 30L. Solo recorre 250km (25*10).